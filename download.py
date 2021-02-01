from selenium import webdriver
import time

def download_roms(url):
    driver = webdriver.Chrome()
    print('opening url...')
    time.sleep(3)
    driver.get('https://romsmania.cc/roms/nintendo')
    print('grabbing links to dl pages...')
    time.sleep(3)

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

    print('starting downloads...')
    for i in range(len(tabs)):
        driver.switch_to.window(tabs[i])
        driver.get(links[i])
        dl_button = driver.find_elements_by_class_name('btn__right')[0]
        dl_button.click()
        time.sleep(10)

download_roms('asdf')