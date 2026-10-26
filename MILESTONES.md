# Milestones

Run `pytest tests/test_<name>.py` for each milestone until it passes, then commit.

## M1 — Generate & explore the data (≈1 evening)
- `python scripts/make_data.py` (provided). Open the parquet files in a notebook.
- Read `src/abtest/simulate.py` so you know the true effect you're trying to recover
  (in a real job you won't — that's why simulation is a great way to validate methods).

## M2 — SQL (≈2 evenings) — `sql/*.sql`
- Write the queries in `sql/` against DuckDB. Each file has the spec in comments.
- Tests: `test_sql.py`. This is your SQL interview prep — window functions, CTEs, joins.

## M3 — Design: power & sample size (≈1 evening) — `stats.py`
- `sample_size_per_arm(...)`. Tests: `test_power.py`.
- Interview question: *what happens to required N if you halve the MDE?* (4x.)

## M4 — Sanity check & inference (≈1 evening) — `stats.py`
- `srm_pvalue`, `welch_ttest`, `two_proportion_ztest`. Tests: `test_inference.py`.

## M5 — CUPED (≈1–2 evenings) — `stats.py`
- `cuped_adjust`. Tests: `test_cuped.py`. Report % variance reduction on the real data.

## M6 — Peeking simulation (≈1 evening) — `peeking.py`
- `false_positive_rate(n_peeks, ...)` on A/A tests. Plot FPR vs. number of peeks.
- Stretch: implement a fix (Bonferroni across looks, or an always-valid / mSPRT approach) and show FPR back near 5%.

## M7 — Write-up (≈1 evening)
- One-page README: decision, effect + CI, what CUPED bought you, the peeking chart.
- Stretch: rewrite the decision for a PM audience in 5 sentences.
