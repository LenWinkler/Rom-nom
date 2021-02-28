import sys
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

y_or_n = {'y': True, 'n': False}
want_to_unzip = input('\nDo you want to unzip the downloaded files? (y/n): ')

while want_to_unzip.lower() not in y_or_n:
    print('\nplease answer y or n\n')
    want_to_unzip = input('Do you want to unzip the downloaded files? (y/n): ')

want_to_unzip = y_or_n[want_to_unzip]

if not want_to_unzip:
    sys.exit('\nquitting Rom Nom\n')

unzipped_roms_destination = input('\nEnter the destination filepath for the unzipped files\nLeave blank to unzip files where they were downloaded: ')

if unzipped_roms_destination == '':
    unzipped_roms_destination = file_destination

move_roms(file_destination, unzipped_roms_destination)