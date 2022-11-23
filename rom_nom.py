import sys
from subprocess import call

from rich.console import Console
from rich.text import Text

from download import download_roms
from move import move_roms


call('clear')
print('\n')
console = Console()

# Prints Rom Nom on start
console.print(Text.assemble(
             ("   _________  ____ ___     ____  ____  ____ ___ ", 
              "bold green")))
console.print(Text.assemble(
             (r"  / ___/ __ \/ __ `__ \   / __ \/ __ \/ __ `__ \ ", 
               "bold green")))
console.print(Text.assemble(
             (r" / /  / /_/ / / / / / /  / / / / /_/ / / / / / /", 
               "bold green")))
console.print(Text.assemble(
             (r"/_/   \____/_/ /_/ /_/  /_/ /_/\____/_/ /_/ /_/ ", 
               "bold green")))
print("                                                ")

# This will be the URL for the console that you'd like to download the roms for
# e.g. https://retromania.gg/roms/commodore-64
url = input('\n\nEnter the romsmania url\n\nURL: ').strip()

# Where you want the roms to be saved on your machine
file_destination = input('\nWhere should the files be saved?' 
                         '(file path)\n\nFile path: ').strip()

# Useful for filtering out certain substrings. e.g. 'Hack', '[hFFE]'. etc.
# Be careful not to be too vague! You'll end up filtering too much
filters = input('\nFilters? Titles containing these words/chars will be ' 
                'ignored.\nSeparate words/chars with spaces. Not '
                'case-sensitive.\nLeave blank for no filters\n\nFilters: ')
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

# Where you want to unzip the files. If left blank, it'll use download location
unzipped_roms_destination = input('\nEnter the destination filepath for the ' 
                                  'unzipped files\nLeave blank to unzip files ' 
                                  'where they were downloaded: ')

if unzipped_roms_destination == '':
    unzipped_roms_destination = file_destination

move_roms(file_destination, unzipped_roms_destination)
