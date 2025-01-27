import pytest

from auxiliary.controller import Controller


@pytest.fixture(scope="function")
def user_data():
    user_data = {
        'username': 'Test username',
        'email': 'test@test.acc',
        'curr_address': 'Test curr address',
        'per_address': 'Test permanent address'
    }
    yield user_data


@pytest.fixture(scope="function")
def practice_form_user_data():
    user_data = {
        'first_name': 'Testname',
        'last_name': 'Testsurname',
        'phone': '1234567890',
        'email': 'test@test.acc',
        'birth_date': '26 Jan 2025',
        'subjects': ['Maths', 'Chemistry', 'Commerce'],
        'picture': 'test_pic.jpg',
        'address': '188300 ,Test street, 23, 67',
        'state': 'NCR',
        'city': 'Delhi'
    }
    yield user_data


@pytest.fixture(scope="function")
def controller(page):
    controller = Controller(page)
    yield controller
