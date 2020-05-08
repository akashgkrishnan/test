import pytest


@pytest.fixture(scope='class')
def setup():
    print('i will be executed first')
    yield
    print("i will be executed last")


@pytest.fixture(scope='class')
def dataload():
    print('your data is being loaded')
    return ['akash', 'krishnan', 'india']