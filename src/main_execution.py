import numpy as np
from sklearn.model_selection import train_test_split

from logger import setup_logger
from data_pipeline import DataPipeline
from model_trainer import HybridModelTrainer
from risk_scorer import RiskScorer
from reporter import ReportGenerator
from explainability import explain_predictions

logger = setup_logger(__name__)


def main():
    """Execute complete threat detection pipeline"""

    logger.info("\n" + "=" * 70)
    logger.info("🚀 INSIDER THREAT DETECTION SYSTEM - PIPELINE START")
    logger.info("=" * 70)

    # ==================== STEP 1: DATA LOADING ====================
    logger.info("\n[STEP 1/5] Loading and Processing Data...")
    pipeline = DataPipeline()
    pipeline_result = pipeline.run()

    if pipeline_result is None:
        logger.error(
            "❌ Data pipeline failed. Check data files in /data directory"
        )
        return

    features_raw = pipeline_result["features_raw"]
    X_scaled = pipeline_result["features_scaled"]

    # ==================== STEP 2: TRAIN/TEST SPLIT ====================
    logger.info("\n[STEP 2/5] Splitting Data...")
    labels_df = pipeline_result["raw_data"].get("threat_labels")
    if labels_df is not None and "is_threat" in labels_df.columns:
        y = labels_df["is_threat"].values
        pos = int((y == 1).sum())
        neg = int((y == 0).sum())
        logger.info(f"Label check: positives={pos}, negatives={neg}")
        if pos < 10:
            logger.warning(
                "⚠️ Very few positive labels; "
                "supervised model may not learn well."
            )
    else:
        logger.warning("⚠️ No labels found, using random labels for demo.")
        y = np.random.randint(0, 2, len(X_scaled))

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y if len(set(y)) > 1 else None,
    )

    logger.info(f"   Train set: {len(X_train)} samples")
    logger.info(f"   Test set: {len(X_test)} samples")

    # ==================== STEP 3: MODEL TRAINING ====================
    logger.info("\n[STEP 3/5] Training Models...")
    trainer = HybridModelTrainer()
    trainer.run(X_train, X_test, y_train, y_test)

    # ==================== STEP 4: RISK SCORING ====================
    logger.info("\n[STEP 4/5] Scoring Risk...")
    iso_scores = trainer.iso_forest.score_samples(X_scaled)
    svm_scores = trainer.oc_svm.score_samples(X_scaled)
    rf_probs = trainer.get_supervised_probs(X_scaled)

    scorer = RiskScorer()
    anomaly_scores = scorer.compute_hybrid_anomaly_score(
        iso_scores, svm_scores
    )
    risk_df = scorer.compute_risk_scores(
        features_raw, anomaly_scores, supervised_probs=rf_probs
    )
    summary = scorer.get_summary_stats(risk_df)

    # ==================== STEP 5: EXPLAINABILITY ====================
    logger.info("\n[STEP 5/5] Explainability + Reporting...")
    explanations = explain_predictions(
        trainer.random_forest,
        X_scaled,
        pipeline_result["feature_columns"],
        top_k=5
    )

    # ==================== STEP 6: REPORTING ====================
    report = ReportGenerator.generate_report(
        risk_df, summary, explanations=explanations
    )
    ReportGenerator.save_report_json(report)
    ReportGenerator.save_report_csv(risk_df)
    ReportGenerator.print_console_report(report)

    logger.info("\n" + "=" * 70)
    logger.info("✅ PIPELINE EXECUTION COMPLETE")
    logger.info("=" * 70)

    return risk_df, report


if __name__ == "__main__":
    risk_df, report = main()
