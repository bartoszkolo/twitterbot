import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium import common

from paths import *

driver = webdriver.Chrome('C:/Users/XYZ/PycharmProjects/twitterbot/chromedriver')
driver.maximize_window()


class TwitterBot:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.logged = False
        self.bot = driver

    def login(self):
        bot = self.bot
        bot.get('http://twitter.com/i/flow/login')
        time.sleep(4)

        try:
            bot.find_element_by_xpath(email_xpath).send_keys(self.login)
            time.sleep(2)
            enter = bot.find_element_by_xpath(next_button_xpath)
            enter.click()
            bot.find_element_by_xpath(password_xpath)
            time.sleep(3)
            enter = bot.find_element_by_xpath(login_xpath)
            enter.click()
        except common.exceptions.NoSuchElementException:
            pass

        self.logged = True

    def logout(self):
        bot = self.bot
        bot.get('https://twitter.com/logout')
        time.sleep(2)
        logout_button = bot.find_element_by_xpath(logout_button_xpath)
        logout_button.click()
        self.logged = False

    def search(self, query=''):
        if not self.logged:
            raise Exception("You must be logged in to use a search method")

        bot = self.bot

        try:
            search_box = bot.find_element_by_xpath(search_box_xpath)
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            search_box = bot.find_element_by_xpath(search_box_xpath)

        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(keys.Keys.RETURN)
        time.sleep(10)

    def like(self, number_of_likes):
        bot = self.bot
        for i in range(number_of_likes):
            try:
                bot.find_element_by_xpath("//div[@data-testid='like']").click()
            except common.exceptions.NoSuchElementException:
                pass
            bot.execute_script('window.scrollBy(0, 250)')
            time.sleep(5)

    def direct_message(self, username, message):
        bot = self.bot
        bot.get("https://twitter.com/" + username)
        try:
            bot.find_element_by_xpath(direct_message_xpath).click()
        except common.exceptions.NoSuchElementException:
            pass
        try:
            bot.find_element_by_xpath(message_box_xpath).send_keys(message)
        except common.exceptions.NoSuchElementException:
            pass

    def comment(self, username, tweet_id, comment_text):
        bot = self.bot
        tweet_url = "https://twitter.com/{username}/status/".format(username=username, tweet_id=tweet_id)
        bot.get(tweet_url)
        try:
            time.sleep(3)
            bot.find_element_by_xpath(comment_xpath).click()
            time.sleep(3)
            bot.find_element_by_xpath(comment_input_xpath).send_keys(comment_text)
            time.sleep(3)
            bot.find_element_by_xpath(reply_button_xpath).click()
        except common.exceptions.NoSuchElementException:
            pass

