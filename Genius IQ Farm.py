# This bot only works for pinned annotations, other than that it won't work ! !

import asyncio
import requests
from pystyle import * 
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import pytz
import string
import os
import json
import random

Write.Print("ONLY WORKS FOR A PINNED ANNOTATION ON SOMEONE'S PROFILE OR ELSE IT WON'T WORK", Colors.red, interval=0)
print(" ")
page = Write.Input("PROFILE LINK > ", Colors.blue, interval=0)
print(" ")

def login_to_website(name, email, password):
    # Set up Selenium WebDriver with appropriate options
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)

    # Load the login page and fill in the credentials
    driver.get("https://genius.com/signup")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[4]").click()
    driver.find_element(By.ID, "user_login").send_keys(name)
    driver.find_element(By.ID, "user_email").send_keys(email)
    driver.find_element(By.ID, "user_password").send_keys(password)
    driver.find_element(By.ID, "user_submit").click()
    driver.get(page)
    driver.find_element(By.XPATH, "/html/body/routable-page/ng-outlet/routed-page/profile-page/div[3]/div[2]/div/div[2]/profile-annotation/div/div[3]/annotation/div[3]/voting/div/div[1]/span").click()
    # Wait for the login process to complete
    driver.implicitly_wait(1)
    return driver

async def follow_account():
    try:
        global web
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + "@gmail.com"
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        print(name, email, password)

        driver = login_to_website(name, email, password)
        
        print(f"An account has been created. (name : {name}, email : {email}, password : {password})")
    except Exception as error:
        print(f"{error}")

async def on_ready():
    while True:
        await follow_account()
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(on_ready())
