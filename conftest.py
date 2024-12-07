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
def controller(page):
    controller = Controller(page)
    yield controller
