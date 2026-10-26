from pathlib import Path

from abtest.simulate import simulate

out = Path(__file__).resolve().parents[1] / "data"
out.mkdir(exist_ok=True)
users, events = simulate()
users.to_parquet(out / "users.parquet", index=False)
events.to_parquet(out / "events.parquet", index=False)
print(f"users: {len(users):,} rows   events: {len(events):,} rows   -> {out}")
