from GPSPhoto import gpsphoto
import os
import glob
import csv

img_dir = 'E:/AvocadoTrees/DJI/13-02-2020/vuelo1/'
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)

fields = ('Latitude', 'Longitude', 'Altitude')
f = open("spdata_vuelo1.csv", "w")
w = csv.writer(f, lineterminator='\n')
data = []
w.writerow(['Filename', 'Latitude', 'Longitude', 'Altitude'])
for i, f1 in enumerate(files):
    data1 = gpsphoto.getGPSData(f1)
    filename = files[i][len(img_dir):]
    w.writerow([filename, data1['Latitude'], data1['Longitude'], data1['Altitude']])
f.close()

