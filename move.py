# start of a fn that will move the unzipped files to the appropriate folders
# on the flash drive

import os, shutil

def move_roms(dl_dir, dest_dir):

    os.chdir(r'/Users/lenwinkler/Desktop/RETROPIE/ROMS/NES')
    os.makedirs('zip_files', exist_ok=True)

    for zipfile in os.listdir(os.getcwd()):
        if zipfile.startswith('.') or not zipfile.endswith('.zip'):
            continue
        
        shutil.copy(zipfile, os.getcwd() + '/zip_files')
        
        

        # print('\n' + '*' * 10)
        # print(folder)
        # for file in os.listdir(os.path.abspath(folder)):
        #     if file.startswith('.') or file.endswith('.txt'):
        #         continue
        #     print(' ---' + file)

        # print('*' * 10)

move_roms('dl_dir', 'dest_dir')