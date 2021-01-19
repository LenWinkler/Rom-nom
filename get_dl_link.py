# basic outline for function that grabs the rom download link from a page

import requests, bs4, sys

def get_dl_link():
    if len(sys.argv) == 1:
        url = input('Enter url: ')
    else: 
        url = sys.argv[1]

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    a_tag = soup.select('#download_link')[0]
    return a_tag['href']


print(get_dl_link())