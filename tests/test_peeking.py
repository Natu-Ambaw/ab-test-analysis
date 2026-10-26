from abtest.peeking import false_positive_rate


def test_single_look_is_about_alpha():
    assert 0.03 < false_positive_rate(n_peeks=1, n_sims=3000) < 0.07


def test_peeking_inflates_fpr():
    assert false_positive_rate(n_peeks=10, n_sims=3000) > 0.12
