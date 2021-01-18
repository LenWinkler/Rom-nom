# TODOS:
# I want to be able to:
# --point a scraper at a url for a certain system (e.g. nes) on a rom site and
#   have it download all the roms for that system (paginated, many pages/files)
# --once they're downloaded, send a copy of the zip file to a "backup" folder
#   and unzip all the files
# --then, go through all the unzipped folders, grab each rom file, copy the
#   name (without extension) to an "inventory" file, and copy the rom to the
#   appropriate folder on a flash drive
# --finally, delete zip files (outside of "backup") and unzipped folders
#   (could maybe do this right after rom is copied to flash drive)


import os

os.chdir(r'/Users/lenwinkler/Desktop/RETROPIE/ROMS/')

for folder in os.listdir(os.getcwd()):
    if folder.startswith('.'):
        continue

    print('\n' + '*' * 10)
    print(folder)
    for file in os.listdir(os.path.abspath(folder)):
        if file.startswith('.') or file.endswith('.txt'):
            continue
        print(' ---' + file)

    print('*' * 10)