import pytest
import requests
from faker import Faker

from auxiliary.controller import Controller
from auxiliary.constants import COLORS, TOOL_TIPS_TEXTS, DRAG_N_DROP_INFO, VisibilityState, TEST_USER


@pytest.fixture(scope="function")
def colors_data():
    yield COLORS


@pytest.fixture(scope="function")
def tool_tips_data():
    yield TOOL_TIPS_TEXTS


@pytest.fixture(scope="function")
def visibility_data():
    yield VisibilityState

@pytest.fixture(scope="function")
def drag_n_drop_info():
    yield DRAG_N_DROP_INFO

@pytest.fixture(scope="function")
def test_user():
    yield TEST_USER

@pytest.fixture(scope="function")
def auth(page, test_user):
    auth = Controller(page)
    auth.login_page.navigate()
    auth.login_page.fill(auth.login_page.username, test_user['username'])
    auth.login_page.fill(auth.login_page.password, test_user['password'])
    auth.login_page.click(auth.login_page.login_btn)
    yield auth

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
def fake_user():
    fake = Faker()
    user = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'username': fake.user_name(),
        'password': 'Qwerty123!'
    }
    yield user


@pytest.fixture(scope="function")
def modal_dialogs_information():
    small_modal_dialog = {
        "heading": "Small Modal",
        "text": "This is a small modal. It has very less content"
    }
    large_modal_dialog = {
        "heading": "Large Modal",
        "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
                "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type "
                "and scrambled it to make a type specimen book. It has survived not only five centuries, but also the "
                "leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s "
                "with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop "
                "publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }
    modals_data = (small_modal_dialog, large_modal_dialog)
    yield modals_data


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


@pytest.fixture(scope="function")
def restore_user_api():
    url_new_user = 'https://demoqa.com/Account/v1/User'
    body = {"userName": "testqwerty", "password": "Qwerty123!"}
    response = requests.post(url_new_user, data=body)
    print(response.status_code)
    print(response.json())
    yield response
