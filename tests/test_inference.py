import numpy as np
import pytest
from scipy import stats

from abtest.stats import srm_pvalue, two_proportion_ztest, welch_ttest


def test_srm():
    assert srm_pvalue(5000, 5000) == pytest.approx(1.0)
    assert srm_pvalue(5000, 5300) < 0.01
    assert srm_pvalue(5000, 5300) == pytest.approx(stats.chisquare([5000, 5300]).pvalue)


def test_welch_matches_scipy():
    rng = np.random.default_rng(1)
    c, t = rng.normal(10, 2, 400), rng.normal(10.5, 3, 600)
    res = welch_ttest(c, t)
    ref = stats.ttest_ind(t, c, equal_var=False)
    assert res["diff"] == pytest.approx(t.mean() - c.mean())
    assert res["pvalue"] == pytest.approx(ref.pvalue)
    assert res["ci_low"] < res["diff"] < res["ci_high"]
    assert res["rel_lift"] == pytest.approx(res["diff"] / c.mean())


def test_two_proportion():
    res = two_proportion_ztest(x_c=400, n_c=1000, x_t=450, n_t=1000)
    assert res["diff"] == pytest.approx(0.05)
    p = 0.425
    z = 0.05 / np.sqrt(p * (1 - p) * (2 / 1000))
    assert res["pvalue"] == pytest.approx(2 * stats.norm.sf(z))
    se = np.sqrt(0.4 * 0.6 / 1000 + 0.45 * 0.55 / 1000)
    assert res["ci_high"] - res["ci_low"] == pytest.approx(2 * 1.959964 * se, rel=1e-4)
