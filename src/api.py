from flask import Flask, jsonify, request
from functools import wraps
import logging
from datetime import datetime
import pandas as pd
from config import PATHS
import pickle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'insider-threat-api-key-2026'

# Load model & results
with open(PATHS["models"] / "calibrated_supervised.pkl", 'rb') as f:
    model = pickle.load(f)

results_df = pd.read_csv(
    PATHS["reports"] / "detailed_results_20260217_122948.csv"
)


# API Key validation
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != 'insider-threat-api-2026':
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated

# ============ THREAT SCORING ENDPOINTS ============


@app.route('/api/v1/score-user', methods=['POST'])
@require_api_key
def score_user():
    """Score a single user"""
    data = request.json
    user_id = data.get('user_id')
    
    user_data = results_df[results_df['user_id'] == user_id]
    if user_data.empty:
        return jsonify({'error': 'User not found'}), 404
    
    user = user_data.iloc[0]
    
    return jsonify({
        'user_id': user_id,
        'risk_score': float(user['risk_score']),
        'risk_level': user['risk_level'],
        'anomaly_score': float(user['anomaly_score']),
        'supervised_score': float(user['supervised_score']),
        'confidence': float(user['confidence']),
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/v1/score-batch', methods=['POST'])
@require_api_key
def score_batch():
    """Score multiple users"""
    data = request.json
    user_ids = data.get('user_ids', [])
    
    results = []
    for uid in user_ids:
        user_data = results_df[results_df['user_id'] == uid]
        if not user_data.empty:
            user = user_data.iloc[0]
            results.append({
                'user_id': uid,
                'risk_score': float(user['risk_score']),
                'risk_level': user['risk_level']
            })
    
    return jsonify({'results': results, 'count': len(results)})


@app.route('/api/v1/threats', methods=['GET'])
@require_api_key
def get_threats():
    """Get all threats above threshold"""
    threshold = request.args.get('threshold', default=5.0, type=float)
    limit = request.args.get('limit', default=50, type=int)
    
    threats = results_df[results_df['risk_score'] >= threshold].nlargest(
        limit, 'risk_score'
    )
    
    threat_columns = ['user_id', 'risk_score', 'risk_level',
                      'confidence']
    return jsonify({
        'threats': threats[threat_columns].to_dict('records'),
        'total': len(threats)
    })


@app.route('/api/v1/Critical-threats', methods=['GET'])
@require_api_key
def get_critical_threats():
    """Get only CRITICAL threats"""
    critical = results_df[results_df['risk_level'] == 'Critical']
    
    threat_data = critical[
        ['user_id', 'risk_score', 'confidence']
    ].to_dict('records')
    
    return jsonify({
        'threats': threat_data,
        'count': len(critical),
        'timestamp': datetime.now().isoformat()
    })


# ============ USER PROFILE ENDPOINTS ============

@app.route('/api/v1/user/<user_id>/profile', methods=['GET'])
@require_api_key
def user_profile(user_id):
    """Get detailed user profile"""
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
        },
        'anomaly_indicators': {
            'anomaly_score': float(user['anomaly_score']),
            'supervised_score': float(user['supervised_score']),
            'failed_login_rate': float(user['failed_login_rate']),
            'sensitive_after_hours_rate': float(
                user['sensitive_after_hours_rate']
            )
        }
    })

# ============ HEALTH & MONITORING ============


@app.route('/api/v1/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'model_status': 'loaded',
        'data_points': len(results_df)
    })


@app.route('/api/v1/stats', methods=['GET'])
def stats():
    """System statistics"""
    return jsonify({
        'total_users': len(results_df),
        'critical_count': len(
            results_df[results_df['risk_level'] == 'Critical']
        ),
        'high_count': len(results_df[results_df['risk_level'] == 'High']),
        'avg_risk_score': float(results_df['risk_score'].mean()),
        'avg_confidence': float(results_df['confidence'].mean()),
        'last_updated': datetime.now().isoformat()
    })

# ============ ERROR HANDLERS ============


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logger.info("Starting API Server on port 5001")
    app.run(debug=False, host='0.0.0.0', port=5001)
