import numpy as np


def population_stability_index(expected, actual, bins=10, eps=1e-6):
    expected = np.asarray(expected, dtype=float)
    actual = np.asarray(actual, dtype=float)

    # clip to finite
    expected = expected[np.isfinite(expected)]
    actual = actual[np.isfinite(actual)]

    if len(expected) == 0 or len(actual) == 0:
        return 0.0

    quantiles = np.linspace(0, 1, bins + 1)
    cuts = np.quantile(expected, quantiles)
    cuts = np.unique(cuts)

    if len(cuts) < 2:
        return 0.0

    exp_counts, _ = np.histogram(expected, bins=cuts)
    act_counts, _ = np.histogram(actual, bins=cuts)

    exp_pct = exp_counts / max(1, exp_counts.sum())
    act_pct = act_counts / max(1, act_counts.sum())

    exp_pct = np.clip(exp_pct, eps, 1)
    act_pct = np.clip(act_pct, eps, 1)

    psi = np.sum((act_pct - exp_pct) * np.log(act_pct / exp_pct))
    return float(psi)
