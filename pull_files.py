import os
import argparse
import sys
import json
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import io
from datetime import datetime

# This simply checks the data folder for needed files. If they are not present it downloads them.
# The force flag will replace all files.

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def download_file(file):
    if os.path.exists(file['title']):
        os.remove(file['title'])
    new_file = drive.CreateFile({'id': file['id']})
    new_file.GetContentFile(file['title'])

if not os.path.exists('settings.yaml'):
    print 'You do not have access. Email jcalebgood@gmail.com.'
    sys.exit()

file_list = drive.ListFile({'q': '\'' + file_registry['google_drive_folder'] + '\'' + " in parents and trashed=false"}).GetList()
files = []

for file in file_list:
    files.append(file)

# Create directory structure

for file in files:
    file_name = file['title']
    if '/' in file_name:
        file_name = file_name.split('/')
        file_name = file_name[0:-1]
        for i in range(len(file_name)+1):
            path = file_name[0:i]
            if len(path):
                path = '/'.join(path)
                if not os.path.exists(path):
                    os.mkdir(path)

# Pull files that are new or have been updated

for file in files:
    if not os.path.exists(file['title']):
        download_file(file)
    else:
        remote_time = float(file['description'])
        disk_time = os.path.getmtime(file['title'])
        if remote_time > disk_time:
            download_file(file)
