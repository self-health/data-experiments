import os
import argparse
import sys

# This simply checks the data folder for needed files. If they are not present it downloads them.
# The force flag will replace all files.

parser = argparse.ArgumentParser()

parser.add_argument("--dir", help="Directory with data files", type=str, nargs='?', const=1, default='./data/')
parser.add_argument("--force", help="Force download of all files", type=bool, nargs='?', const=1, default=False)

args = parser.parse_args()

if not os.path.exists('settings.yaml'):
    print 'You do not have access. Email jcalebgood@gmail.com.'
    sys.exit()

if not os.path.exists(args.dir):
    os.mkdir(args.dir)

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
