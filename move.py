# start of a fn that will move the unzipped files to the appropriate folders
# on the flash drive

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