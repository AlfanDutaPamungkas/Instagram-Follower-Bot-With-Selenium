from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME_IG")
PASS = os.getenv("PASS")
TARGET = os.getenv("TARGET")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)

        self.driver = webdriver.Chrome(options=chrome_options)
        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(10)
        username_bar = self.driver.find_element(By.NAME, "username")
        username_bar.send_keys(USERNAME)
        
        password_bar = self.driver.find_element(By.NAME, "password")
        password_bar.send_keys(PASS)
        password_bar.send_keys(Keys.ENTER)
        
        time.sleep(5)
        not_btn = self.driver.find_element(By.CSS_SELECTOR, '._ac8f div')
        not_btn.click()

        time.sleep(5)
        off_notif = self.driver.find_element(By.CSS_SELECTOR, '._a9-z ._a9_1')
        off_notif.click()
        
    def find_follower(self):
        self.driver.get(f"https://www.instagram.com/{TARGET}/followers/")
        
        time.sleep(5)
        follower_body = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]')

        for i in range(1,11):
            self.follow(i)
            time.sleep(1)
            if i % 5 == 0:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_body)
    
    def follow(self,i):
        follow_btn = self.driver.find_element(By.XPATH, f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
        follow_btn.click()
        
insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_follower()
