# URLS
# fb login page
fb_login = 'https://facebook.com/login/'
# pleasanton homes for sale page
ph4s = 'https://www.facebook.com/pleasantonhome/'

# LOGIN PAGE PATHS
# "email or phone number" input box; xpath
login_box = '//*[@id="email"]'
# password input box; xpath
pass_box = '//*[@id="pass"]'

# POST STATUS (GENERAL) PATHS
# page post box; xpath
post_box = '//*[@aria-label="Write a post..."]'
# 'share now' post button; xpath
post_button = '//span[@id="composerPostButton"]'

# POST STATUS ADD ON PATHS
# 'feeling/activity' button; xpath 
feeling_button = '//*[contains(text(),"Feeling/Activity")]'
# 'feeling/activity' button; xpath 
check_in_button = '//*[contains(text(),"Check in")]'
# general button response input text box; xpath
add_info_box = '//*[@data-testid="searchable-text-input"]'
# 'more post options' dots (button); xpath -- # '//*[@aria-label="More post options"]'
more_post_options = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/ul/li[4]/span/a/div/i'
