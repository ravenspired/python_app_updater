#Automatic software updater for apps python script
#Compiled by: Anton Voronov, Raven Development

import urllib.request, filecmp, sys, os


#Download check for updates file
print("Checking for updates...")
urllib.request.urlretrieve ("http://raven-development-update-server--antonvoronov.repl.co/software/update/sample/sampleupdate.txt", "sampleupdate.txt")


#Compare it with existing file
files = filecmp.cmp('originalupdate.txt', 'sampleupdate.txt')

#Invert outputted value (for simplicities' sake)
needup = 0
if files == True:
    needup = False
else:
    neepup = True

#Update if neccesary
if needup == True:
    print("Updating Software...")
    urllib.request.urlretrieve ("http://raven-development-update-server--antonvoronov.repl.co/software/download/sample/sample.py", "sample.py")
    os.remove("originalupdate.txt")
    os.rename("sampleupdate.txt", "originalupdate.txt")
    os.remove("run.py")
    os.rename("sample.py", "run.py")


else:
    print("Up to date.")
    os.remove("sampleupdate.txt")

import run