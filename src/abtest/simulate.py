"""Synthetic experiment data (provided).

Produces two tables shaped like real product logs:
  users(user_id, variant, signup_date, pre_minutes)
  events(user_id, event_date, event_type, minutes)
where event_type is 'session' and the experiment runs 14 days.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

START = pd.Timestamp("2026-09-01")


def simulate(
    n_users: int = 20_000,
    lift: float = 0.03,          # true relative lift in watch minutes for treatment
    retention_lift: float = 0.0,  # true absolute change in day-7 retention
    seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    user_id = np.arange(1, n_users + 1)
    variant = np.where(rng.random(n_users) < 0.5, "control", "treatment")

    # Latent engagement drives both pre-period and in-experiment minutes -> CUPED works.
    engagement = rng.lognormal(mean=3.0, sigma=0.6, size=n_users)
    pre_minutes = engagement * 14 * rng.lognormal(0, 0.25, n_users)
    users = pd.DataFrame({
        "user_id": user_id,
        "variant": variant,
        "signup_date": START - pd.to_timedelta(rng.integers(30, 400, n_users), unit="D"),
        "pre_minutes": pre_minutes.round(2),
    })

    is_t = variant == "treatment"
    p_active = np.clip(0.55 + 0.1 * np.log(engagement / 20), 0.05, 0.95)
    rows = []
    for day in range(14):
        active = rng.random(n_users) < p_active + (retention_lift if day >= 6 else 0) * is_t
        mins = engagement * rng.lognormal(0, 0.5, n_users) * np.where(is_t, 1 + lift, 1.0)
        idx = np.flatnonzero(active)
        rows.append(pd.DataFrame({
            "user_id": user_id[idx],
            "event_date": START + pd.Timedelta(days=day),
            "event_type": "session",
            "minutes": mins[idx].round(2),
        }))
    events = pd.concat(rows, ignore_index=True)
    return users, events
