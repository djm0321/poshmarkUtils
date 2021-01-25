from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from send2trash import send2trash
import requests
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
    driver = webdriver.Chrome("/Users/dj/Documents/chromedriver")
    driver.get("https://poshmark.com/login")
    return driver

def getToCloset(driver, username, fromUser):
    first = True
    urlEnd = ""
    passIns = ["", "", "", ""]
    dept = ""
    cat = ""
    sort = "price_asc"
    avail = "available"
    base = "https://poshmark.com/closet/" + username
    if (fromUser[0] != ""):
        passIns[0] = "department=" + fromUser[0]
    if (fromUser[1] != ""):
       passIns[1] = "category=" + fromUser[1]
    if (fromUser[2] != ""):
        passIns[2] = "sort_by=" + fromUser[2]
    passIns[3] = "availability=available"
    
    for x in passIns:
        if (x != ""):
            if (first):
                urlEnd = "?" + x
                first = False
            else:
                urlEnd = urlEnd + "&" + x
    driver.get(base + urlEnd)
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
    print("1")
    clicked = False
    shared = False
    while not clicked:
        try:
            print("2")
            item.click()
            print("3")
            clicked = True
        except ElementClickInterceptedException:
            input("Oops! Something went wrong. Please fix it, then click ENTER to continue.")
        except  ElementNotInteractableException:
            input("Oops! Something went wrong. Please fix it, then click ENTER to continue :(")
    time.sleep(random.randint(0, 1))
    if clicked:
        cts = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "pm-followers-share-linK")))
        while not shared:
            try:
                cts.click()
                shared = True
            except ElementClickInterceptedException:
                input("CaptchaCaptchaCaptcha")
            except ElementNotInteractableException:
                input("I Dont think that this is necessary but whatever ill leave it in for now")
        time.sleep(random.randint(0, 1))

# pm-party-share-link
# pm-followers-share-linK

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

def sharer(driver, username, passIns, minPrice):
    getToCloset(driver, username, passIns)
    loadWholePage(driver)
    itemArray = makeItemClass(driver)
    if minPrice != None:
        itemArray = sortByPrice(minPrice, itemArray)
    shareAll(driver, itemArray)

def begin(username, password, minPrice, sortBy, checkBoxes):
    driver = start()
    male = checkBoxes[1]
    female = checkBoxes[2]
    children = checkBoxes[3]
    home = checkBoxes[4]
    passIns = ["", "", sortBy]
    runState = signIn(driver, username, password)
    if runState == 2:
        if (checkBoxes[0]):
            if (male[0]):
                maleCats = getCats(male)
                passIns[0] = "Men"
                if maleCats == None:
                    sharer(driver, username, passIns, minPrice)
                else:
                    for x in maleCats:
                        passIns[1] = x
                        sharer(driver, username, passIns, minPrice)
            if (female[0]):
                femaleCats = getCats(female)
                passIns[0] = "Women"
                if femaleCats == None:
                    sharer(driver, username, passIns, minPrice)
                else:
                    for x in femaleCats:
                        passIns[1] = x
                        sharer(driver, username, passIns, minPrice)
            if children[0]:
                passIns[0] = "Kids"
                sharer(driver, username, passIns, minPrice)
            if home[0]:
                passIns[0] = "Home"
        else:
            sharer(driver, username, passIns, minPrice)
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

def getLabels(driver):
    driver.get("https://poshmark.com/order/sales")
    items = driver.find_elements_by_class_name("status")
    soldItems = 0
    for x in items:
        if soldItems == 0:
            value = x.find_elements_by_class_name("value")
            print(value[0].text)
            soldItems = soldItems + 1
    print(soldItems)
    # sales = driver.find_elements_by_class_name("item")
    # for x in range(0, soldItems):
    #     sales[x].click()
    
def resellItem():
    driver = start()
    driver.get("https://poshmark.com/listing/Dunhill-brown-down-parka-coat-jacket-XL-5e4b5e44969d1f0321df9718")
    pix = driver.find_elements_by_class_name("carousel-vertical__item")
    desc = driver.find_element_by_class_name("listing__description")
    descText = desc.text
    print(descText)
    picURLs = list()
    jpgNames = list()
    for x in range(0, len(pix)):
        temp = pix[x].find_element_by_class_name("img__container").find_element_by_tag_name("img").get_attribute("data-src")
        picURLs.append(temp.replace("s_", "m_", 1))
        temp2 = picURLs[x].split("/")
        jpgNames.append(temp2[len(temp2) - 1])

    
    for x in range(0, len(picURLs)):
        f = open(jpgNames[x], 'wb')
        f.write(requests.get(picURLs[x]).content)
        f.close()

    input()

    for x in range(0, len(picURLs)):
        send2trash(jpgNames[x])
 
