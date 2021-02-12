from download import download_roms
from move import move_roms

url = input('Enter the romsmania url:\n')
file_destination = input('Where should the files be saved? (file path)\n')

download_roms(url, file_destination)