# basic outline for function that grabs the rom download link from a page

import requests, bs4

def get_dl_link(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    a_tag = soup.select('#download_link')[0]
    return a_tag['href']