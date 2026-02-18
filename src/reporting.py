import json
from datetime import datetime


class ReportGenerator:
    """Generate comprehensive detection reports"""

    @staticmethod
    def generate_report(risk_df, summary):
        """Create detailed report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': summary,
            'critical_users': risk_df[risk_df['risk_level'] == 'Critical'][
                ['user_id', 'risk_score', 'anomaly_score', 'confidence']
            ].to_dict('records'),
            'high_risk_users': risk_df[risk_df['risk_level'] == 'High'][
                ['user_id', 'risk_score', 'anomaly_score', 'confidence']
            ].to_dict('records')[:10]  # Top 10
        }
        return report

    @staticmethod
    def save_report(report, output_dir='../reports'):
        """Save report to file"""
        import os
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{output_dir}/threat_report_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

        return filename
