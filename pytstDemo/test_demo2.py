import pytest


@pytest.mark.smoke
def test_assert():
    msg = 'hellp'
    assert msg == 'hellp', "the strings dont match"


def test_assertnew_credit():
    msg = 'hellp'
    assert msg == 'hellp', "the strings dont match"