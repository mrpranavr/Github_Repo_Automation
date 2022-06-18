import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

fileName = sys.argv[1]
path = sys.argv[2]
browser = webdriver.Chrome()
browser.get('https://github.com/login')

# Enter the github username and password here
username = ''
password = ''

def createRepo():
    folderName = str(fileName)
    os.makedirs(path + "/" + folderName)
    usernameForm = browser.find_element(by= By.XPATH, value='//*[@id="login_field"]')
    usernameForm.send_keys(username)

    passwordForm = browser.find_element(by= By.XPATH, value='//*[@id="password"]')
    passwordForm.send_keys(password)

    submitButton = browser.find_element(by= By.XPATH, value='//*[@id="login"]/div[4]/form/div/input[12]')
    submitButton.click()

    browser.get('https://github.com/new')

    newRepoForm = browser.find_element(by= By.XPATH, value='//*[@id="repository_name"]')
    newRepoForm.send_keys(fileName)

    createRepoButton = browser.find_element(by = By.CSS_SELECTOR, value= 'button.btn-primary.btn')
    createRepoButton.submit()

    browser.quit()

if __name__ == '__main__':
    createRepo()



