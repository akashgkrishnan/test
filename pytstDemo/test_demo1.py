#file name for pytest should start / end with test_
# function names should also start with test_
# any code written inside method
# every method is called a new test cases
#dont use same method names in diff filles for same test
#run from cmd py.test -v -s, pytest, py.test
# py.test test_rest_of_file_name -v -s
# - v stands for verbose
# -s for logs in output
# -k find the string mentioned after it in all the files of the pytest folder.
#test case name in pytest should be meaningful name and this name would be called as testcase
# py.test -k "string" -v -s "this shoould be used to match test case names in multiple files and runthem
# for smoketest cases in pytest there is a decorator called mark  this will run the test cases that are m
# marked in a group
# decorator  pytest.mark.mark_name :- py.test -m mark_name -v -s
# -m flag is used to understand -m
#@pytest.mark.skip -> for skipping a test case
#@pytest.mark.xfail -> the test will run but the report wont be generated



import  pytest

@pytest.mark.smoke
def test_hello_credit(setup):
    print('hello')

@pytest.mark.skip
def test_ccasetwo(setup):
    print("hi")