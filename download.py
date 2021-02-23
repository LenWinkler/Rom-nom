from selenium import webdriver
import time, os

def download_roms(url, file_destination, filters):

    # helper function that creates a chrome instance with custom download path
    def new_chrome_browser(save_location):
        options = webdriver.ChromeOptions()
        os.makedirs(save_location, exist_ok=True)

        prefs = {}
        prefs['profile.default_content_settings.popups']=0
        prefs['download.default_directory']=save_location
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=options, executable_path='/Users/lenwinkler/Downloads/chromedriver')

        return browser

    driver = new_chrome_browser(file_destination)
    print('starting rom nom ᗧ * * *\n')
    time.sleep(3)
    driver.get(url)
    time.sleep(3)

    start = time.perf_counter()
    download_count = 0

    already_downloaded = set()

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

        print('opening tabs ᗧ * * * 🍒\n')
        for i in range(len(links)):
            driver.execute_script("window.open('');")

        tabs = driver.window_handles[1:]

        print('starting downloads ᗧ * * 👻 * 👻\n')
        for i in range(len(tabs)):
            driver.switch_to.window(tabs[i])
            driver.get(links[i])
            dl_button = driver.find_elements_by_class_name('btn__right')[0]
            rom_name = driver.find_element_by_xpath("//h1[@itemprop='name']").text
            should_skip = False

            if filters:
                for f in filters:
                    if f in rom_name.lower():
                        should_skip = True
                        break

            if should_skip:
                continue

            if rom_name in already_downloaded:
                continue

            already_downloaded.add(rom_name)
            dl_button.click()
            download_count += 1
            print(f'downloading {rom_name}')

        print('closing tabs ᗤ  👻 👻\n')
        for i in range(len(tabs)):
            driver.switch_to.window(tabs[i])
            driver.close()
        
        driver.switch_to.window(driver.window_handles[0])

        try:
            next_page = driver.find_element_by_xpath("//a[@title='Next page']")
        except:
            should_continue = False
            continue

        driver.execute_script("arguments[0].scrollIntoView(true);", next_page)
        next_page.click()
        time.sleep(2)

    end = time.perf_counter()
    time_elapsed = (end - start) / 60 / 60
    print(f'downloaded {download_count} roms in {time_elapsed} hours')