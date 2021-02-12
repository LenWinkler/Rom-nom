import os, shutil, zipfile, time

def move_roms(move_from, move_to):
    print('starting move...\n')
    start = time.perf_counter()
    os.chdir(move_from)
    cwd = os.getcwd()
    dst_dir = (move_to)
    os.makedirs('zip_files', exist_ok=True)

    if not os.path.isfile(fr'{cwd}/inventory.txt'):
        inventory = open('inventory.txt', 'a')
        inventory.close()

    if not os.path.isdir(move_to):
        os.makedirs(move_to)

    inventory_list = []

    for zip_file in os.listdir(cwd):
        if zip_file.startswith('.') or not zip_file.endswith('.zip'):
            continue
        
        shutil.copy(zip_file, cwd + '/zip_files')

        with zipfile.ZipFile(os.path.abspath(zip_file), 'r') as zip_ref:
            zip_ref.extractall(cwd)

        inventory_list.append(zip_file[:-4])
        

        os.remove(zip_file)

    inventory_list.sort()

    print('building inventory file...\n')
    with open('inventory.txt', 'a') as inventory:
        for title in inventory_list:
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