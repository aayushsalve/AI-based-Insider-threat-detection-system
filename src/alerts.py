import logging
import pandas as pd
import json
from datetime import datetime
from config import PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AlertSystem:
    def __init__(self):
        results_path = (
            PATHS["reports"] / "detailed_results_20260217_122948.csv"
        )
        self.results_df = pd.read_csv(results_path)
        self.alerts_dir = PATHS["reports"] / "alerts"
        self.alerts_dir.mkdir(exist_ok=True)

    def save_alert_to_file(self, alert_type, user_data):
        """Save alert to JSON file"""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'alert_type': alert_type,
            'severity': ('CRITICAL' if user_data['risk_score'] > 8.0
                         else 'HIGH'),
            'user_id': user_data['user_id'],
            'risk_score': float(user_data['risk_score']),
            'risk_level': user_data['risk_level'],
            'confidence': float(user_data['confidence']),
            'threat_indicators': {
                'sensitive_files_accessed': int(
                    user_data['sensitive_files_accessed']),
                'after_hours_access': int(
                    user_data['after_hours_access']),
                'failed_login_rate': float(
                    user_data['failed_login_rate']),
                'unique_locations': int(
                    user_data['unique_locations']),
                'downloads': int(user_data['downloads_count']),
                'failed_activities': int(
                    user_data['failed_activities'])
            },
            'recommended_actions': [
                'Immediately review user account activity',
                'Check for unauthorized file access',
                'Monitor network traffic from user IPs',
                'Consider temporary access suspension',
                'Escalate to Security Operations Center'
            ]
        }

        # Save individual alert
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"alert_{user_data['user_id']}_{timestamp}.json"
        alert_file = self.alerts_dir / filename
        with open(alert_file, 'w') as f:
            json.dump(alert, f, indent=2)

        logger.info(f"✅ Alert saved: {alert_file.name}")
        return alert

    def generate_incident_report(self, threats):
        """Generate consolidated incident report"""
        report = {
            'report_generated': datetime.now().isoformat(),
            'total_alerts': len(threats),
            'critical_count': len(threats[threats['risk_score'] > 8.5]),
            'threats': []
        }

        for _, threat in threats.iterrows():
            report['threats'].append({
                'rank': len(report['threats']) + 1,
                'user_id': threat['user_id'],
                'risk_score': float(threat['risk_score']),
                'confidence': float(threat['confidence'])
            })

        # Save incident report
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = self.alerts_dir / f"incident_report_{timestamp}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        logger.info(f"✅ Incident report saved: {report_file.name}")
        return report

    def monitor_and_alert(self):
        """Monitor system and generate alerts"""
        logger.info("="*60)
        logger.info("MONITORING FOR CRITICAL THREATS")
        logger.info("="*60)

        critical_threats = self.results_df[
            self.results_df['risk_level'] == 'Critical'
        ].sort_values('risk_score', ascending=False)

        logger.info(f"Found {len(critical_threats)} critical threats\n")

        # Generate individual alerts
        for _, threat in critical_threats.iterrows():
            user_id = threat['user_id']
            risk_score = threat['risk_score']
            logger.info(f"🚨 ALERT: {user_id} - Risk: {risk_score:.1f}")
            self.save_alert_to_file('CRITICAL_THREAT', threat)

        # Generate consolidated incident report
        if len(critical_threats) > 0:
            self.generate_incident_report(critical_threats)

        logger.info("\n✅ Monitoring complete.")
        logger.info(
            f"✅ {len(critical_threats)} alerts saved to: "
            f"{self.alerts_dir}"
        )
        logger.info("="*60)

        # Print alert summary
        self.print_alert_summary(critical_threats)

    def print_alert_summary(self, threats):
        """Print alert summary table"""
        logger.info("\nALERT SUMMARY")
        logger.info("-"*60)
        logger.info(f"{'User ID':<15} {'Risk Score':<15} {'Confidence':<15}")
        logger.info("-"*60)
       
        for _, threat in threats.iterrows():
            alert_line = (
                f"{threat['user_id']:<15} "
                f"{threat['risk_score']:<15.1f} "
                f"{threat['confidence']:<15.1f}%"
            )
            logger.info(alert_line)
    
        logger.info("-"*60)


if __name__ == "__main__":
    alert_system = AlertSystem()
    alert_system.monitor_and_alert()
