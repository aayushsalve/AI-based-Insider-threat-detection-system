import json
from datetime import datetime
from config import PATHS
from logger import setup_logger

logger = setup_logger(__name__)


class ReportGenerator:
    """Generate comprehensive detection reports"""

    @staticmethod
    def generate_report(risk_df, summary_stats, explanations=None):
        critical_users = risk_df[risk_df["risk_level"] == "Critical"]
        high_users = risk_df[risk_df["risk_level"] == "High"]

        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": summary_stats,
            "critical_threats": critical_users[
                [
                    "user_id",
                    "risk_score",
                    "anomaly_score",
                    "supervised_score",
                    "confidence",
                ]
            ].to_dict("records"),
            "high_risk_users": high_users[
                [
                    "user_id",
                    "risk_score",
                    "anomaly_score",
                    "supervised_score",
                    "confidence",
                ]
            ].head(10).to_dict("records"),
        }

        if explanations is not None:
            report["explanations"] = explanations

        return report

    @staticmethod
    def save_report_json(report):
        PATHS["reports"].mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = PATHS["reports"] / f"threat_report_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        logger.info(f"✅ Report saved: {filename}")
        return filename

    @staticmethod
    def save_report_csv(risk_df):
        PATHS["reports"].mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = PATHS["reports"] / f"detailed_results_{timestamp}.csv"
        risk_df.to_csv(filename, index=False)
        logger.info(f"✅ CSV saved: {filename}")
        return filename

    @staticmethod
    def print_console_report(report):
        print("\n" + "=" * 70)
        print("INSIDER THREAT DETECTION - SUMMARY REPORT")
        print("=" * 70)
        print(f"Generated: {report['timestamp']}")
        summary = report["summary"]
        print(f"Total Users: {summary['total_users']} | "
              f"Critical: {summary['critical']} | High: {summary['high']}")
        print(f"Avg Risk: {summary['avg_risk_score']:.2f} | "
              f"Max: {summary['max_risk_score']:.2f}")
        print("=" * 70)
