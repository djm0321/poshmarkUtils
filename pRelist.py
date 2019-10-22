from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import pickle
import time
import random


PAUSE_FOR_SHARING = .5

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)
    
def start():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://poshmark.com/login")
    foo = input()
    return driver

def getToCloset(driver):
    driver.get("https://poshmark.com/closet/jenwm5?sort_by=price_asc&availability=available")
    dims = driver.get_window_size()
    height = dims['height']

def loadWholePage(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)") 

def share(driver, item):
    clicked = False
    while not clicked:
        try:
            item.click()
            clicked = True
        except ElementClickInterceptedException and ElementNotInteractableException:
            input("Oops! Something went wrong. Please fix it, then click ENTER to continue.")
    time.sleep(random.randint(0, 1))
    if clicked:
        cts = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pm-followers-share-link")))
        cts.click()

def shareAll(driver):
    sharers = driver.find_elements_by_class_name("share")
    for sharer in sharers:
        found = False
        while not found:
            try:
                share(driver, sharer)
                found = True
            except NoSuchElementException:
                time.sleep(random.randint(0, 2))
                driver.execute_script("window.scrollTo(0, height)")
        time.sleep(random.randint(1, 2))

def main():
    driver = start()
    getToCloset(driver)
    loadWholePage(driver)
    shareAll(driver)

# save_cookie(driver, '~/Documents/PoshmarkRelister/cookie.txt')
# driver = start()
# driver.get("https://poshmark.com/login")
# login = driver.find_element_by_name("login_form[username_email]")
# login.send_keys("jenwm5")
# pwd = driver.find_element_by_name("login_form[password]")
# pwd.send_keys("pay4college2day")
# pwd.send_keys(Keys.RETURN)
main()