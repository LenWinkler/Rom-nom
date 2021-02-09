import os, shutil, zipfile, time

def move_roms(dl_dir, dest_dir):
    print('starting move...\n')
    start = time.perf_counter()
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

    inventory_list = []

    for zip_file in os.listdir(cwd):
        if zip_file.startswith('.') or not zip_file.endswith('.zip'):
            continue
        
        shutil.copy(zip_file, cwd + '/zip_files')

        with zipfile.ZipFile(os.path.abspath(zip_file), 'r') as zip_ref:
            zip_ref.extractall(cwd)

        inventory_list.append(zip_file[:-4])
        

        os.remove(zip_file)
    sort_start = time.perf_counter()
    inventory_list.sort()
    sort_end = time.perf_counter()
    print(f'sorting completed in {sort_end - sort_start:0.2f} seconds\n')

    print('building inventory file...\n')
    for title in inventory_list:
        with open('inventory.txt', 'a') as inventory:
            inventory.write(title + '\n')
            inventory.close()

    print('copying files to flash drive...\n')
    for item in os.listdir(cwd):
        if item.endswith('nes'):
            shutil.copy(item, dst_dir)
        elif item == 'zip_files' or item == 'inventory.txt':
            continue
        os.remove(item)

    end = time.perf_counter()
    print(f'move completed in {end - start:0.2f} seconds\n')

move_roms('dl_dir', 'dest_dir')