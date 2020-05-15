#@authors: John Hernandez,Naomy Morales, Luis Diaz

import csv
import shutil
from tempfile import NamedTemporaryFile

#Creating a CSV file
def create_graph():
    with open('data.csv','w',newline='') as csv_file:
        fieldnames=['first_town','second_town','distance','speed']
        csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        csv_writer.writeheader()
#Creating a graph using towns of Puerto Rico
#The distance is based on miles and the speed is the maximum speed.
        csv_writer.writerow({'first_town':'Arecibo','second_town':'San Juan','distance':59,'speed':45})
        csv_writer.writerow({'first_town': 'San Juan', 'second_town': 'Fajardo', 'distance': 37, 'speed': 45})
        csv_writer.writerow({'first_town': 'San Juan', 'second_town': 'Caguas', 'distance': 19, 'speed': 40})
        csv_writer.writerow({'first_town': 'San Juan', 'second_town': 'Mayaguez', 'distance': 99, 'speed': 65})
        csv_writer.writerow({'first_town': 'Caguas', 'second_town': 'Ponce', 'distance': 54, 'speed': 60})
        csv_writer.writerow({'first_town': 'Caguas', 'second_town': 'Cayey', 'distance': 15, 'speed': 60})
        csv_writer.writerow({'first_town': 'Fajardo', 'second_town': 'Ponce', 'distance': 64, 'speed': 60})
        csv_writer.writerow({'first_town': 'Mayaguez', 'second_town': 'Ponce', 'distance': 49, 'speed': 60})
        csv_writer.writerow({'first_town': 'Mayaguez', 'second_town': 'Cabo Rojo', 'distance': 9, 'speed': 50})
        csv_writer.writerow({'first_town': 'Rincon', 'second_town': 'Arecibo', 'distance': 53, 'speed': 50})
        csv_writer.writerow({'first_town': 'Rincon', 'second_town': 'Mayaguez', 'distance': 14, 'speed': 50})
        csv_writer.writerow({'first_town': 'Cabo Rojo', 'second_town': 'Ponce', 'distance': 46, 'speed': 50})

#Reading a CSV file
def read_csv_file(file='data.csv'):
    with open(file,'r') as csv_file:
        reader=csv.DictReader(csv_file)
        for line in reader:
            print(line)

def get_length(file_path='data.csv'): #allows you to get the length of a csv file
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        readerlist=list(reader)

    return len(readerlist)

#Appending new data
def adding_data(file_path,town,secondtown,distance,speed):
    fieldnames=['first_town','second_town','distance','speed']
    with open('data.csv','a') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({ 'first_town':town,'second_town':secondtown,'distance':distance,'speed':speed })

#Updating data
def edit_data(file_path='data.csv',editfirst_town=None,editsecond_town=None,editdistance=None,editspeed=None):

    filename=file_path
    tempfile=NamedTemporaryFile(delete=False)
    with open(filename,'rb') as csvfile,tempfile:
        reader=csv.DictReader(csvfile)
        fieldnames=['first_town','second_town','distance','speed','optimized']
        this_writer=csv.DictWriter(tempfile,fieldnames=fieldnames)
        this_writer.writeheader()
        for row in reader:
            if editfirst_town is not None:
                if str(row['first_town'])==str(editfirst_town):
                    row['distance']=editdistance
                    row['speed']=editspeed
            elif editsecond_town is not None and editfirst_town is None:
                if str(row['second_town'])==str(editsecond_town):
                    row['distance'] = editdistance
                    row['speed'] = editspeed
            else:
                pass
            this_writer.writerow(row)

        shutil.move(tempfile.name, filename)
        return True
    return False



