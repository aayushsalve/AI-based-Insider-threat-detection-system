
from flask import (
    Flask, render_template, session, redirect, url_for,
    request, flash, jsonify, Response
)
import base64
import random
from datetime import datetime, timedelta
import math


app = Flask(__name__)
app.secret_key = 'insider_threat_demo_key_2026'


# ---------------------------------------------------------------------------
# Formal Risk Scoring Model
# Formula: Risk Score = Σ(weight_i × factor_i) × 10  →  [0, 10]
# Weights: Anomaly=0.40, Sensitive Access=0.30,
#          Login Anomalies=0.20, Behavioral=0.10
# ---------------------------------------------------------------------------
RISK_WEIGHTS = {
    'anomaly':          0.40,
    'sensitive_access': 0.30,
    'login_anomaly':    0.20,
    'behavioral':       0.10,
}


def compute_risk_score(user_id: int, status: str) -> dict:
    """Return a deterministic formal risk score for a user.

    Each factor is in [0, 1]; the weighted sum is scaled to [0, 10].
    A fixed seed derived from user_id ensures scores are stable across
    page reloads while still varying per user.
    """
    rng = random.Random(user_id * 31337)

    # Base factors depend on account status
    status_boost = {
        'Alert':      0.55,
        'Blocked':    0.70,
        'Restricted': 0.50,
        'Active':     0.20,
        'Normal':     0.10,
    }.get(status, 0.10)

    anomaly_factor   = min(1.0, status_boost + rng.uniform(0.00, 0.40))
    sensitive_factor = min(1.0, status_boost * 0.8 + rng.uniform(0.00, 0.35))
    login_factor     = min(1.0, status_boost * 0.6 + rng.uniform(0.00, 0.30))
    behavioral_factor = rng.uniform(0.00, 0.25)

    raw_score = (
        RISK_WEIGHTS['anomaly']          * anomaly_factor +
        RISK_WEIGHTS['sensitive_access'] * sensitive_factor +
        RISK_WEIGHTS['login_anomaly']    * login_factor +
        RISK_WEIGHTS['behavioral']       * behavioral_factor
    ) * 10

    score = round(min(10.0, max(0.0, raw_score)), 1)

    if score >= 7.5:
        level = 'Critical'
    elif score >= 5.0:
        level = 'High'
    elif score >= 2.5:
        level = 'Medium'
    else:
        level = 'Low'

    return {
        'score': score,
        'level': level,
        'breakdown': {
            'anomaly':          round(anomaly_factor   * RISK_WEIGHTS['anomaly']          * 10, 2),
            'sensitive_access': round(sensitive_factor * RISK_WEIGHTS['sensitive_access'] * 10, 2),
            'login_anomaly':    round(login_factor     * RISK_WEIGHTS['login_anomaly']    * 10, 2),
            'behavioral':       round(behavioral_factor * RISK_WEIGHTS['behavioral']      * 10, 2),
        }
    }


LEVEL_COLORS = {
    'Critical': 'danger',
    'High':     'warning',
    'Medium':   'info',
    'Low':      'success',
}


def enrich_user_risk(user: dict) -> dict:
    """Attach risk fields to a user dict in-place and return it."""
    rd = compute_risk_score(user['id'], user.get('status', 'Normal'))
    user['risk_score'] = rd['score']
    user['risk_level'] = rd['level']
    user['risk_color'] = LEVEL_COLORS[rd['level']]
    user['risk_breakdown'] = rd['breakdown']
    return user


@app.route('/favicon.ico')
def favicon():
    """Return a tiny 1x1 PNG as the favicon to avoid 404s."""
    png_b64 = (
        'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nG'
        'NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII='
    )
    png = base64.b64decode(png_b64)
    return Response(png, mimetype='image/png')


# Demo users list (initial)
users = [
    {
        "id": 1,
        "name": "Amit Sharma",
        "role": "User",
        "email": "amit@company.com",
        "phone": "+91-9876543210",
        "avatar": "https://randomuser.me/api/portraits/men/1.jpg",
        "status": "Alert",
        "username": "amit",
        "password": "adminpass"  # Plaintext for demo only
    },
    {
        "id": 2,
        "name": "Priya Singh",
        "role": "User",
        "email": "priya@company.com",
        "phone": "+91-9123456780",
        "avatar": "https://randomuser.me/api/portraits/women/2.jpg",
        "status": "Normal",
        "username": "priya",
        "password": "analystpass"
    },
    {
        "id": 3,
        "name": "Aayush S",
        "role": "Admin",
        "email": "aayush@company.com",
        "phone": "+91-9000000003",
        "avatar": "https://randomuser.me/api/portraits/men/3.jpg",
        "status": "Active",
        "username": "aayush",
        "password": "aayushadminpass"
    },
    {
        "id": 4,
        "name": "Aryan Wagh",
        "role": "User",
        "email": "aryan@company.com",
        "phone": "+91-9000000004",
        "avatar": "https://randomuser.me/api/portraits/men/4.jpg",
        "status": "Normal",
        "username": "aryan",
        "password": "aryanpass"
    },
]


