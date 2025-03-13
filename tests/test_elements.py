import os
import allure
from random import choice

from auxiliary.url_path import BASE_URL
from auxiliary.constants import HTMLAttr, HTMLValue, RCode, TABLE_ROW


@allure.epic("Тесты элементов")
class TestElements:

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

    @allure.feature("Проверка скачивания и загрузки файлов")
    @allure.story("Проверяем процесс скачивания файла и процесс загрузки файлов")
    @allure.title("Тест процесса скачивания файла и процесса загрузки файлов")
    @allure.description("Производим скачивание файла, производим загрузку файла")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_download(self, controller):
        with allure.step('Открыть страницу скачивания и загрузки файла'):
            controller.upload_download_page.navigate()
        with allure.step('Нажать кнопку скачивания файла'):
            controller.upload_download_page.page.on("download", lambda download: print(download.path()))
            with controller.upload_download_page.page.expect_download() as download_info:
                controller.upload_download_page.click(controller.upload_download_page.download)
        with allure.step('Получить данные атрибутов элемента скачивания'):
            file_url = controller.upload_download_page.get_attr(controller.upload_download_page.download, HTMLAttr.HREF)
            file_name = controller.upload_download_page.get_attr(controller.upload_download_page.download, "download")
        with allure.step('Сравнить данные элемента скачивания с информацией о скачиваемом файле'):
            controller.helper.is_eq(download_info.value.url, file_url)
            controller.helper.is_eq(download_info.value.suggested_filename, file_name)
        with allure.step('Подготовка данных загрузки файла'):
            current_working_dir = os.getcwd()
            file_name = "test.txt"
            file_path = os.path.join(current_working_dir, f"uploads/{file_name}")
        with allure.step('Нажать кнопку загрузки файла'):
            controller.upload_download_page.page.set_input_files(controller.upload_download_page.upload["selector"], file_path)
        with allure.step('Проверить данные загрузки файла'):
            controller.helper.to_contain_text(controller.upload_download_page.upload_path, file_name)

    @allure.feature("Проверка динамических изменений")
    @allure.story("Проверяем изменения свойст элементов")
    @allure.title("Тест изменения свойств элементов и процесса взаимодействия с ними")
    @allure.description("Производим проверку изменений в элементах")
    @allure.severity(allure.severity_level.NORMAL)
    def test_upload_download(self, controller):
        with allure.step('Открыть страницу динамических элементов'):
            controller.dyn_properties_page.navigate()
        with allure.step('Проверка наличия элемента с рандомным id'):
            controller.helper.to_be_visible(controller.dyn_properties_page.random_id)
        with allure.step('Проверка доступности элемента спустя время'):
            controller.helper.to_be_enabled(controller.dyn_properties_page.enable_after, 6000)
        with allure.step('Проверка изменения цвета текста элемента спустя время'):
            controller.helper.to_have_css(controller.dyn_properties_page.color_change, "color", "rgb(220, 53, 69)")
        with allure.step('Проверка видимости элемента спустя время'):
            controller.helper.to_be_visible(controller.dyn_properties_page.visible_after)

    @allure.feature("Проверка функциональности таблиц")
    @allure.story("Проверяем работу с записями в таблицах")
    @allure.title("Тест удаления записи из таблицы")
    @allure.description("Производим удаление элемента из таблицы и проверяем, что запись удалена")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_row(self, controller):
        with allure.step('Открыть страницу рвботы с таблицами'):
            controller.web_table_page.navigate()
        with allure.step('Получить все записи на странице'):
            rows = controller.web_table_page.all_els(controller.web_table_page.rows)
        with allure.step('Выбрать рандомную запись и получить ее индекс'):
            random_row = choice(rows)
            index = rows.index(random_row)
        with allure.step('Нажать на кнопку удаления, соотвествующую записи'):
            dlt_selector = controller.web_table_page.delete_btn['selector']
            controller.web_table_page.page.locator(f"({dlt_selector})[{index+1}]").click()
        with allure.step('Получить все записи после удаления'):
            rows_after_deleting = controller.web_table_page.all_els(controller.web_table_page.rows)
        with allure.step('Проверить что кол-во записей уменьшилось на 1'):
            controller.helper.is_eq(len(rows) - 1, len(rows_after_deleting))

    @allure.feature("Проверка функциональности таблиц")
    @allure.story("Проверяем работу с записями в таблицах")
    @allure.title("Тест поиска данных в таблице")
    @allure.description("Производим поиск элементов в таблице и проверяем, что результат соотвествует")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search(self, controller):
        data = ["rra", "tr", "9", "a@example.com", "2000", "nce"]
        with allure.step('Открыть страницу работы с таблицами'):
            controller.web_table_page.navigate()
        for item in data:
            with allure.step(f'Ввести данные [{item}] в поисковую строку'):
                controller.web_table_page.fill(controller.web_table_page.search_input, item)
            with allure.step(f'Получить все записи на странице, соотвествующие [{item}]'):
                rows = controller.web_table_page.all_els(controller.web_table_page.rows)
            with allure.step(f'Проверить, что все записи в таблице содержат [{item}]'):
                for row in rows:
                    controller.helper.is_in(item, row.text_content())
            with allure.step(f'Очистить поисковую строку'):
                controller.web_table_page.search_input['locator'].clear()
        with allure.step(f'Проверить, что информации о пустом результате нет'):
            controller.helper.not_to_be_visible(controller.web_table_page.no_rows)
        with allure.step(f'Ввести пустую строку'):
            controller.web_table_page.fill(controller.web_table_page.search_input, "    ")
        with allure.step(f'Проверить, что информация о пустом результате есть'):
            controller.helper.to_be_visible(controller.web_table_page.no_rows)

    @allure.feature("Проверка функциональности таблиц")
    @allure.story("Проверяем работу с записями в таблицах")
    @allure.title("Тест редактирования данных в таблице")
    @allure.description("Выбираем элемент в таблице и редактируем его")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit(self, controller):
        with allure.step('Открыть страницу работы с таблицами'):
            controller.web_table_page.navigate()
        with allure.step('Получить все записи на странице'):
            rows = controller.web_table_page.all_els(controller.web_table_page.rows)
        with allure.step('Выбрать рандомную запись и получить ее индекс'):
            random_row = choice(rows)
            index = rows.index(random_row)
        with allure.step('Получить текст выбранной записи'):
            chosen_row_text = random_row.text_content()
        with allure.step('Нажать на кнопку редактирования, соотвествующую записи'):
            edit_selector = controller.web_table_page.edit_btn['selector']
            controller.web_table_page.page.locator(f"({edit_selector})[{index+1}]").click()
        with allure.step('Проверить, что элементы формы редактирования отображаются'):
            controller.web_table_page.form_els_visibility()
        with allure.step('Нажать на кнопку закрытия формы редактирования'):
            controller.web_table_page.click(controller.web_table_page.close_btn)
        with allure.step('Проверить, что элементы формы редактирования не отображаются'):
            controller.web_table_page.form_els_not_visibility()
        with allure.step('Повторно нажать на кнопку редактирования, соотвествующую записи'):
            controller.web_table_page.page.locator(f"({edit_selector})[{index + 1}]").click()
        with allure.step('Проверить, что окно содержит данные выбранной записи'):
            first_name_text = controller.web_table_page.get_element_text(controller.web_table_page.first_name)
            last_name_text = controller.web_table_page.get_element_text(controller.web_table_page.last_name)
            age_text = controller.web_table_page.get_element_text(controller.web_table_page.age)
            email_text = controller.web_table_page.get_element_text(controller.web_table_page.email)
            salary_text = controller.web_table_page.get_element_text(controller.web_table_page.salary)
            department = controller.web_table_page.get_element_text(controller.web_table_page.department)
            controller.helper.is_in(first_name_text, chosen_row_text)
            controller.helper.is_in(last_name_text, chosen_row_text)
            controller.helper.is_in(age_text, chosen_row_text)
            controller.helper.is_in(email_text, chosen_row_text)
            controller.helper.is_in(salary_text, chosen_row_text)
            controller.helper.is_in(department, chosen_row_text)
        with allure.step('Ввести новые данные'):
            controller.web_table_page.fill_data_in_form()
        with allure.step('Нажать на закрытие формы, не сохранив данные'):
            controller.web_table_page.click(controller.web_table_page.close_btn)
        with allure.step('Проверить, что данные не сохранились'):
            row_selector = controller.web_table_page.rows['selector']
            cur_chosen_row_text = controller.web_table_page.page.locator(f"({row_selector})[{index+1}]").text_content()
            for item in TABLE_ROW:
                controller.helper.is_not_in(item, cur_chosen_row_text)
        with allure.step('Повторно нажать на кнопку редактирования, соотвествующую записи'):
            controller.web_table_page.page.locator(f"({edit_selector})[{index + 1}]").click()
        with allure.step('Повторно ввести новые данные'):
            controller.web_table_page.fill_data_in_form()
        with allure.step('Сохранить данные'):
            controller.web_table_page.click(controller.web_table_page.submit)
        with allure.step('Проверить, что данные сохранены'):
            cur_chosen_row_text = controller.web_table_page.page.locator(f"({row_selector})[{index+1}]").text_content()
            for item in TABLE_ROW:
                controller.helper.is_in(item, cur_chosen_row_text)

    @allure.feature("Проверка функциональности таблиц")
    @allure.story("Проверяем работу с записями в таблицах")
    @allure.title("Тест добавления данных в таблице")
    @allure.description("Добавление нового элемента в таблицу")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add(self, controller):
        with allure.step('Открыть страницу работы с таблицами'):
            controller.web_table_page.navigate()
        with allure.step('Получить все записи на странице'):
            rows = controller.web_table_page.all_els(controller.web_table_page.rows)
        with allure.step('Сохранить текущее кол-во записей'):
            rows_amount = len(rows)
        with allure.step('Проверить, что элементы формы редактирования не отображаются'):
            controller.web_table_page.form_els_not_visibility()
        with allure.step('Нажать кнопку "Add"'):
            controller.web_table_page.click(controller.web_table_page.add_btn)
        with allure.step('Проверить, что элементы формы редактирования отображаются'):
            controller.web_table_page.form_els_visibility()
        with allure.step('Ввести новые данные'):
            controller.web_table_page.fill_data_in_form()
        # with allure.step('Нажать на закрытие формы, не сохранив данные'):
        #     controller.web_table_page.click(controller.web_table_page.close_btn)
        # with allure.step('Проверить, что данные не сохранились'):
        #     curr_rows = controller.web_table_page.all_els(controller.web_table_page.rows)
        #     controller.helper.is_eq(rows_amount, len(curr_rows))
        #     for row in curr_rows:
        #         for item in TABLE_ROW:
        #             controller.helper.is_not_in(item, row.text_content())
        # with allure.step('Повторно нажать на кнопку "Add"'):
        #     controller.web_table_page.click(controller.web_table_page.add_btn)
        # with allure.step('Ввести новые данные'):
        #     controller.web_table_page.fill_data_in_form()
        with allure.step('Сохранить данные'):
            controller.web_table_page.click(controller.web_table_page.submit)
        with allure.step('Проверить, что данные сохранились'):
            curr_rows = controller.web_table_page.all_els(controller.web_table_page.rows)
            print(len(curr_rows))
            controller.helper.is_eq(rows_amount + 1, len(curr_rows))
            for item in TABLE_ROW:
                controller.helper.is_in(item, curr_rows[-1].text_content())
