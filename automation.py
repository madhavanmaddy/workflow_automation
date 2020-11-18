import os

import getpass

import time

from selenium import webdriver

name = input("Enter the Project Name : ")

user = input("Enter your Github Username : ")

userpass = getpass.getpass(prompt="Enter your Github password : ")

os.system('flutter create '+name)

cur = os.getcwd()

os.chdir(cur+'/'+name)

os.system('git init .')

browser = webdriver.Chrome()

browser.get('https://www.github.com/login')

time.sleep(2)

username = browser.find_element_by_xpath('//*[@id="login_field"]')

username.send_keys(user)

password = browser.find_element_by_xpath('//*[@id="password"]')

password.send_keys(userpass)

signinButton = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')

signinButton.click()

time.sleep(2)

newButton = browser.find_element_by_xpath('//*[@id="repos-container"]/h2/a')

newButton.click()

time.sleep(2)

nameField = browser.find_element_by_xpath('//*[@id="repository_name"]')

nameField.send_keys(name)

time.sleep(2)

createRepoButton = browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')

createRepoButton.click()

time.sleep(2)

browser.close()

repourl = 'https://github.com/'+user+'/'+name+'.git'

remoteadd = 'git remote add origin '+repourl

os.system(remoteadd)

os.system('git add .')

os.system('git commit -m "Initial Commit"')

os.system('git push -u origin master')

os.system('code .')
