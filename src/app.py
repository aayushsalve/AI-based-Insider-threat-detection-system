import logging
import pandas as pd
import numpy as np
from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'insider-threat-detection-2026'

# Load data only (no model/scaler)
results_df = pd.read_csv(
    PATHS["reports"] / "detailed_results_20260217_122948.csv"
)


@app.route('/')
@app.route('/dashboard')
def dashboard():
    """Main dashboard"""
    return render_template('dashboard.html')


@app.route('/api/overview')
def get_overview():
    """Dashboard overview metrics"""
    critical = len(results_df[results_df['risk_level'] == 'Critical'])
    high = len(results_df[results_df['risk_level'] == 'High'])
    medium = len(results_df[results_df['risk_level'] == 'Medium'])
    low = len(results_df[results_df['risk_level'] == 'Low'])

    detection_rate = (
        results_df['risk_level']
        .isin(['Critical', 'High'])
        .sum() / len(results_df) * 100
    )
    return jsonify({
        'total_users': len(results_df),
        'critical_threats': critical,
        'high_threats': high,
        'medium_threats': medium,
        'low_threats': low,
        'avg_risk_score': float(results_df['risk_score'].mean()),
        'detection_rate': f"{detection_rate:.1f}%"
    })


@app.route('/api/risk-distribution')
def risk_distribution():
    """Risk level distribution pie chart"""
    risk_counts = results_df['risk_level'].value_counts()

    fig = go.Figure(data=[go.Pie(
        labels=risk_counts.index,
        values=risk_counts.values,
        marker=dict(colors=['#d32f2f', '#f57c00', '#fbc02d', '#388e3c'])
    )])

    fig.update_layout(title='Risk Level Distribution')
    return jsonify({
        'chart': fig.to_html(
            include_plotlyjs=False,
            div_id='risk-dist'
        )
    })


@app.route('/api/top-threats')
def top_threats():
    """Top 10 threats ranked by risk score"""
    columns = ['user_id', 'risk_score', 'risk_level', 'anomaly_score', 'confidence']
    top10 = results_df.nlargest(10, 'risk_score')[columns].fillna('N/A')
    return jsonify({'threats': top10.to_dict('records')})


@app.route('/api/anomaly-indicators')
def anomaly_indicators():
    """Top anomaly features"""
    features = {
        'Feature': [
            'Sensitive After-Hours Access',
            'Failed Login Rate',
            'Unique Locations',
            'Download Rate',
            'Activity Frequency',
            'After-Hours Access',
            'Failed Activities',
            'Sensitive Files Accessed'
        ],
        'Importance': [0.156, 0.124, 0.098, 0.087, 0.076, 0.065, 0.052, 0.048]
    }
    
    fig = px.bar(x=features['Feature'], y=features['Importance'],
                 title='Top Anomaly Indicators',
                 labels={'x': 'Feature', 'y': 'Importance Score'})

    return jsonify({
        'chart': fig.to_html(
            include_plotlyjs=False,
            div_id='anomaly-ind'
        )
    })


@app.route('/api/user/<user_id>')
def user_detail(user_id):
    """Detailed user profile"""
    user_data = results_df[results_df['user_id'] == user_id]
    
    if user_data.empty:
        return jsonify({'error': 'User not found'}), 404
    
    user = user_data.iloc[0].to_dict()
    
    return jsonify({
        'user_id': user_id,
        'risk_score': float(user['risk_score']),
        'risk_level': user['risk_level'],
        'confidence': float(user['confidence']),
        'anomaly_score': float(user['anomaly_score']),
        'supervised_score': float(user['supervised_score']),
        'details': {
            'total_activities': int(user['total_activities']),
            'failed_activities': int(user['failed_activities']),
            'downloads_count': int(user['downloads_count']),
            'sensitive_files_accessed': int(user['sensitive_files_accessed']),
            'after_hours_access': int(user['after_hours_access']),
            'failed_login_rate': float(user['failed_login_rate']),
            'unique_locations': int(user['unique_locations'])
        }
    })


@app.route('/api/timeline')
def timeline():
    """Risk scores over time (simulated)"""
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    # Simulated data
    scores = np.random.normal(4.5, 2, 30).clip(0, 10)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=scores, mode='lines+markers',
        name='Avg Risk Score'
    ))
    fig.update_layout(
        title='Risk Score Timeline (30 days)',
        xaxis_title='Date',
        yaxis_title='Risk Score'
    )
    
    return jsonify({
        'chart': fig.to_html(
            include_plotlyjs=False,
            div_id='timeline'
        )
    })


@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Active alerts"""
    critical = results_df[results_df['risk_level'] == 'Critical']
    alerts = []
    
    for _, row in critical.head(5).iterrows():
        alerts.append({
            'user_id': row['user_id'],
            'type': 'CRITICAL_THREAT',
            'message': f"Critical threat detected: {row['user_id']}",
            'timestamp': datetime.now().isoformat(),
            'risk_score': float(row['risk_score'])
        })
    
    return jsonify({'alerts': alerts})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    logger.info("Starting Insider Threat Detection Dashboard")
    app.run(debug=True, host='0.0.0.0', port=5000)
