import os
import time

from chrome_custom import new_chrome_browser
from get_links import get_links


def download_roms(url, file_destination, filters):
    driver = new_chrome_browser(file_destination)
    os.chdir(file_destination)
    print('starting rom nom ᗧ * * *\n')
    time.sleep(3)
    driver.get(url)
    time.sleep(3)

    start = time.perf_counter()
    download_count = 0

    already_downloaded = set()
    resuming_download = os.path.isfile('progress.txt')

    if resuming_download:
        print('figuring out where we left off. this may take a minute...\n')
        with open('progress.txt', 'r') as progress:
            for line in progress:
                already_downloaded.add(line.rstrip())
        progress.close()

    while resuming_download:
        links = get_links(driver)

        if links[-1] in already_downloaded:
            next_page = driver.find_element_by_xpath("//a[@title='Next page']")
            driver.execute_script("arguments[0].scrollIntoView(true);", 
                                  next_page)
            next_page.click()
            time.sleep(2)
        else:
            resuming_download = False

    should_continue = True

    while should_continue:
        links = get_links(driver)

        print('opening tabs ᗧ * * * 🍒\n')
        for i in range(len(links)):
            driver.execute_script("window.open('');")

        tabs = driver.window_handles[1:]

        print('starting downloads ᗧ * * 👻 * 👻\n')
        for i in range(len(tabs)):
            driver.switch_to.window(tabs[i])
            driver.get(links[i])
            dl_button = driver.find_elements_by_class_name('btn__right')[0]
            rom_name = driver.find_element_by_xpath("//h1"
                                                    "[@itemprop='name']").text
            should_skip = False

            if filters:
                for f in filters:
                    if f in rom_name.lower():
                        should_skip = True
                        break

            if should_skip:
                continue

            if links[i] in already_downloaded:
                continue

            with open('inventory.txt', 'a') as inventory:
                inventory.write(rom_name + '\n')
            inventory.close()

            already_downloaded.add(links[i])
            with open('progress.txt', 'a') as progress:
                progress.write(links[i] + '\n')

            dl_button.click()
            download_count += 1
            print(f'downloading {rom_name}')

        print('\nclosing tabs ᗤ  👻 👻\n')
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
    print(f'downloaded {download_count} roms' 
           'in {round(time_elapsed, 2)} hours')

    os.remove('progress.txt')
