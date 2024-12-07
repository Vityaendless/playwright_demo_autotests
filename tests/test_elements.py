import time
import pytest


class TestElements:

    def test_textbox(self, controller, user_data):
        username = user_data['username']
        email = user_data['email']
        curr_address = user_data['curr_address']
        per_address = user_data['per_address']
        controller.textbox_page.navigate()
        controller.helper.not_to_be_visible(controller.textbox_page.output)
        controller.textbox_page.fill(controller.textbox_page.username, username)
        controller.textbox_page.fill(controller.textbox_page.email, email)
        controller.textbox_page.fill(controller.textbox_page.c_address, curr_address)
        controller.textbox_page.fill(controller.textbox_page.p_address, per_address)
        controller.textbox_page.click(controller.textbox_page.submit)
        controller.helper.to_be_visible(controller.textbox_page.output)
        controller.helper.to_contain_text(controller.textbox_page.output_name, username)
        controller.helper.to_contain_text(controller.textbox_page.output_email, email)
        controller.helper.to_contain_text(controller.textbox_page.output_c_address, curr_address)
        controller.helper.to_contain_text(controller.textbox_page.output_p_address, per_address)
