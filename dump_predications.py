import argparse
import mysql.connector
import codecs

#The expection is that you have already dumped the predications from the NLM
#The predications can be downloaded at https://skr3.nlm.nih.gov/SemMedDB/download/download.htmlself.
#I used the entire database file.

parser = argparse.ArgumentParser()

parser.add_argument("--out", help="Output directory for the file", type=str, nargs='?', const=1, default='./data/')
parser.add_argument("--db_name", help="Name of database.", type=str, nargs='?', const=1, default='SEMANTIC_MEDLINE')
parser.add_argument("--user", help="Database user name.", type=str, nargs='?', const=1, default='caleb')
parser.add_argument("--password", help="Database password.", type=str, nargs='?', const=1, default='password')
parser.add_argument("--host", help="Ip address.", type=str, nargs='?', const=1, default='127.0.0.1')

args = parser.parse_args()

cnx = mysql.connector.connect(user=args.user, password=args.password, host=args.host, database=args.db_name)
cursor = cnx.cursor()
cursor.execute("SELECT * FROM PREDICATION")

predications = []

row = cursor.fetchone()

while row is not None:
    relation = row[3]
    s = row[5]
    o = row[9]
    s_cui = row[4]
    o_cui = row[8]
    s_type = row[6]
    o_type = row[10]

    predications.append(s + '\t' + relation + '\t' + o + '\t' + s_cui + '\t' + o_cui + '\t' + s_type + '\t' + o_type)

    row = cursor.fetchone()

predications = [unicode(el, errors='replace') for el in predications]

f_out = codecs.open(args.out+'all_predications.txt', 'w', encoding='utf-8')
f_out.write('\n'.join(predications))
f_out.close()
