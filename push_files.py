import os
import argparse
import sys
import json

# This simply checks the data folder for needed files. If they are not present it downloads them.
# The force flag will replace all files.

parser = argparse.ArgumentParser()

parser.add_argument("--dir", help="Directory with data files", type=str, nargs='?', const=1, default='./')
parser.add_argument("--mode", help="Select operation. Force = Replace all files. Update = Fetch files you don't have.", type=str, nargs='?', const=1, default='update')

args = parser.parse_args()

if not os.path.exists('settings.yaml'):
    print 'You do not have access. Email jcalebgood@gmail.com.'
    sys.exit()

if os.path.exists('./file_registry.json'):
    with open('./file_registry.json') as data_file:
        file_registry = json.load(data_file)

for folder in file_registry['folders']:
    if not os.path.exists(args.dir+folder):
        os.mkdir(args.dir+folder)


# try:
#     f = open('password.txt','r')
#     password = f.read()
#     password = password.strip()
# except IOError:
#     print 'You do not have access. Email jcalebgood@gmail.com.'
#     sys.exit()

# if not os.path.exists(args.dir):
#     os.mkdir(args.dir)

#import os
# os.mkdir(path)

# import zipfile
# zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
# zip_ref.extractall(directory_to_extract_to)
# zip_ref.close()

# data = data.split('\n')
#
# print os.path.exists(args.dir+'all_predications.txt')

#print args.dir
#print args.force
