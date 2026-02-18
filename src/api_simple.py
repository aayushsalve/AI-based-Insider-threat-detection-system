import logging
import pandas as pd
from functools import wraps
from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS
import plotly.express as px
import plotly.graph_objects as go
import traceback
import sys


def chart_to_html(fig):
    """Convert Plotly figure to HTML string"""
    # Do NOT include plotly.js in every chart, only in the dashboard HTML
    return fig.to_html(
        full_html=False,
        include_plotlyjs=False,
        config={'editable': False, 'displayModeBar': False}
    )


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # <-- Add this line right after creating the Flask app

app.config['SECRET_KEY'] = 'insider-threat-api-key-2026'

# Load results (no model loading)
try:
    results_path = (
        r"D:\Major Project\Insider Threat Detection\reports"
        r"\detailed_results_20260217_122948.csv"
    )
    results_df = pd.read_csv(results_path)
    logger.info(f"✅ Loaded {len(results_df)} threat assessments")
except Exception as e:
    logger.error(f"❌ Failed to load results: {str(e)}")
    traceback.print_exc()
    results_df = pd.DataFrame()


# API Key validation decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != 'insider-threat-api-2026':
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.route('/api/v1/health', methods=['GET'])
def health():
    """Health check"""
    logger.info("Health check requested")
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'data_points': len(results_df)
    })


@app.route('/api/v1/stats', methods=['GET'])
@require_api_key
def stats():
    """System statistics"""
    logger.info("Stats requested")
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    critical_count = len(
        results_df[results_df['risk_level'] == 'Critical']
    )
    high_count = len(
        results_df[results_df['risk_level'] == 'High']
    )
    return jsonify({
        'total_users': len(results_df),
        'critical_count': critical_count,
        'high_count': high_count,
        'avg_risk_score': float(results_df['risk_score'].mean()),
        'avg_confidence': float(results_df['confidence'].mean()),
        'last_updated': datetime.now().isoformat()
    })


