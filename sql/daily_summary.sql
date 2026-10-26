-- M2b — one row per (variant, event_date). Used for the "results by day" chart
-- that tempts people to peek (see M6).
--
-- Output columns (exact names), ordered by variant, event_date:
--   variant, event_date,
--   active_users        -- distinct users with a session that day
--   total_minutes       -- sum of minutes that day
--   cumulative_minutes  -- running total of total_minutes within the variant (window function)
--
-- Hints: JOIN events to users for variant; GROUP BY; SUM(...) OVER (PARTITION BY ... ORDER BY ...).

SELECT 'TODO: write daily_summary.sql' AS todo;
