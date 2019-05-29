#Automatic software updater for apps python script
#Compiled by: Anton Voronov, Raven Development

import urllib.request, filecmp, sys, os, time


#Download check for updates file
print("Checking for updates...")
urllib.request.urlretrieve ("http://example.com/yourupdatetestfile.txt", "sampleupdate.txt")


#Compare it with existing file
files = filecmp.cmp('originalupdate.txt', 'sampleupdate.txt', shallow=False)



#Update if neccesary
if files == False:
    print("Updating Software...")
    time.sleep(2)
    urllib.request.urlretrieve ("http://example.com/youupdatedscript.script", "sample.py")
    os.remove("originalupdate.txt")
    os.rename("sampleupdate.txt", "originalupdate.txt")
    os.remove("run.py")
    os.rename("sample.py", "run.py")


else:
    print("Up to date.")
    os.remove("sampleupdate.txt")

import run