@app.route('/api/v1/critical-threats', methods=['GET'])
@require_api_key
def get_critical_threats():
    """Get only CRITICAL threats"""
    logger.info("Critical threats requested")
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    critical = results_df[results_df['risk_level'] == 'Critical']
    critical = critical.sort_values('risk_score', ascending=False)

    threat_data = critical[['user_id', 'risk_score', 'confidence']]
    return jsonify({
        'threats': threat_data.to_dict('records'),
        'count': len(critical),
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/v1/threats', methods=['GET'])
@require_api_key
def get_threats():
    """Get all threats above threshold"""
    logger.info("Threats requested")
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    threshold = request.args.get('threshold', default=5.0, type=float)
    limit = request.args.get('limit', default=50, type=int)

    threats = results_df[results_df['risk_score'] >= threshold]
    threats = threats.nlargest(limit, 'risk_score')

    threat_cols = [
        'user_id', 'risk_score', 'risk_level', 'confidence'
    ]
    return jsonify({
        'threats': threats[threat_cols].to_dict('records'),
        'total': len(threats)
    })


@app.route('/api/v1/user/<user_id>/profile', methods=['GET'])
@require_api_key
def user_profile(user_id):
    """Get detailed user profile"""
    logger.info(f"Profile requested for {user_id}")
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    user_data = results_df[results_df['user_id'] == user_id]

    if user_data.empty:
        return jsonify({'error': 'User not found'}), 404

    user = user_data.iloc[0]

    return jsonify({
        'user_id': user_id,
        'risk_assessment': {
            'risk_score': float(user['risk_score']),
            'risk_level': user['risk_level'],
            'confidence': float(user['confidence'])
        },
        'behavior_metrics': {
            'total_activities': int(user['total_activities']),
            'failed_activities': int(user['failed_activities']),
            'downloads': int(user['downloads_count']),
            'sensitive_files': int(user['sensitive_files_accessed']),
            'after_hours_access': int(user['after_hours_access']),
            'unique_locations': int(user['unique_locations'])
        }
    })


@app.route('/api/v1/overview', methods=['GET'])
@require_api_key
def overview():
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    total = len(results_df)
    critical = (
        len(results_df[results_df['risk_level'] == 'Critical'])
        if 'risk_level' in results_df else 0
    )
    high = (
        len(results_df[results_df['risk_level'] == 'High'])
        if 'risk_level' in results_df else 0
    )
    avg_risk = (
        float(results_df['risk_score'].mean())
        if 'risk_score' in results_df else 0.0
    )
    detection_rate = (
        f"{((critical + high) / total * 100):.1f}%"
        if total > 0 else "0.0%"
    )

    return jsonify({
        'total_users': total,
        'critical_threats': critical,
        'high_threats': high,
        'avg_risk_score': avg_risk,
        'detection_rate': detection_rate
    })


@app.route('/api/v1/risk-distribution', methods=['GET'])
@require_api_key
def risk_distribution():
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    if 'risk_level' in results_df:
        counts = results_df['risk_level'].value_counts().reset_index()
        counts.columns = ['risk_level', 'count']
        fig = px.pie(
            counts,
            names='risk_level',
            values='count',
            title='Risk Distribution by Level'
        )
        return jsonify({'chart': chart_to_html(fig)})
    else:
        fig = go.Figure()
        fig.update_layout(title='Risk Distribution (No Data)')
        return jsonify({'chart': chart_to_html(fig)})


@app.route('/api/v1/anomaly-indicators', methods=['GET'])
@require_api_key
def anomaly_indicators():
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    candidate_cols = [
        'failed_activities', 'downloads_count', 'sensitive_files_accessed',
        'after_hours_access', 'unique_locations'
    ]
    cols = [c for c in candidate_cols if c in results_df.columns]
    if not cols:
        fig = go.Figure()
        fig.update_layout(title='Anomaly Indicators (No Data)')
        return jsonify({'chart': chart_to_html(fig)})

    means = results_df[cols].mean().reset_index()
    means.columns = ['indicator', 'mean_value']
    maxs = results_df[cols].max().reset_index()
    maxs.columns = ['indicator', 'max_value']
    merged = pd.merge(means, maxs, on='indicator')
    fig = go.Figure(data=[
        go.Bar(name='Mean', x=merged['indicator'], y=merged['mean_value']),
        go.Bar(name='Max', x=merged['indicator'], y=merged['max_value'])
    ])
    fig.update_layout(barmode='group', title='Anomaly Indicators (Mean & Max)')
    return jsonify({'chart': chart_to_html(fig)})


@app.route('/api/v1/top-threats', methods=['GET'])
@require_api_key
def top_threats():
    """Get all users (not just top by risk_score)"""
    logger.info("All users requested")
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    limit = request.args.get('limit', default=10000, type=int)
    cols = ['user_id', 'risk_score', 'risk_level', 'confidence']
    if 'anomaly_score' in results_df:
        cols.append('anomaly_score')

    # Return up to 'limit' users as they appear in the file
    top = results_df.head(limit)
    return jsonify({'threats': top[cols].fillna(0).to_dict('records')})


@app.route('/api/v1/timeline', methods=['GET'])
@require_api_key
def timeline():
    if results_df.empty:
        return jsonify({'error': 'No data loaded'}), 500

    fig = go.Figure()
    # Show top 5 users' timelines
    top_users = (
        results_df.sort_values('risk_score', ascending=False)['user_id']
        .unique()[:5]
    )
    for user_id in top_users:
        user_df = results_df[results_df['user_id'] == user_id]
        if 'timestamp' in user_df:
            user_df = user_df.copy()
            user_df['timestamp'] = pd.to_datetime(
                user_df['timestamp'], errors='coerce'
            )
            user_df = user_df.dropna(subset=['timestamp'])
            user_df = user_df.sort_values('timestamp')
            fig.add_trace(go.Scatter(
                x=user_df['timestamp'],
                y=user_df['risk_score'],
                mode='lines+markers',
                name=str(user_id)
            ))
    fig.update_layout(
        title='Risk Score Timeline (Top 5 Users)',
        xaxis_title='Time',
        yaxis_title='Risk Score'
    )
    return jsonify({'chart': chart_to_html(fig)})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    logger.error(f"Server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500


@app.route('/')
def root():
    return jsonify({"message": "Insider Threat Detection API"})


if __name__ == '__main__':
    try:
        logger.info("="*60)
        logger.info("Starting Insider Threat Detection API")
        logger.info("="*60)
        app.run(debug=False, host='127.0.0.1', port=5001, threaded=True)
    except Exception as e:
        logger.error(f"Failed to start API: {str(e)}")
        traceback.print_exc()
        sys.exit(1)
