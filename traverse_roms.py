# import requests, bs4
# import get_dl_link from get_dl_link

# def traverse_roms(url):
#     res = requests.get(url)
#     res.raise_for_status()

# bs4 doesn't work since site uses JS to start dl. switching to selenium

from selenium import webdriver

driver = webdriver.Firefox()

# grab all td tags, then put the url for each title into a list
td_tags = driver.find_elements_by_tag_name('td')
links = []
for td in td_tags:
    try:
        links.append(td.find_element_by_tag_name('a').get_attribute('href'))
    except:
        continue