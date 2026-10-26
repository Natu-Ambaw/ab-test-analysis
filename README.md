# A/B Test Analysis: Power, CUPED, and the Peeking Problem

An end-to-end analysis of an online experiment — from SQL extraction to a
ship/no-ship recommendation — built with the methods product data science
teams actually use.

> **Status:** work in progress — see [`MILESTONES.md`](MILESTONES.md).

## Scenario

A short-video app tests a new feed-ranking model. Primary metric:
**watch minutes per user** over 14 days. Guardrail: **day-7 retention**.

## What this project shows

1. **SQL** — building the per-user analysis table from raw event logs (DuckDB).
2. **Experiment design** — sample size for a target minimum detectable effect (MDE).
3. **Sanity checks** — sample ratio mismatch (SRM) test before looking at results.
4. **Inference** — Welch's t-test and a two-proportion z-test with confidence intervals.
5. **Variance reduction** — CUPED using pre-experiment behavior; how much smaller the CIs get.
6. **Peeking** — simulation showing how checking daily inflates false positives.

## Results

_TODO: effect size + CI with and without CUPED, SRM result, guardrail result, recommendation._

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python scripts/make_data.py   # writes data/events.parquet + data/users.parquet
pytest
```
