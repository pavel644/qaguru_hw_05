import os.path
from selene import browser, be, have, command
import tests


def test_submit_all_fields(set_browser_resolution):
    # GIVEN
    browser.open('https://demoqa.com/automation-practice-form')

    # WHEN
    browser.element('#firstName').should(be.blank).type('Pavel')
    browser.element('#lastName').should(be.blank).type('Gorozhankin')
    browser.element('#userEmail').should(be.blank).type('test_mail@test.mail')

    browser.element('[name=gender][value=Male]+label').click()

    browser.element('#userNumber').should(be.blank).type('7987654321')

    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__year-select').send_keys('1992')
    browser.element('[aria-label*="May 7th, 1992"]').click()

    browser.element('#subjectsInput').should(be.blank).type('math').press_enter()

    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Music')).click()

    avatar_path = os.path.join(
        os.path.dirname(os.path.abspath(tests.__file__)), 'resources', 'avatar.jpg'
    )
    browser.element('#uploadPicture').set_value(avatar_path)

    browser.element('#currentAddress').should(be.blank).type('Russia, Samara')

    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('.modal-header').should(
        have.text('Thanks for submitting the form')
    )
    browser.element('.table > tbody').should(
        have.text('Student Name Pavel Gorozhankin')). \
        should(have.text('Student Email test_mail@test.mail')). \
        should(have.text('Gender Male')). \
        should(have.text('Mobile 7987654321')). \
        should(have.text('Date of Birth 07 May,1992')). \
        should(have.text('Subjects Maths')). \
        should(have.text('Hobbies Music')). \
        should(have.text('Picture avatar.jpg')). \
        should(have.text('Address Russia, Samara')). \
        should(have.text('State and City Uttar Pradesh Lucknow'))
