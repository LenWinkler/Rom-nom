from download import download_roms
from move import move_roms

url = input('Enter the romsmania url:\nURL: ')
file_destination = input('Where should the files be saved? (file path)\nFile path: ')
filters = input('Filters? Titles containing these words/chars will be ignored.\nSeparate words/chars with spaces. Leave blank for no filters\nFilters: ')
filters = filters.strip().split(' ')

print('\n')
download_roms(url, file_destination, filters)