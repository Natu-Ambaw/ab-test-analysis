from abtest.stats import sample_size_per_arm


def test_textbook_case():
    # sd/delta = 10/1, (1.95996+0.84162)^2*2*100 = 1569.8 -> 1570
    assert sample_size_per_arm(100, 10, 0.01) == 1570


def test_halving_mde_quadruples_n():
    n1 = sample_size_per_arm(50, 20, 0.04)
    n2 = sample_size_per_arm(50, 20, 0.02)
    assert abs(n2 / n1 - 4) < 0.01


def test_returns_int():
    assert isinstance(sample_size_per_arm(10, 3, 0.05), int)
