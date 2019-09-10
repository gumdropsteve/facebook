from user import u, p
from base import fbBot
from infos import ph4s

if __name__=='__main__':
    # tag facebook bot
    fb = fbBot(user=u)
    # start up driver, keep window large
    fb.start_driver(minimize=False)
    
    # log in to fb
    fb.login(password=p)
    # load ph4s page
    fb.load_page(url=ph4s)
    
    # write status
    status = f'Hello,\nWorld!\nhttp://bit.ly/2kcA60f '
    fb.write_post(text=status, link=True)
    
    # expand post customization options
    fb.expand_post_options()  
    # add feeling
    fb.add_feeling(general='looking for', specific='a house')
    # add location     
    fb.add_location('Pleasanton, Ca')

    # post status
    fb.share_post()
    # close up shop
    fb.close_browser(test=True)
    