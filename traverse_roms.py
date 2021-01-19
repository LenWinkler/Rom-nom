import requests, bs4
import get_dl_link from get_dl_link

def traverse_roms(url):
    res = requests.get(url)
    res.raise_for_status()