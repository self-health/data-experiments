import os
import argparse
import sys
import json
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import io

# This uploads all files that are new or have been modified.

parser = argparse.ArgumentParser()

parser.add_argument("--dir", help="Directory with data files", type=str, nargs='?', const=1, default='./')

args = parser.parse_args()

if not os.path.exists('settings.yaml'):
    print 'You do not have access. Email jcalebgood@gmail.com.'
    sys.exit()

if os.path.exists('./file_registry.json'):
    with open('./file_registry.json') as data_file:
        file_registry = json.load(data_file)
else:
    print 'No registered files.'
    sys.exit()

# Delete data that is no longer there

for folder in file_registry['folders']:
    if not os.path.exists(args.dir+folder):
        file_registry['folders'].remove(args.dir+folder)

for file in file_registry['files']:
    if not os.path.exists(args.dir+file):
        file_registry['files'].remove(file)
        if file in file_registry['updates']:
            del file_registry['updates']

# Push files that are new or have been updated

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

for file in file_registry['files']:
    if file not in file_registry['updates']:
        modified_time = os.path.getmtime(args.dir+file)
        f = drive.CreateFile({"description":modified_time, "title":file,"parents": [{"kind": "drive#fileLink", "id":file_registry['google_drive_folder']}]})
        f.SetContentFile(args.dir+file)
        f.Upload()
        file_registry['updates'][file]=time.time()
    else:
        modified_time = os.path.getmtime(args.dir+file)
        recorded_time = file_registry['updates'][file]
        if modified_time != recorded_time:
            f = drive.CreateFile({"description":modified_time, "title":file,"parents": [{"kind": "drive#fileLink", "id":file_registry['google_drive_folder']}]})
            f.SetContentFile(args.dir+file)
            f.Upload()
            file_registry['updates'][file]=modified_time

file_registry = json.dumps(file_registry)
file_registry = unicode(file_registry, errors='replace')

with io.open('file_registry.json', 'w', encoding='utf-8') as f:
    f.write(file_registry)
