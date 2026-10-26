import pytest

from abtest.simulate import simulate


@pytest.fixture(scope="session")
def data():
    return simulate(n_users=3_000, seed=7)
