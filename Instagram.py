from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    # twitter login
    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    #like tweet
    def like_post(self, hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(3)

        #scroll tweet
        for i in range(1, 3):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            posts = bot.find_elements_by_tag_name("a")
            links = [elem.get_attribute("href") for elem in posts] 
            
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9").click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)           
            

# PengenNikah
big = InstagramBot("username", "password")
big.login()
big.like_post("food")