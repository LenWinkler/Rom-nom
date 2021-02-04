import os, shutil, zipfile

def move_roms(dl_dir, dest_dir):

    os.chdir(r'/Users/lenwinkler/Desktop/RETROPIE/ROMS/NES')
    cwd = os.getcwd()
    dst_dir = (r'/Volumes/UUI')
    os.makedirs('zip_files', exist_ok=True)

    if not os.path.isfile(fr'{cwd}/inventory.txt'):
        inventory = open('inventory.txt', 'a')
        inventory.close()

    if not os.path.isdir(fr'{dst_dir}/NES'):
        os.makedirs(fr'{dst_dir}/NES')
    dst_dir = fr'{dst_dir}/NES'

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

    for item in os.listdir(cwd):
        if item.endswith('nes'):
            shutil.copy(item, dst_dir)
        elif item == 'zip_files' or item == 'inventory.txt':
            continue
        os.remove(item)

move_roms('dl_dir', 'dest_dir')