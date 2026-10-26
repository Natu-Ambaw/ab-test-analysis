"""M6 — why you shouldn't check results every day. YOU implement this."""
from __future__ import annotations

import numpy as np


def false_positive_rate(
    n_peeks: int,
    n_per_arm: int = 2_000,
    n_sims: int = 2_000,
    alpha: float = 0.05,
    seed: int = 0,
) -> float:
    """Simulate A/A tests (no true effect) and stop at the FIRST significant peek.

    For each simulation:
      - draw n_per_arm standard-normal values for control and treatment
      - look at `n_peeks` evenly spaced checkpoints (the last one = all data);
        e.g. n_peeks=4 -> look after 25%, 50%, 75%, 100% of users
      - at each look, run a two-sided z-test on the data so far (known sd = 1)
      - count the sim as a false positive if ANY look has p < alpha
    Return the fraction of sims that were false positives.

    With n_peeks=1 this should be ≈ alpha. With n_peeks=10 it's much higher.
    Hint: vectorize with np.cumsum instead of looping over users.
    """
    raise NotImplementedError("M6")
