from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import datetime

HEAD_HUNTER = 'https://ufa.hh.ru/'
LOGIN = 'YOUR_LOGIN'
PASSWORD = 'PASSWORD'
browser = webdriver.Chrome()
actions = ActionChains(browser)


def login():
    browser.get(HEAD_HUNTER)
    login_button = browser.find_element(By.CSS_SELECTOR, "[data-qa='login']")
    login_button.click()
    enter_with_password = browser.find_element(By.CSS_SELECTOR, '[data-qa="expand-login-by-password"]')
    enter_with_password.click()
    phone_inp = browser.find_element(By.CSS_SELECTOR, '[data-qa="login-input-username"]')
    phone_inp.send_keys(LOGIN)
    password_inp = browser.find_element(By.CSS_SELECTOR, '[data-qa="login-input-password"]')
    password_inp.send_keys(PASSWORD)
    enter_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="account-login-submit"]')
    enter_button.click()


def up_my_cv():
    my_cv_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="mainmenu_myResumes"]')
    my_cv_button.click()
    cv_up_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="resume-update-button_actions"]')
    actions.move_to_element(cv_up_button)
    x = datetime.datetime.now()
    f = open('PATH_TO_FILE', 'a')
    if cv_up_button.text == 'Поднимать автоматически':
        browser.quit()
        f.write(f'Не обновилось {x.time()}\n')
    else:
        cv_up_button.click()
        f.write(f'Все обновилось, супер {x.time()}\n')
    f.close()


def main():
    login()
    sleep(5)
    up_my_cv()


if __name__ == '__main__':
    main()
