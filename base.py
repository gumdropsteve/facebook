import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class fbBot:

    def __init__(self, user):
        # set user
        self.user = user

    def login(self, password):
        from infos import fb_login, login_box, pass_box
        """loads and logs in to facebook
        """
        # load facebook login page
        self.load_page(fb_login)
        # find user box, type in account id
        self.driver.find_element_by_xpath(login_box).send_keys(self.user)
        # find key box and call locksmith, he should be able to punch in
        self.driver.find_element_by_xpath(pass_box).send_keys(password, Keys.RETURN)
        time.sleep(self.page_load_time)

    def write_post(self, text, link=False):
        from infos import post_box
        """locates post box and writes out (text) post
        inputs)
        > text
            >> message to be shared in post, text only 
        """
        # find the post box & send message text 
        self.driver.find_element_by_xpath(post_box).send_keys(text)
        # long post?
        extra_long = int(len(text)/100)
        # hedge type time 
        time.sleep(self.action_load_time + extra_long)
        # is there a link?
        if link:
            # provide extra load time
            time.sleep(self.page_load_time)

    def add_feeling(self, general, specific):
        from infos import feeling_button, add_info_box
        """add a 'feeling/activity' to the post
        inputs)
        > general
            >> the feeling/activity to be added (to the post)
        > specific 
            >> the specific thing being felt or activity being done
        """
        # find 'feeling/activity' button & click it
        self.driver.find_element_by_xpath(feeling_button).click()
        time.sleep(self.action_load_time)
        # find input box & send feeling
        self.driver.find_element_by_xpath(add_info_box).send_keys(general)
        time.sleep(self.action_load_time)
        # select top result
        self.driver.find_element_by_xpath(add_info_box).send_keys(Keys.RETURN)
        # find input box & send feeling
        self.driver.find_element_by_xpath(add_info_box).send_keys(specific)
        time.sleep(self.action_load_time)
        # select top result
        self.driver.find_element_by_xpath(add_info_box).send_keys(Keys.RETURN)

    def add_location(self, location):
        from infos import check_in_button, add_info_box
        """add a location to the post
        inputs)
        > location
            >> the location to be added
        """
        # find 'Check in' button & click it
        self.driver.find_element_by_xpath(check_in_button).click()
        time.sleep(self.action_load_time)
        # find input box & send feeling
        self.driver.find_element_by_xpath(add_info_box).send_keys(location)
        time.sleep(self.action_load_time)
        # select top result
        self.driver.find_element_by_xpath(add_info_box).send_keys(Keys.RETURN)

    def expand_post_options(self):
        from infos import more_post_options
        """taps the 3 dots to expand post customization options
        """
        # find 'more post options' button (3 dots) and click
        self.driver.find_element_by_xpath(more_post_options).click() 

    def share_post(self, now=True):
        from infos import post_button
        """locates and clicks 'share now' button
        """
        # default is to post now
        if now:
            # find and click 'share now' button 
            self.driver.find_element_by_xpath(post_button).click()
            time.sleep(self.page_load_time)
        else:
            # pending, used in testing now
            pass

    # helper functions
    def start_driver(self, specs=True, minimize=True, page_load_time=2, action_load_time=1):
        """starts up geckodriver session
        inputs)
        > specs
            >> turns off pop-up notifications 
        > minimize
            >> minimized browser window? 
                > default yes (True)
        > page_load_time
            >> extra sleep time for rendering pages during this session 
                > default = 2
        > action_load_time
            >> extra sleep time taken after an interaction
                > default = 1
        """
        # set load times
        self.page_load_time = page_load_time
        self.action_load_time = action_load_time

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

    def load_page(self, url):
        """loads given web address
        inputs)
        > url
            >> web address to load
        """
        # set target location (url)
        self.target = url
        # go to location (load webpage)
        self.driver.get(self.target)
        # hedge load time
        time.sleep(self.page_load_time)

    def close_browser(self, test=False):
        """closes webdriver
        inputs)
        > test
            >> default False
                > if True, 
        """
        if test == False:
            # default, close browser
            self.driver.close()  
        # we are testing
        else:
            # and may need to see the window
            pass
