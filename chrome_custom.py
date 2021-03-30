import os

from selenium import webdriver


# creates a chrome instance with custom download path
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
