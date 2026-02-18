import numpy as np


def explain_predictions(model, X, feature_names, top_k=5):
    """
    Returns a list of top-k feature contributions per row.
    Uses SHAP if available, otherwise falls back to feature_importances
    heuristic.
    """
    try:
        import shap
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        sv = shap_values[1] if isinstance(shap_values, list) else shap_values
        explanations = []
        for i in range(X.shape[0]):
            idx = np.argsort(np.abs(sv[i]))[::-1][:top_k]
            row_explanation = [
                (feature_names[j], float(sv[i][j])) for j in idx
            ]
            explanations.append(row_explanation)
        return explanations
    except Exception:
        importances = getattr(model, "feature_importances_", None)
        if importances is None:
            return [[] for _ in range(X.shape[0])]
        explanations = []
        for i in range(X.shape[0]):
            scores = np.abs(X[i] * importances)
            idx = np.argsort(scores)[::-1][:top_k]
            row_explanation = [
                (feature_names[j], float(scores[j])) for j in idx
            ]
            explanations.append(row_explanation)
        return explanations
