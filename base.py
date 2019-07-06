import time
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from infos import fb_login, login_box, pass_box


class fbBot:

    def __init__(self, username, password):
        # tag the options field
        options = webdriver.FirefoxOptions()  
        # disable push/popups 
        options.set_preference("dom.push.enabled", False)  
        # set user
        self.username = username
        # set pwrd
        self.password = password
        # set driver with options 
        self.driver = webdriver.Firefox(options=options)
        # minimize browser window
        self.driver.minimize_window()

    def login(self):
        """loads and logs in to facebook
        """
        # load facebook login page
        self.driver.get(fb_login)
        # wait (hedge load time)
        sleep(3)
        # find user box, type in account id
        self.driver.find_element_by_xpath(login_box).send_keys(self.username)
        # find key box and call locksmith, he should be able to punch in
        self.driver.find_element_by_xpath(pass_box).send_keys(self.password, Keys.RETURN)
        # hedge request/load time 
        sleep(3)

    def close_browser(self):
        """closes webdriver
        """
        self.driver.close()  


"""
# Automation of posting to Facebook
# NOTES
#    NEEDS
#     Selenium
#     ChromeDriver (in PATH)
#    POSSIBLE IMPROVEMENTS
#     Ability to use characters out of the BMP\
#      E.g. emojis
#       Idea: use FB emojis, access through XPATH
#     If using GeckoDriver
#        Escaping or blocking notifications alert


emailElement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailElement.send_keys("YOUR EMAIL")
print('Entered User...')
time.sleep(random.randrange(1, 2))


passElement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passElement.send_keys('YOUR PASSWORD')
print('Entered pass...')
sleep(random.randrange(1, 2))


elem = driver.find_element(By.XPATH, './/*[@id="loginbutton"]')
print('Logging in...')
elem.click()
time.sleep(random.randrange(2, 4))
# Sleep range can be lowered to 1-2 on most connections


print('Loading page...')
driver.get('YOUR PAGE LINK')
# E.g. https://www.facebook.com/FoodNetwork/
time.sleep(random.randrange(2, 4))


StatusElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/'
                                              'div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div/'
                                              'div[2]/div/div[1]/div/span/div/div[2]/div/div[1]/div/div/div/div/'
                                              'div[2]/div')
# XPATH of "Write a Post" box, may be different for you, used is the easy way not the most correct way
print('Found Status Box..')
time.sleep(random.randrange(1, 2))
print('Sending keys...')
StatusElement.send_keys(" Hello, World! "
                        " https://github.com/gumdropsteve/posttopage-facebook ")
# Advise having spaces before and after each line
# Still working on how to have the post 'Enter' into the next line
print('Status sent.. sleeping to load preview...')
# If you've included a link this pause is to load the preview
# NOTE: this does not always work and you may have to 'Edit' the post
#       If you are able to click the place after the link and add a 'space' it WILL work
sleep(random.randrange(2, 4))
# Extend sleep range to 8+ for best results if using above method


# Optional 'Check In'
CheckInElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/'
                                               'div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div/'
                                               'div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/span/a/div/div')
print('Located Check In...')
CheckInElement.click()
print('Clicked Check In...')
CheckInElement2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/'
                                                'div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/'
                                                'div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/'
                                                'span/span/label/input')
CheckInElement2.send_keys("Pleasanton, California")
# Fill in as much of the exact check in location as possible to ensure accurate results
print('Sent Location...')
CheckInElement2.click()
print('Location clicked...')
CheckInElement2.send_keys(u'\ue007')
# This is why you fill in as much of the location as possible, the top result is chosen here
print('Locked Check In...')
# Conformation of 'Check In' completion
time.sleep(random.randrange(1, 2))


# Optional Feeling/Activity
ActivityElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/'
                                                'div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/'
                                                'div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/'
                                                'span/a/div/div')
print('Located Feeling/Activity...')
ActivityElement.click()
print('Clicked Feeling/Activity...')
ActivityElement2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/'
                                                 'div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/'
                                                 'div/div/div[2]/div/div[2]/div[1]/div/div/span/span/label/input')
print('Located Specify Feeling/Activity...')
ActivityElement2.send_keys('Looking for')
print('Sent Feeling/Activity keys...')
ActivityElement2.send_keys(u'\ue007')
print('Locked in Feeling/Activity...')
ActivityElement3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/'
                                                 'div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/'
                                                 'div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/span/'
                                                 'span/label/input')
print('Located: What are you looking for?...')
ActivityElement3.send_keys('home recom')
print('Sent what is being looked for keys...')
ActivityElement3.send_keys(u'\ue007')
print('Locked in what is being looked for...')


PostElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/'
                                            'div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div/'
                                            'div[2]/div/div[2]/div[3]/div/div[2]/div/span[3]/div/span/button')
PostElement.click()
print('posting...')
time.sleep(random.randrange(3, 5))


print('finishing...')
sleep(7)
print("done")
"""
