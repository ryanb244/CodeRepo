import os
import shutil
import send2trash
import csv

"""
f = open('practice.txt', 'w+')

f.write('This is a test string')

f.close()

print(os.getcwd())

print(os.listdir('C:\\Users'))


shutil.move(
    'C:\\Users\\Ryan\\Google Drive\\CodeRepo\\DEVASC-ENAUTO\\practice.txt', os.getcwd())


send2trash.send2trash('practice.txt')



with open("textfile.txt", "w+") as file:
    file.write('Like omg I am a file \n like woah my god I am Ryan \n like woah')

with open("textfile.txt", "r") as data:
    print(data.read())

"""

"""samplefile = open('routerlist.csv')
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)

print(sampledata)"""

with open("routerlist.csv") as data:
    csv_list = csv.reader(data)

    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]

        print(f"{device} is in {location.rstrip()} and has IP {ip}.")
