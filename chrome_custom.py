import os

from selenium import webdriver


"""
Creates a chrome instance with custom download path, which is gathered from
user input in rom_nom.py

The executable_path on line 22 should be the location of your chromedriver. I
set mine to /Downloads for the sake of convenience

N.B. - Make sure your version of chromedriver supports your version of chrome!
"""

def new_chrome_browser(download_path):
    options = webdriver.ChromeOptions()
    os.makedirs(download_path, exist_ok=True)

    prefs = {}
    prefs['profile.default_content_settings.popups']=0
    prefs['download.default_directory']=download_path
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options, 
                               executable_path=('/Users/lenwinkler'
                                                '/Downloads/chromedriver'))
    return browser
