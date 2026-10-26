"""M3–M5 — experiment statistics. YOU implement these.

Use numpy and scipy.stats (norm, t, chi2). Don't call scipy.stats.ttest_ind
for welch_ttest — derive it yourself, then check against scipy in a notebook.
"""
from __future__ import annotations

import numpy as np


# ---------- M3: design ----------
def sample_size_per_arm(
    baseline_mean: float,
    baseline_sd: float,
    mde_rel: float,
    alpha: float = 0.05,
    power: float = 0.80,
) -> int:
    """Users needed PER ARM to detect a relative lift `mde_rel` (e.g. 0.02 = 2%).

        delta = mde_rel * baseline_mean
        n = 2 * (z_{1-alpha/2} + z_{power})^2 * sd^2 / delta^2

    Round UP to an int.
    """
    raise NotImplementedError("M3")


# ---------- M4: sanity check + inference ----------
def srm_pvalue(n_control: int, n_treatment: int, expected_share: float = 0.5) -> float:
    """Chi-square goodness-of-fit p-value for sample ratio mismatch (1 dof).

    If p < 0.001, stop: the randomization or logging is broken.
    """
    raise NotImplementedError("M4")


def welch_ttest(control: np.ndarray, treatment: np.ndarray, alpha: float = 0.05) -> dict:
    """Difference in means (treatment - control) with Welch's t-test.

    Return dict with keys: diff, se, ci_low, ci_high, pvalue, rel_lift
      se  = sqrt(s_t^2/n_t + s_c^2/n_c)  (sample variances, ddof=1)
      dof = Welch–Satterthwaite
      CI  = diff ± t_{1-alpha/2, dof} * se ; pvalue two-sided
      rel_lift = diff / mean(control)
    """
    raise NotImplementedError("M4")


def two_proportion_ztest(x_c: int, n_c: int, x_t: int, n_t: int, alpha: float = 0.05) -> dict:
    """Difference in proportions p_t - p_c.

    Return dict with keys: diff, ci_low, ci_high, pvalue
      Test statistic uses the POOLED proportion under H0.
      CI uses the UNPOOLED standard error.
    (Why the difference? Be ready to explain it.)
    """
    raise NotImplementedError("M4")


# ---------- M5: CUPED ----------
def cuped_adjust(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    """CUPED-adjusted metric: y_adj = y - theta * (x - mean(x)), theta = cov(x, y) / var(x).

    Compute theta on ALL users pooled (both arms). x is a pre-experiment
    covariate, so it's independent of treatment — that's why this is unbiased.
    Use ddof=1 consistently for cov and var.
    """
    raise NotImplementedError("M5")
