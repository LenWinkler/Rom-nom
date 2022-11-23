import os
import shutil
import time
import zipfile

from rich.console import Console
from rich.text import Text


def move_roms(move_from, move_to):
    console = Console()
    console.print(Text.assemble(("\nStarting move 🚚💨💨\n\n", "bold green")))
    start = time.perf_counter()
    os.chdir(move_from)
    cwd = os.getcwd()
    # Create a zip_files dir, if it doesn't already exist
    os.makedirs('zip_files', exist_ok=True)

    # Create unzip location if it doesn't already exist
    if not os.path.isdir(move_to):
        os.makedirs(move_to)

    for zip_file in os.listdir(cwd):
        if zip_file.startswith('.') or not zip_file.endswith('.zip'):
            continue
        
        shutil.copy(zip_file, cwd + '/zip_files')

        with zipfile.ZipFile(os.path.abspath(zip_file), 'r') as zip_ref:
            zip_ref.extractall(cwd)

        os.remove(zip_file)

    if move_from != move_to:
        console.print(Text.assemble(("Copying files to ", "bold green"), 
                                    (move_to, "bold"), "\n"))
        for item in os.listdir(cwd):
            if (
                item == 'zip_files' 
                or item == 'inventory.txt' 
                or os.path.isdir(item)
            ):
                continue
            shutil.copy(item, move_to)
            os.remove(item)

    end = time.perf_counter()
    print(f'Move completed in {end - start:0.2f} seconds\n')
