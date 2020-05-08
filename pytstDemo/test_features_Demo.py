'''
fixtures are used as setup and tear down for test cases
conftest files are used so that these fixtures can be made available to all test cases

'''


def test_fixture_demo(setup):
    print("i wil execute fixtures")
    assert  10 == 20