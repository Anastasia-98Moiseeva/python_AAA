from one_hot_encoder import fit_transform
import pytest


def test_with_assert_equal():
    actual = fit_transform('dark', 'light')

    expected = [('dark', [0, 1]), ('light', [1, 0])]
    assert actual == expected


def test_with_asset_not_in():
    actual = fit_transform('dark', 'light')

    for item in actual:
        assert 2 not in item[1]


def test_with_assert_true():
    actual = fit_transform('dark', 'light')

    for item in actual:
        for i in item[1]:
            assert i < 2


def test_with_assert_raises():
    with pytest.raises(TypeError):
        actual = fit_transform()