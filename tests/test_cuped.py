import numpy as np
import pytest

from abtest.stats import cuped_adjust


def test_cuped_preserves_mean_and_reduces_variance():
    rng = np.random.default_rng(3)
    x = rng.normal(50, 10, 5000)
    y = 0.8 * x + rng.normal(0, 5, 5000)
    adj = cuped_adjust(y, x)
    assert adj.mean() == pytest.approx(y.mean())
    assert adj.var() < 0.3 * y.var()


def test_cuped_theta_exact():
    x = np.array([1.0, 2, 3, 4])
    y = np.array([2.0, 4, 6, 8])  # theta = 2 -> adjusted is constant
    assert np.allclose(cuped_adjust(y, x), y.mean())
