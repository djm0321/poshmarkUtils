from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import pickle
import time
import random
from pClass import *


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
    driver = webdriver.Chrome("/Users/dj/Downloads/chromedriver")
    driver.get("https://poshmark.com/login")
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
        except ElementClickInterceptedException:
            input("Oops! Something went wrong. Please fix it, then click ENTER to continue.")
        except  ElementNotInteractableException:
            input("Oops! Something went wrong. Please fix it, then click ENTER to continue :(")
    time.sleep(random.randint(0, 1))
    if clicked:
        cts = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pm-followers-share-link")))
        cts.click()

def makeItemClass(driver):
    sharers = driver.find_elements_by_class_name("share")
    items = driver.find_elements_by_class_name("price")
    prices = list()
    for x in range(len(items)):
        prices.append(int(items[x].text.split(" ", 1)[0][1:]))
    itemArray = list()
    for x in range(len(sharers)):
        itemArray.append(Item(sharers[x], prices[x]))
    return itemArray

def shareAll(driver, itemArray):
    print(itemArray[0].price)
    driver.execute_script("arguments[0].scrollIntoView();", itemArray[0].share_button)
    driver.execute_script("window.scrollTo(0, -250)")
    for item in itemArray:
        found = False
        while not found:
            try:
                share(driver, item.share_button)
                found = True
            except NoSuchElementException:
                time.sleep(random.randint(1, 2))
                driver.execute_script("window.scrollTo(0, height)")
        time.sleep(random.randint(1, 3))

def shareGroups(driver):
    print("Maybe this will work later")

def signIn(driver, username, password):
    login = driver.find_element_by_name("login_form[username_email]")
    pwd = driver.find_element_by_name("login_form[password]")
    login.send_keys(username)
    pwd.send_keys(password)
    pwd.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        driver.find_element_by_id("rc-anchor-container")
    except: 
        try:
            driver.find_element_by_class_name("base_error_message")
        except:
            return 2
        else:
            input()
            return 2
    else:
        return 0


def begin(username, password, minPrice):
    driver = start()
    runState = signIn(driver, username, password)
    if runState == 2:
        getToCloset(driver)
        loadWholePage(driver)
        itemArray = makeItemClass(driver)
        if minPrice != None:
            itemArray = sortByPrice(minPrice, itemArray)
        shareAll(driver, itemArray)
        driver.close()
    elif runState == 1:
        print("You dumb fuck you put the wrong shit in idiot now go try again and try not to be as bad at doing stuff this time")
        driver.close()
    elif runState == 0:
        print("Captcha has shown up (probably bc u suck at entering ur info). Please log in on site, complete captcha and then continue by pressing ENTER")
        foo = input()
        getToCloset(driver)
        loadWholePage(driver)
        shareAll(driver)
        driver.close()

# save_cookie(driver, '~/Documents/PoshmarkRelister/cookie.txt')
# driver = start()
# driver.get("https://poshmark.com/login")
# login = driver.find_element_by_name("login_form[username_email]")
# login.send_keys("jenwm5")
# pwd = driver.find_element_by_name("login_form[password]")
# pwd.send_keys("pay4college2day")
# pwd.send_keys(Keys.RETURN)