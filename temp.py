from selenium import webdriver
from send2trash import send2trash
import requests

def main():
    # driver = webdriver.Chrome("/Users/dj/Downloads/chromedriver")
    # driver.get("https://di2ponv0v5otw.cloudfront.net/posts/2020/02/17/5e4b5e44969d1f0321df9718/m_5e4b5e6e26219ffba19f8a3b.jpg")
    # f = open('test.jpg', 'wb')
    # f.write(requests.get("https://di2ponv0v5otw.cloudfront.net/posts/2020/02/17/5e4b5e44969d1f0321df9718/m_5e4b5e6e26219ffba19f8a3b.jpg").content)
    # f.close()
    # input()
    # send2trash('test.jpg') 
    temp = "https://di2ponv0v5otw.cloudfront.net/posts/2020/02/17/5e4b5e44969d1f0321df9718/m_5e4b5e6e26219ffba19f8a3b.jpg"
    temp2 = temp.split("/")
    print(temp2[len(temp2) - 1])
    


main()