# Populate more random Indian users if not present
_populated = False


def populate_random_users(count=50):
    global _populated
    if _populated:
        return
    first_names = [
        'Rahul', 'Saurabh', 'Vikram', 'Rohit', 'Sanjay', 'Karan', 'Rakesh',
        'Manish', 'Neha', 'Anjali', 'Sunita', 'Pooja', 'Sakshi', 'Divya',
        'Asha', 'Priya', 'Vijay', 'Amit', 'Aayush', 'Aryan', 'Ritu', 'Ankit',
        'Aditya', 'Harsh', 'Kavita', 'Rohan', 'Ishaan', 'Kabir', 'Madhav',
        'Ramesh', 'Siddharth'
    ]
    last_names = [
        'Sharma', 'Kumar', 'Patel', 'Singh', 'Gupta', 'Mehta', 'Joshi',
        'Reddy', 'Nair', 'Desai', 'Iyer', 'Bose', 'Chatterjee', 'Verma',
        'Ghosh'
    ]
    start_id = max(u['id'] for u in users) + 1
    for i in range(count):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        name = f"{fn} {ln}"
        username = (fn[0] + ln).lower() + str(start_id + i)
        email = f"{username}@example.com"
        phone = f"+91-9{random.randint(100000000, 999999999)}"
        avatar = (
            f"https://randomuser.me/api/portraits/lego/"
            f"{random.randint(1, 9)}.jpg"
        )
        users.append({
            'id': start_id + i,
            'name': name,
            'role': 'User',
            'email': email,
            'phone': phone,
            'avatar': avatar,
            'status': 'Normal',
            'username': username,
            'password': f'pass{start_id + i}'
        })
    _populated = True


# ensure there are many users
populate_random_users(50)

# Attach risk scores to all users once at startup
for _u in users:
    enrich_user_risk(_u)


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    # Find the logged-in user
    user = next(
        (u for u in users if u['username'] == session['username']),
        None
    )
    # Re-enrich risk scores (status may have changed since startup)
    for _u in users:
        enrich_user_risk(_u)

    # --- Summary statistics ---
    total_users = len(users)
    critical_users = [u for u in users if u['risk_level'] == 'Critical']
    high_users     = [u for u in users if u['risk_level'] == 'High']
    alerts_today   = len(critical_users)
    suspicious_activities = len(high_users)

    # Top-5 highest-risk users for the leaderboard panel
    top_risk_users = sorted(users, key=lambda x: x['risk_score'], reverse=True)[:5]

    # Risk distribution counts for the donut chart
    risk_distribution = {
        'Critical': len(critical_users),
        'High':     len(high_users),
        'Medium':   len([u for u in users if u['risk_level'] == 'Medium']),
        'Low':      len([u for u in users if u['risk_level'] == 'Low']),
    }

    # --- Recent activities with risk scores injected ---
    now = datetime.now()
    rng_act = random.Random(int(now.strftime('%Y%m%d%H')))
    recent_activities = []

    flagged_actions = [
        'Downloaded sensitive file',
        'Multiple failed logins',
        'Accessed restricted folder',
        'Large data transfer',
        'Alert triggered',
        'Privilege escalation attempt',
        'USB device connected',
    ]
    normal_actions = [
        'Login', 'Viewed dashboard', 'Opened report',
        'Submitted timesheet', 'Attended meeting',
    ]

    for u in critical_users + high_users:
        recent_activities.append({
            'user':       u['name'],
            'user_id':    u['id'],
            'action':     rng_act.choice(flagged_actions),
            'time':       (now - timedelta(minutes=rng_act.randint(1, 360))).strftime('%Y-%m-%d %H:%M'),
            'status':     'Flagged',
            'risk_score': u['risk_score'],
            'risk_level': u['risk_level'],
            'risk_color': u['risk_color'],
        })

    normal_pool = [u for u in users if u['risk_level'] in ('Low', 'Medium')]
    while len(recent_activities) < 15 and normal_pool:
        u = rng_act.choice(normal_pool)
        recent_activities.append({
            'user':       u['name'],
            'user_id':    u['id'],
            'action':     rng_act.choice(normal_actions),
            'time':       (now - timedelta(minutes=rng_act.randint(1, 1440))).strftime('%Y-%m-%d %H:%M'),
            'status':     'Normal',
            'risk_score': u['risk_score'],
            'risk_level': u['risk_level'],
            'risk_color': u['risk_color'],
        })

    recent_activities.sort(key=lambda x: x['risk_score'], reverse=True)

    return render_template(
        'dashboard.html',
        user=user,
        users=users,
        total_users=total_users,
        alerts_today=alerts_today,
        suspicious_activities=suspicious_activities,
        recent_activities=recent_activities,
        top_risk_users=top_risk_users,
        risk_distribution=risk_distribution,
        level_colors=LEVEL_COLORS,
    )


