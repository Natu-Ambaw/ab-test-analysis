"""Checks your SQL against an independent pandas computation."""
import numpy as np
import pandas as pd

from abtest.sql import run_sql


def test_user_metrics(data):
    users, events = data
    got = run_sql("user_metrics", users, events)
    assert list(got.columns) == ["user_id", "variant", "pre_minutes", "total_minutes",
                                 "active_days", "retained_d7"]
    assert len(got) == len(users), "one row per user, including users with no events"

    g = events.groupby("user_id")
    exp = users[["user_id"]].copy()
    exp["total_minutes"] = exp.user_id.map(g.minutes.sum()).fillna(0)
    exp["active_days"] = exp.user_id.map(g.event_date.nunique()).fillna(0)
    late = events[events.event_date >= "2026-09-07"].user_id.unique()
    exp["retained_d7"] = exp.user_id.isin(late).astype(int)

    got = got.sort_values("user_id").reset_index(drop=True)
    assert got.user_id.tolist() == exp.user_id.tolist()
    assert np.allclose(got.total_minutes, exp.total_minutes)
    assert (got.active_days.astype(int) == exp.active_days.astype(int)).all()
    assert (got.retained_d7.astype(int) == exp.retained_d7).all()


def test_daily_summary(data):
    users, events = data
    got = run_sql("daily_summary", users, events)
    assert list(got.columns) == ["variant", "event_date", "active_users", "total_minutes",
                                 "cumulative_minutes"]
    m = events.merge(users[["user_id", "variant"]], on="user_id")
    exp = (m.groupby(["variant", "event_date"])
             .agg(active_users=("user_id", "nunique"), total_minutes=("minutes", "sum"))
             .reset_index().sort_values(["variant", "event_date"]))
    exp["cumulative_minutes"] = exp.groupby("variant").total_minutes.cumsum()
    assert len(got) == len(exp) == 28
    assert got.variant.tolist() == exp.variant.tolist()
    assert (pd.to_datetime(got.event_date).values == exp.event_date.values).all()
    assert (got.active_users.values == exp.active_users.values).all()
    assert np.allclose(got.cumulative_minutes, exp.cumulative_minutes)
