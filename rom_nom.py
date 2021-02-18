from download import download_roms
from move import move_roms

url = input('Enter the romsmania url:\n\nURL: ')
file_destination = input('\nWhere should the files be saved? (file path)\n\nFile path: ')
filters = input('\nFilters? Titles containing these words/chars will be ignored.\nSeparate words/chars with spaces. Not case-sensitive.\n Leave blank for no filters\n\nFilters: ')
filters = filters.strip().split(' ')
filters = [f.lower() for f in filters]

print('\n')
download_roms(url, file_destination, filters)