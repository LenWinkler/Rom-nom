# start of a fn that will move the unzipped files to the appropriate folders
# on the flash drive

import os, shutil, zipfile

def move_roms(dl_dir, dest_dir):

    os.chdir(r'/Users/lenwinkler/Desktop/RETROPIE/ROMS/NES')
    cwd = os.getcwd()
    os.makedirs('zip_files', exist_ok=True)

    if not os.path.isfile(cwd + '/inventory.txt'):
        inventory = open('inventory.txt', 'a')
        inventory.close()

    for zip_file in os.listdir(cwd):
        if zip_file.startswith('.') or not zip_file.endswith('.zip'):
            continue
        
        shutil.copy(zip_file, cwd + '/zip_files')

        with zipfile.ZipFile(os.path.abspath(zip_file), 'r') as zip_ref:
            zip_ref.extractall(cwd)

        with open('inventory.txt', 'a') as inventory:
            inventory.write(zip_file[:-4] + '\n')
            inventory.close()

        os.remove(zip_file)

        # print('\n' + '*' * 10)
        # print(folder)
        # for file in os.listdir(os.path.abspath(folder)):
        #     if file.startswith('.') or file.endswith('.txt'):
        #         continue
        #     print(' ---' + file)

        # print('*' * 10)

move_roms('dl_dir', 'dest_dir')