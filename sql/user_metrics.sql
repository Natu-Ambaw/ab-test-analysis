-- M2a — one row per user: the analysis table for the whole project.
--
-- Tables:
--   users(user_id, variant, signup_date, pre_minutes)
--   events(user_id, event_date, event_type, minutes)   -- experiment runs 2026-09-01 .. 2026-09-14
--
-- Output columns (exact names), ordered by user_id:
--   user_id, variant, pre_minutes,
--   total_minutes  -- sum of minutes over the experiment; 0 (not NULL) for users with no events
--   active_days    -- number of distinct event_dates; 0 for no events
--   retained_d7    -- 1 if the user had any session on or after 2026-09-07, else 0
--
-- Hints: LEFT JOIN users -> aggregated events (a CTE), COALESCE, CASE WHEN / MAX.
-- Watch out: joining raw events before aggregating is fine here, but think about
-- why it would double count if you joined two event tables.

SELECT 'TODO: write user_metrics.sql' AS todo;
