# Rom Nom

I wrote this to automate the downloading, unzipping, and moving of rom files from romsmania.

Given a URL for a certain system on romsmania (e.g. 'https://romsmania.cc/roms/nintendo') it 
uses Python3 and Selenium to control a Chrome browser and download every rom for that platform
into a specified directory.

It then copies the zip files to a backup directory, unzips each file and moves it to a
specified folder, and deletes the unnecessary files from the HD.
