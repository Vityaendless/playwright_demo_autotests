import pytest
import allure

from auxiliary.url_path import BASE_URL
from auxiliary.constants import HTMLAttr, HTMLValue, RCode


@allure.epic("Тесты элементов")
class TestElements:

    @pytest.mark.skip
    @allure.feature("Форма отправки данных юзера")
    @allure.story("Авторизация")
    @allure.title("Тест заполнения текстовой формы")
    @allure.description("Ввод данных в форму и проверка сохранения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_textbox(self, controller, user_data):
        username = user_data['username']
        email = user_data['email']
        curr_address = user_data['curr_address']
        per_address = user_data['per_address']
        with allure.step('Открыть страницу формы'):
            controller.textbox_page.navigate()
        with allure.step('Проверить отсуствие элемента вывода данных'):
            controller.helper.not_to_be_visible(controller.textbox_page.output)
        with allure.step('Ввести данные в форму'):
            controller.textbox_page.fill(controller.textbox_page.username, username)
            controller.textbox_page.fill(controller.textbox_page.email, email)
            controller.textbox_page.fill(controller.textbox_page.c_address, curr_address)
            controller.textbox_page.fill(controller.textbox_page.p_address, per_address)
        with allure.step('Нажать кнопку "Submit"'):
            controller.textbox_page.click(controller.textbox_page.submit)
        with allure.step('Проверить наличие элемента вывода данных'):
            controller.helper.to_be_visible(controller.textbox_page.output)
        with allure.step('Проверить, что элемент вывода данных содержит информацию, введенную в форму'):
            controller.helper.to_contain_text(controller.textbox_page.output_name, username)
            controller.helper.to_contain_text(controller.textbox_page.output_email, email)
            controller.helper.to_contain_text(controller.textbox_page.output_c_address, curr_address)
            controller.helper.to_contain_text(controller.textbox_page.output_p_address, per_address)

    @pytest.mark.skip
    @allure.feature("Раскрывающийся список")
    @allure.story("Иеархия элементов")
    @allure.title("Тест выбора элементов в иеархии")
    @allure.description("Выбор элементов и иеархии и проверка этого выбора")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkbox(self, controller):
        els_lst = []
        with allure.step('Открыть страницу элементов иеархии'):
            controller.checkbox_page.navigate()
        with allure.step('Проверить отсуствие элемента результата'):
            controller.helper.not_to_be_visible(controller.checkbox_page.result)
        with allure.step('Раскрыть иеархию'):
            controller.checkbox_page.click(controller.checkbox_page.expand_all)
        with allure.step('Нажать кнопку "Home"'):
            controller.checkbox_page.click(controller.checkbox_page.home)
        with allure.step('Проверить наличие элемента результата'):
            controller.helper.to_be_visible(controller.checkbox_page.result)
        all_els = controller.checkbox_page.all_els(controller.checkbox_page.els)
        with allure.step('Получить названия всех элементов иеархии'):
            for el in all_els:
                els_lst.append(el.text_content().lower().split(".")[0].replace(' file', 'File'))
        with allure.step('Скрыть иеархию'):
            controller.checkbox_page.click(controller.checkbox_page.collapse_all)
        with allure.step('Проверить, что все элементы отобразились в строке результата'):
            for title in els_lst:
                controller.helper.to_contain_text(controller.checkbox_page.result, title)
        with allure.step('Повторно нажать кнопку "Home"'):
            controller.checkbox_page.click(controller.checkbox_page.home)
        with allure.step('Повторно проверить отсуствие элемента результата'):
            controller.helper.not_to_be_visible(controller.checkbox_page.result)

    @pytest.mark.skip
    @allure.feature("Выбор ответа через radio btns")
    @allure.story("Выбор ответа")
    @allure.title("Тест выбора ответа")
    @allure.description("Выбор ответа и проверка этого выбора")
    @allure.severity(allure.severity_level.NORMAL)
    def test_radio_btn(self, controller):
        with allure.step('Открыть страницу выбора на основе radio btns'):
            controller.radio_btn_page.navigate()
        with allure.step('Проверить отсуствие элемента результата'):
            controller.helper.not_to_be_visible(controller.radio_btn_page.result)
        with allure.step('Проверить стартовое отображение элементов'):
            controller.helper.to_be_disabled(controller.radio_btn_page.no_radio)
            controller.helper.not_to_be_disabled(controller.radio_btn_page.yes_radio)
            controller.helper.not_to_be_disabled(controller.radio_btn_page.impressive_radio)
        with allure.step('Выбрать первый ответ "YES"'):
            controller.radio_btn_page.check(controller.radio_btn_page.yes)
        with allure.step('Проверить, что в результате ответ "YES"'):
            controller.helper.to_have_text(
                controller.radio_btn_page.result, controller.radio_btn_page.yes['title'].capitalize()
            )
        with allure.step('Выбрать первый ответ "IMPRESSIVE"'):
            controller.radio_btn_page.check(controller.radio_btn_page.impressive)
        with allure.step('Проверить, что в результате ответ "IMPRESSIVE"'):
            controller.helper.to_have_text(
                controller.radio_btn_page.result, controller.radio_btn_page.impressive['title'].capitalize()
            )

    @pytest.mark.skip
    @allure.feature("Проверка кликабельности")
    @allure.story("Производим различные клики мыши")
    @allure.title("Тест различных кликов по элементам")
    @allure.description("Производим клик по элементу и проверяем результат в зависимости от типа клика")
    @allure.severity(allure.severity_level.MINOR)
    def test_buttons(self, controller):
        with allure.step('Открыть страницу кликов по кнопкам'):
            controller.btn_page.navigate()
        with allure.step('Проверить кликабельность элемента dbl клика'):
            controller.helper.not_to_be_visible(controller.btn_page.dbl_click_result)
            controller.btn_page.click(controller.btn_page.dbl_click_el)
            controller.helper.not_to_be_visible(controller.btn_page.dbl_click_result)
            controller.btn_page.dblclick(controller.btn_page.dbl_click_el)
            controller.helper.to_be_visible(controller.btn_page.dbl_click_result)
        with allure.step('Проверить кликабельность элемента right клика'):
            controller.helper.not_to_be_visible(controller.btn_page.right_click_result)
            controller.btn_page.click(controller.btn_page.right_click_el)
            controller.helper.not_to_be_visible(controller.btn_page.right_click_result)
            controller.btn_page.click(controller.btn_page.right_click_el, button="right")
            controller.helper.to_be_visible(controller.btn_page.right_click_result)
        with allure.step('Проверить кликабельность элемента клика'):
            controller.helper.not_to_be_visible(controller.btn_page.click_result)
            controller.btn_page.click(controller.btn_page.click_el, button="right")
            controller.helper.not_to_be_visible(controller.btn_page.click_result)
            controller.btn_page.click(controller.btn_page.click_el)
            controller.helper.to_be_visible(controller.btn_page.click_result)

    @pytest.mark.skip
    @allure.feature("Проверка работы ссылок")
    @allure.story("Проверяем ответы и переходы по ссылкам")
    @allure.title("Тест различных ответов и переходов по ссылкам")
    @allure.description("Производим клик ссылке и проверяем переход по ней или возврат нужного ответа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_links(self, controller):
        with allure.step('Открыть страницу проверки ссылок'):
            controller.links_page.navigate()
        with allure.step('Проверить параметры ссылки "HOME"'):
            controller.helper.to_have_attribute(controller.links_page.home, HTMLAttr.TARGET, HTMLValue.BLANK)
            controller.helper.to_have_attribute(controller.links_page.home, HTMLAttr.HREF, BASE_URL[:-1])
            tab1 = controller.links_page.get_new_tab(controller.links_page.home)
            controller.helper.to_have_url(tab1, BASE_URL)
        with allure.step('Закрыть открытую вкладку'):
            tab1.close()
        with allure.step('Проверить параметры динамической ссылки "HOME"'):
            controller.helper.to_have_attribute(controller.links_page.dyn_home, HTMLAttr.TARGET, HTMLValue.BLANK)
            controller.helper.to_have_attribute(controller.links_page.dyn_home, HTMLAttr.HREF, BASE_URL[:-1])
            tab2 = controller.links_page.get_new_tab(controller.links_page.dyn_home)
            controller.helper.to_have_url(tab2, BASE_URL)
        with allure.step('Повторно закрыть открытую вкладку'):
            tab2.close()
        with allure.step(f'Нажать кнопку "Created"'):
            controller.links_page.click(controller.links_page.created)
        with allure.step('Проверить корректность нажатия на кнопку "Created"'):
            controller.links_page.resp_check(controller.links_page.created)
        print(controller.links_page.no_content['selector'])
        with allure.step(f'Нажать кнопку "No content"'):
            controller.links_page.click(controller.links_page.no_content)
        with allure.step('Проверить корректность нажатия на кнопку "No content"'):
            controller.links_page.resp_check(controller.links_page.no_content)
        with allure.step(f'Нажать кнопку "Moved"'):
            controller.links_page.click(controller.links_page.moved)
        with allure.step('Проверить корректность нажатия на кнопку "Moved"'):
            controller.links_page.resp_check(controller.links_page.moved)
        with allure.step(f'Нажать кнопку "Bad Request"'):
            controller.links_page.click(controller.links_page.bad_request)
        with allure.step('Проверить корректность нажатия на кнопку "Bad Request"'):
            controller.links_page.resp_check(controller.links_page.bad_request)
        with allure.step(f'Нажать кнопку "Unauthorized"'):
            controller.links_page.click(controller.links_page.unauthorized)
        with allure.step('Проверить корректность нажатия на кнопку "Unauthorized"'):
            controller.links_page.resp_check(controller.links_page.unauthorized)
        with allure.step(f'Нажать кнопку "Forbidden"'):
            controller.links_page.click(controller.links_page.forbidden)
        with allure.step('Проверить корректность нажатия на кнопку "Forbidden"'):
            controller.links_page.resp_check(controller.links_page.forbidden)
        with allure.step(f'Нажать кнопку "Not Found"'):
            controller.links_page.click(controller.links_page.invalid_url)
        with allure.step('Проверить корректность нажатия на кнопку "Not Found"'):
            controller.links_page.resp_check(controller.links_page.invalid_url)

    @allure.feature("Проверка корректности ссылок и изображений")
    @allure.story("Проверяем коды ответа ссылок и изображений")
    @allure.title("Тест неверных кодов ответа для изображений и ссылок")
    @allure.description("Считывем ссылку из параметров изображения или ссылки и проверяем ее доступность")
    @allure.severity(allure.severity_level.MINOR)
    def test_broken_img_links(self, controller):
        with allure.step('Открыть страницу неверных изображений и ссылок'):
            controller.broken_obj_page.navigate()
        with allure.step('Получить значение src валидного изображения'):
            valid_img_src = controller.broken_obj_page.get_attr(controller.broken_obj_page.valid_img, HTMLAttr.SRC)
        with allure.step('Проверить код ответа src для валидного изображения'):
            controller.broken_obj_page.check_resp_code(BASE_URL[:-1] + valid_img_src, RCode.OK.code)
        with allure.step('Получить значение src НЕ валидного изображения'):
            broken_img_src = controller.broken_obj_page.get_attr(controller.broken_obj_page.broken_img, HTMLAttr.SRC)
        with allure.step('Проверить код ответа src для НЕ валидного изображения'):
            controller.broken_obj_page.check_resp_code(BASE_URL[:-1] + broken_img_src, RCode.OK.code)
        with allure.step('Получить значение href валидной ссылки'):
            valid_link_href = controller.broken_obj_page.get_attr(controller.broken_obj_page.valid_link, HTMLAttr.HREF)
        with allure.step('Проверить код ответа href для валидной ссылки'):
            controller.broken_obj_page.check_resp_code(valid_link_href, RCode.OK.code)
        with allure.step('Получить значение href НЕ валидной ссылки'):
            broken_link_href = controller.broken_obj_page.get_attr(
                controller.broken_obj_page.broken_link, HTMLAttr.HREF
            )
        with allure.step('Проверить код ответа href для НЕ валидной ссылки'):
            controller.broken_obj_page.check_resp_code(broken_link_href, RCode.INTERNAL_SERVER_ERR.code)
