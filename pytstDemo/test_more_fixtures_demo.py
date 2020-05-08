import pytest
'''

@pytest.mark.usefixtures('setup') this decorator is given on a class so that all the test cases/ methods defined
inside the class use fixutes
this way setup will run every time before and afte the test case
for fixtures to run just once before the execution of all tests in class and after executing 
all the test cases is to update the conftest fixture method for setup and teardown 
@pytest.fixtures(scope= class)

'''

@pytest.mark.usefixtures('setup')
class TestExample:
    def test_firstDemo(self):
        print('first demo')


    def test_secondDEmo(self):
        print('second demo')


    def test_thirdDemo(self):
        print('third demo')


    def test_fourthDemo(self):
        print('fourth demo')


@pytest.mark.usefixtures('dataload', 'setup')
class TestExample3:
    def test_dataloading(self, dataload):
        print('in class',dataload)

    def test_dataolading_Setup(self):
        print('gambles')


def test_example2(dataload):
    print('in function',dataload)