from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import PracticeFormPageLocator as PracticeFormPL


class PracticeFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().practice_form
        self.first_name = {
            'title': 'first_name',
            'locator': self.page.locator(PracticeFormPL.FIRST_NAME),
            'selector': PracticeFormPL.FIRST_NAME
        }
        self.last_name = {
            'title': 'last_name',
            'locator': self.page.locator(PracticeFormPL.LAST_NAME),
            'selector': PracticeFormPL.LAST_NAME
        }
        self.email = {
            'title': 'email',
            'locator': self.page.locator(PracticeFormPL.EMAIL),
            'selector': PracticeFormPL.EMAIL
        }
        self.gender_male = {
            'title': 'gender_male',
            'locator': self.page.locator(PracticeFormPL.GENDER_MALE),
            'selector': PracticeFormPL.GENDER_MALE
        }
        self.gender_female = {
            'title': 'gender_female',
            'locator': self.page.locator(PracticeFormPL.GENDER_FEMALE),
            'selector': PracticeFormPL.GENDER_FEMALE
        }
        self.gender_other = {
            'title': 'gender_other',
            'locator': self.page.locator(PracticeFormPL.GENDER_OTHER),
            'selector': PracticeFormPL.GENDER_OTHER
        }
        self.phone_number = {
            'title': 'phone_number',
            'locator': self.page.locator(PracticeFormPL.PHONE_NUMBER),
            'selector': PracticeFormPL.PHONE_NUMBER
        }
        self.birth_date = {
            'title': 'birth_date',
            'locator': self.page.locator(PracticeFormPL.BIRTH_DATE),
            'selector': PracticeFormPL.BIRTH_DATE
        }
        self.subjects = {
            'title': 'subjects',
            'locator': self.page.locator(PracticeFormPL.SUBJECTS),
            'selector': PracticeFormPL.SUBJECTS
        }
        self.hobby_sports = {
            'title': 'hobby_sports',
            'locator': self.page.locator(PracticeFormPL.HOBBY_SPORTS),
            'selector': PracticeFormPL.HOBBY_SPORTS
        }
        self.hobby_reading = {
            'title': 'hobby_reading',
            'locator': self.page.locator(PracticeFormPL.HOBBY_READING),
            'selector': PracticeFormPL.HOBBY_READING
        }
        self.hobby_music = {
            'title': 'hobby_music',
            'locator': self.page.locator(PracticeFormPL.HOBBY_MUSIC),
            'selector': PracticeFormPL.HOBBY_MUSIC
        }
        self.upload_picture = {
            'title': 'upload_picture',
            'locator': self.page.locator(PracticeFormPL.UPLOAD_PICTURE),
            'selector': PracticeFormPL.UPLOAD_PICTURE
        }
        self.current_address = {
            'title': 'current_address',
            'locator': self.page.locator(PracticeFormPL.CURRENT_ADDRESS),
            'selector': PracticeFormPL.CURRENT_ADDRESS
        }
        self.state = {
            'title': 'state',
            'locator': self.page.locator(PracticeFormPL.STATE),
            'selector': PracticeFormPL.STATE
        }
        self.city = {
            'title': 'city',
            'locator': self.page.locator(PracticeFormPL.CITY),
            'selector': PracticeFormPL.CITY
        }
        self.submit = {
            'title': 'submit',
            'locator': self.page.locator(PracticeFormPL.SUBMIT),
            'selector': PracticeFormPL.SUBMIT
        }
