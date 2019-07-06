from user import u,p
from base import fbBot
if __name__=='__main__':
    fb=fbBot(username=u,password=p)
    fb.login()
    fb.close_browser()
    