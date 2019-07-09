from user import u,p
from base import fbBot
from infos import ph4s

if __name__=='__main__':
    # tag facebook bot
    fb=fbBot(username=u,password=p)
    # start up driver, keep window large
    fb.start_driver(minimize=False)
    # log in to fb
    fb.login()
    # load ph4s page
    fb.load_page(url=ph4s)
    # set status
    msg='Hello, World!'
    # write status
    fb.write_post(text=msg)
    # post status
    fb.post_now()
    # close up shop
    fb.close_browser()
    