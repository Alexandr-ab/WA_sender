from pages.register_page import RegisterPage
from selenium.common.exceptions import ElementNotInteractableException
import time

link = 'http://qa.noveogroup.com/'
user_data = ['John Doe', 'test@mail.com', 'Qwerty123', 'Qwerty123', '01/01/2001']

def check_user_register():
    print('Check user registration. Positive test')
    page = RegisterPage(link)
    page.open()
    page.check_for_elements_presens()
    page.enter_data(*user_data)
    page.register_success()
    print('=' * 10)
    page.close()

def check_register_existed_emails(emails):
    print('\nCheck registration with existed emails. Negative test')
    page = RegisterPage(link)
    page.open()
    page.check_for_elements_presens()
    for email in emails:
        page.enter_data('John Doe', email, 'Qwerty123', 'Qwerty123', '01/01/2001')
        if page.register_success(f'with {email}'):
            print('Test Failed')
        else:
            print(f'Test is successful with {email}')
        page.refresh()
    print('=' * 10)
    page.close()

def check_password_requirements(passwords):
    print('\nCheck password requirements. Negative test')
    page = RegisterPage(link)
    page.open()
    page.check_for_elements_presens()
    for password in passwords:
        page.enter_data('John Doe', 'test@email.com', password[0], password[1], '01/01/2001')
        if page.should_be_invalid_feedback():
            print(f'Test is successful with {password[0]} / {password[1]}')
        else:
            print(f'Test failed with {password[0]} / {password[1]}')
        page.refresh()
    print('=' * 10)
    page.close()

def check_email_requirements(email):
    print('\nCheck email requirements. Negative test')
    page = RegisterPage(link)
    page.open()
    page.check_for_elements_presens()
    page.enter_data('John Doe', email, 'Qwerty123', 'Qwerty123', '01/01/2001')
    if page.should_be_invalid_feedback():
        print(f'Test is successful with {email}')
    else:
        print(f'Test failed with {email}')
    print('=' * 10)
    page.close()

def check_required_fields():
    multi_user_data = [['', 'test@mail.com', 'Qwerty123', 'Qwerty123', '01/01/2001'],
                       ['John Doe', '', 'Qwerty123', 'Qwerty123', '01/01/2001'],
                       ['John Doe', 'test@mail.com', '', 'Qwerty123', '01/01/2001'],
                       ['John Doe', 'test@mail.com', 'Qwerty123', '', '01/01/2001'],
                       ['John Doe', 'test@mail.com', 'Qwerty123', 'Qwerty123', '']]
    print('\nCheck empty required fields. Negative test')
    page = RegisterPage(link)
    page.open()
    page.check_for_elements_presens()
    for item in multi_user_data:
        page.enter_data(*item)
        page.should_be_invalid_feedback()
        try:
            page.enter_data(*user_data)
            print('Test is successful after data input:', *['-Empty-' if i == '' else i for i in item], sep=' / ')
        except ElementNotInteractableException:
            print('Webpage doesn\'t respond after data input:', *['-Empty-' if i == '' else i for i in item], sep=' / ')
        page.refresh()
    print('=' * 10)
    page.close()

check_user_register()
check_register_existed_emails(['user@domain.com', 'me@domain.com', 'admin@domain.com'])
check_password_requirements([['qwerty', 'qwerty'], ['Qwerty123', 'Qwerty321']])
check_email_requirements('test@mail')
check_required_fields()