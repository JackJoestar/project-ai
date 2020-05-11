import csv
import shutil
from tempfile import NamedTemporaryFile

#Creating a CSV file
with open('data.csv','w',newline='') as csv_file:
     fieldnames=['first_town','second_town','distance','speed']
     csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
     csv_writer.writeheader()

     csv_writer.writerow({'first_town':'Arecibo','second_town':'San Juan','distance':20,'speed':45})
     csv_writer.writerow({'first_town': 'San Juan', 'second_town': 'Fajardo', 'distance': 20, 'speed': 45})
     csv_writer.writerow({'first_town': 'San Juan', 'second_town': 'Caguas', 'distance': 10, 'speed': 40})
     csv_writer.writerow({'first_town': 'San Juan', 'second_town': 'Mayaguez', 'distance': 60, 'speed': 65})
     csv_writer.writerow({'first_town': 'Caguas', 'second_town': 'Ponce', 'distance': 20, 'speed': 60})
     csv_writer.writerow({'first_town': 'Caguas', 'second_town': 'Cayey', 'distance': 0, 'speed': 0})
     csv_writer.writerow({'first_town': 'Fajardo', 'second_town': 'Ponce', 'distance': 0, 'speed': 0})
     csv_writer.writerow({'first_town': 'Mayaguez', 'second_town': 'Ponce', 'distance': 50, 'speed': 60})
     csv_writer.writerow({'first_town': 'Mayaguez', 'second_town': 'Cabo Rojo', 'distance': 0, 'speed': 0})
     csv_writer.writerow({'first_town': 'Rincon', 'second_town': 'Arecibo', 'distance': 0, 'speed': 0})
     csv_writer.writerow({'first_town': 'Rincon', 'second_town': 'Mayaguez', 'distance': 0, 'speed': 0})
     csv_writer.writerow({'first_town': 'Cabo Rojo', 'second_town': 'Ponce', 'distance': 0, 'speed': 0})

#Reading a CSV file
with open('data.csv','r') as csv_file:
    reader=csv.DictReader(csv_file)
    for line in reader:
        print(line)

def get_length(file_path):
    with open('data.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        readerlist=list(reader)

    return len(readerlist)

#Appending new data
def adding_data(file_path,town,secondtown,distance,speed):
    fieldnames=['first_town','second_town','distance','speed']
    next_value=get_length(file_path)
    with open(file_path,'a') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({ 'first_town':town,'second_town':secondtown,'distance':distance,'speed':speed })

#Updating data
def edit_data(editfirst_town=None,editsecond_town=None,editdistance=None,editspeed=None):

    filename="data.csv"
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



