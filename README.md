# rom_script

This will eventually be a script that will download a bunch of roms from romsmania, unzip them, and send them to certain folders on a flash drive.

## List of TODOS (not necessarily in order, WIP):

- [x] Function that grabs download link from a rom detail page
- [x] Function that goes through all the roms on a page and calls the above function on each
- [ ] Once we reach the end of a page, go to next page
- [x] Download each zip file
- [ ] Send a copy of each zip file to a "backup" dir
- [ ] Unzip each file
- [ ] Go through all unzipped dirs, take name and add it to "inventory" file, move rom to flash drive
- [ ] Delete rom/zip files from HD (this could be done as they're copied or all at once at the end)
