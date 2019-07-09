import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from infos import fb_login, login_box, pass_box, post_box, post_button


class fbBot:

    def __init__(self, username, password):
        # set user
        self.username = username
        # set pwrd
        self.password = password

    def login(self):
        """loads and logs in to facebook
        """
        # load facebook login page
        self.load_page(fb_login)
        # wait (hedge load time)
        time.sleep(3)
        # find user box, type in account id
        self.driver.find_element_by_xpath(login_box).send_keys(self.username)
        # find key box and call locksmith, he should be able to punch in
        self.driver.find_element_by_xpath(pass_box).send_keys(self.password, Keys.RETURN)
        # hedge request/load time 
        time.sleep(4)

    def write_post(self, text):
        """locates post box and writes out (text) post
        inputs)
        > text
            >> message to be shared in post, text only 
        """
        # find the post box & send message text 
        self.driver.find_element_by_xpath(post_box).send_keys(text)
        # hedge type time 
        time.sleep(1)
        # long post?
        if len(text) > 99:
            # hedge type time
            time.sleep(1 * (len(text)/100))

    def post_now(self):
        """locates and clicks 'share now' button
        """
        # find and click 'share now' button 
        self.driver.find_element_by_xpath(post_button).click()

    # helper functions
    def start_driver(self, specs=True, minimize=True):
        """starts up geckodriver session
        inputs)
        > specs
            >> turns off pop-up notifications 
        """
        # default
        if specs == True:
            # tag the options field
            prefs = webdriver.FirefoxOptions()  
            # disable push/popups 
            prefs.set_preference("dom.push.enabled", False)  
            # spin up driver
            self.driver = webdriver.Firefox(options=prefs)
            # default
            if minimize == True:
                # minimize browser window
                self.driver.minimize_window()
        # no hedge on pop-ups
        else:
            # spin up default driver
            self.driver = webdriver.Firefox()
            # default
            if minimize == True:
                # minimize browser window
                self.driver.minimize_window()

    def close_browser(self):
        """closes webdriver
        """
        self.driver.close()  

    def load_page(self, url):
        """loads given web address
        inputs)
        > url
            >> web address to load
        """
        # init webpage
        self.url = url
        # load webpage
        self.driver.get(self.url)
        # hedge load time
        time.sleep(4)

