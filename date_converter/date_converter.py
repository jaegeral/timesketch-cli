# imports a file with a date in a given format each line and prints them out to two new files for the needed format

import datetime
import time

filename = 'input.txt'
fin=open(filename,'r')

datetimefile = open('datetime.txt','w')
timestampfile = open('timestamp.txt', 'w')

inputformat = '%Y-%m-%d %H:%M:%S'

# method to create the datetime
def convert_date_to_datetime(argument):
    argument  = argument.replace('Z', '')
    d = datetime.datetime.strptime(argument, '%Y-%m-%d %H:%M:%S')
    iso_date = d.isoformat()
    iso_date_new = iso_date + "+00:00"
    return  iso_date_new
# helper to create the timestamp
def convert_date_to_timestamp(argument):
    argument = argument.replace('Z', '')
    d = datetime.datetime.strptime(argument, '%Y-%m-%d %H:%M:%S')
    unixtime = time.mktime(d.timetuple())
    unix_print = int(unixtime)
    unix_print = unix_print*1000
    return unix_print

for line in fin:
    print line
    line = line.replace('\n', '')
    line = line.replace('\t', '')
    entry_unix_timestamp = convert_date_to_timestamp(line)
    entry_timestamp = convert_date_to_datetime(line)
    datetimefile.write(entry_timestamp)
    datetimefile.write("\n")
    timestampfile.write(str(entry_unix_timestamp))
    timestampfile.write("\n")

datetimefile.close()
timestampfile.close()