@app.route('/api/v1/threats')
def threats():
    return jsonify({
        "trend": [5, 7, 3, 8, 6, 9, 4],
        "distribution": [10, 20, 5]
    })


@app.route('/api/v1/risk')
def risk_api():
    """Return risk scores for all users — demo API endpoint."""
    for _u in users:
        enrich_user_risk(_u)
    payload = [
        {
            'id':         u['id'],
            'name':       u['name'],
            'risk_score': u['risk_score'],
            'risk_level': u['risk_level'],
            'breakdown':  u['risk_breakdown'],
            'status':     u['status'],
        }
        for u in sorted(users, key=lambda x: x['risk_score'], reverse=True)
    ]
    return jsonify({'users': payload, 'generated_at': datetime.now().isoformat()})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next(
            (u for u in users if u['username'] == username
                and u['password'] == password),
            None
        )
        if user:
            session['username'] = username
            # store role in session for quick checks
            session['role'] = user.get('role', 'User')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))


def get_user_by_id(user_id):
    return next((u for u in users if u.get('id') == user_id), None)


def get_user_by_username(username):
    return next((u for u in users if u.get('username') == username), None)


@app.route('/user/<int:user_id>/restrict', methods=['POST'])
def restrict_user(user_id):
    # Admin-only action: set status to Restricted
    if session.get('role') != 'Admin':
        flash('Permission denied', 'danger')
        return redirect(url_for('dashboard'))
    u = get_user_by_id(user_id)
    if not u:
        flash('User not found', 'danger')
        return redirect(url_for('dashboard'))
    u['status'] = 'Restricted'
    flash(f"User {u['name']} restricted", 'success')
    return redirect(url_for('dashboard'))


@app.route('/user/<int:user_id>/block', methods=['POST'])
def block_user(user_id):
    # Admin-only action: set status to Blocked
    if session.get('role') != 'Admin':
        flash('Permission denied', 'danger')
        return redirect(url_for('dashboard'))
    u = get_user_by_id(user_id)
    if not u:
        flash('User not found', 'danger')
        return redirect(url_for('dashboard'))
    u['status'] = 'Blocked'
    flash(f"User {u['name']} blocked", 'success')
    return redirect(url_for('dashboard'))


@app.route('/user/<int:user_id>/unblock', methods=['POST'])
def unblock_user(user_id):
    # Admin-only action: set status to Normal/Active
    if session.get('role') != 'Admin':
        flash('Permission denied', 'danger')
        return redirect(url_for('dashboard'))
    u = get_user_by_id(user_id)
    if not u:
        flash('User not found', 'danger')
        return redirect(url_for('dashboard'))
    u['status'] = 'Active'
    flash(f"User {u['name']} unblocked", 'success')
    return redirect(url_for('dashboard'))


@app.route('/user/<int:user_id>', methods=['GET'])
def view_profile(user_id):
    # Admin can view any profile; others can view only their own
    u = get_user_by_id(user_id)
    if not u:
        flash('User not found', 'danger')
        return redirect(url_for('dashboard'))
    # if not admin and not the same user, deny
    if session.get('role') != 'Admin':
        current = get_user_by_username(session.get('username'))
        if not current or current.get('id') != user_id:
            flash('Permission denied', 'danger')
            return redirect(url_for('dashboard'))
    return render_template('profile.html', user=u)


@app.route('/user/<int:user_id>/set_role', methods=['POST'])
def set_role(user_id):
    # Admin-only: change role
    if session.get('role') != 'Admin':
        flash('Permission denied', 'danger')
        return redirect(url_for('dashboard'))
    new_role = request.form.get('role')
    u = get_user_by_id(user_id)
    if not u:
        flash('User not found', 'danger')
        return redirect(url_for('dashboard'))
    u['role'] = new_role
    flash(f"User {u['name']} role set to {new_role}", 'success')
    return redirect(url_for('dashboard'))


if __name__ == "__main__":
    app.run(debug=True)
