from download import download_roms
from move import move_roms
from subprocess import call

url = input('\n\nEnter the romsmania url:\n\nURL: ').strip()
file_destination = input('\nWhere should the files be saved? (file path)\n\nFile path: ').strip()
filters = input('\nFilters? Titles containing these words/chars will be ignored.\nSeparate words/chars with spaces. Not case-sensitive.\nLeave blank for no filters\n\nFilters: ')
filters = filters.strip().split(' ')
filters = [f.lower() for f in filters]
if filters[0] == '':
    filters = []

call('clear')
download_roms(url, file_destination, filters)