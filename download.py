from selenium import webdriver
import time, os

# helper function that creates a chrome instance with custom download path
def new_chrome_browser():
    options = webdriver.ChromeOptions()
    download_path = '/Users/lenwinkler/Desktop/RETROPIE/ROMS/NES'
    os.makedirs(download_path, exist_ok=True)

    prefs = {}
    prefs['profile.default_content_settings.popups']=0
    prefs['download.default_directory']=download_path
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options, executable_path='/Users/lenwinkler/Downloads/chromedriver')

    return browser

def download_roms(url):
    driver = new_chrome_browser()
    print('opening url...')
    time.sleep(3)
    driver.get('https://romsmania.cc/roms/nintendo')
    print('grabbing links to download pages...')
    time.sleep(3)

    should_continue = True
    while should_continue:
        # grab all td tags, then put the url for each title into a list
        td_tags = driver.find_elements_by_tag_name('td')
        links = []
        for td in td_tags:
            try:
                links.append(td.find_element_by_tag_name('a').get_attribute('href'))
            except:
                continue

        print('opening tabs...')
        for i in range(len(links)):
            driver.execute_script("window.open('');")

        tabs = driver.window_handles[1:]

        print('starting downloads...\n')
        for i in range(len(tabs)):
            driver.switch_to.window(tabs[i])
            driver.get(links[i])
            dl_button = driver.find_elements_by_class_name('btn__right')[0]
            rom_name = driver.find_element_by_xpath("//h1[@itemprop='name']").text
            # for NES, if we hit the 'ZZZ' roms, quit
            if rom_name.startswith('ZZZ'):
                should_continue = False
                break
            dl_button.click()
            print(f'downloading {rom_name}')
            time.sleep(4)

        print('closing tabs...')
        for i in range(len(tabs)):
            driver.switch_to.window(tabs[i])
            driver.close()

        try:
            next_page = driver.find_element_by_xpath("//a[@title='Next page']")
        except:
            should_continue = False
            continue

        driver.execute_script("arguments[0].scrollIntoView(true);", next_page)
        next_page.click()

download_roms('asdf')