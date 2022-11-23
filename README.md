# Rom Nom

**Automates the downloading, unzipping, and moving of rom files from romsmania.**

![rom nom title screen](https://github.com/LenWinkler/Rom-nom/blob/master/screens/1.png)

**Given a set of (optional) filters and a URL for a certain system on romsmania (e.g. 'https://romsmania.cc/roms/nintendo') it 
uses Python3 and Selenium to control a Chrome browser and download every rom for that platform
into a specified directory.**

![rom nom downloading](https://github.com/LenWinkler/Rom-nom/blob/master/screens/2.png)

**It then copies the zip files to a backup directory, unzips each file and moves it to a
specified folder, and deletes the unnecessary files from the HD.**


TODO List:
- [ ] Comment Code
- [ ] Try to avoid issue with chrome and chromedriver version. Can webdriver run a
specific version of chrome if we tell it to?
- [ ] Can we eliminate the need for the browser window? Could it run in headless mode?
- [ ] Add list of default filters