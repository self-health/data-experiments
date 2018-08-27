import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json

# Caution when using this. This syncs your remote to match exactly with what is
# on the remote. Any files and folders that are not on the remote will be removed.

if os.path.exists('./file_registry.json'):
    with open('./file_registry.json') as data_file:
        file_registry = json.load(data_file)
else:
    print 'No registered files.'
    sys.exit()

local_files = set()

data = os.walk('data/')

for el in data:
    path = el[0]
    for item in el[2]:
        local_files.add((path+'/'+item).replace('//','/'))

# Delete all files that are not on the remote drive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': '\'' + file_registry['google_drive_folder'] + '\'' + " in parents and trashed=false"}).GetList()
remote_files = set()

for file in file_list:
    remote_files.add(file['title'])

removed_files = []

for file in local_files:
    if file not in remote_files:
        removed_files.append(file)
        os.remove(file)

# Delete all empty folders

removed_folders = set()

folders = os.walk('./data/')

while True:
    folders = list(os.walk('./data/'))
    prev = len(folders)
    remove = set()
    for folder in folders:
        if not len(folder[1]) and not len(folder[2]):
            remove.add(folder[0])

    if len(remove):
        for folder in remove:
            os.rmdir(folder)
            removed_folders.add(folder)
    else:
        break

print 'Removed files:'
for el in removed_files:
    print el

print '\nRemoved folders:'
for el in removed_folders:
    print el
