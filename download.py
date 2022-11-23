import os
import time
from subprocess import call

from rich.console import Console
from rich.text import Text

from chrome_custom import new_chrome_browser
from get_links import get_links


def download_roms(url, file_destination, filters):
    console = Console()
    start_program_text = Text.assemble(("Starting rom nom ", "green"),
                                       ("ᗧ ", "bold yellow"), "* * *\n")
    left_off_text = Text.assemble(("Figuring out where we left off. "
                                  "This may take a minute... ⏳\n", "bold"))
    open_tabs_text = Text.assemble(("Opening tabs ", "green"), 
                                   ("ᗧ ", "bold yellow"), "* * * 🍒\n")
    start_dls_text = Text.assemble(("Starting downloads ", "green"), 
                                   ("ᗧ ", "bold yellow"), "* * 👻 * 👻\n")
    close_tabs_text = Text.assemble("\n", ("Closing tabs ", "bold"), 
                                    ("ᗤ ", "bold yellow"),  "👻 👻\n")
    # Open new chrome browser with user-specified download location
    driver = new_chrome_browser(file_destination)
    os.chdir(file_destination)
    console.print(start_program_text)
    # Needed sleep here to keep the driver from moving too quickly. It wouldn't
    # wait for chrome to fully start and that caused the script to hang
    time.sleep(3)
    driver.get(url)
    time.sleep(3)

    start = time.perf_counter()
    download_count = 0

    already_downloaded = set()
    # This is my janky implementation of a 'save' system. If the script sees a
    # progress file here, it assumes that the last download session for this
    # console didn't complete. After all pages have been gone through for a
    # given console, the progress file will be deleted
    resuming_download = os.path.isfile('progress.txt')

    # If resuming download, load progress file into already_downloaded
    if resuming_download:
        console.print(left_off_text)
        with open('progress.txt', 'r') as progress:
            for line in progress:
                already_downloaded.add(line.rstrip())
        progress.close()

    # This is where we figure out where we left off. It goes through each page
    # until it finds the page where the last rom isn't in already_downloaded
    # and that's where it starts. This would be much simpler if we could use
    # page numbers
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

        # Open n new tabs where n = number of download links on page
        console.print(open_tabs_text)
        for i in range(len(links)):
            driver.execute_script("window.open('');")

        tabs = driver.window_handles[1:]

        console.print(start_dls_text)
        for i in range(len(tabs)):
            # Switch to the ith tab and open the ith link
            # Find the download button and the rom name
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

            # This handles restarting a download session. We ignore previously
            # downloaded roms on our restart page
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
            console.print(Text.assemble(("Downloading  ", "green"), 
                                        (rom_name, "bold")))

        # After starting the downloads, we can close the tabs and move on
        console.print(close_tabs_text)
        tabs = driver.window_handles[1:]
        for i in range(len(tabs)):
            driver.switch_to.window(tabs[i])
            driver.close()
        
        driver.switch_to.window(driver.window_handles[0])

        call('clear')

        # This block helps us know when we're done. The last page won't have a
        # 'Next Page' button
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
    print(f'Downloaded {download_count} roms '
          f'in {round(time_elapsed, 2)} hours')

    os.remove('progress.txt')
