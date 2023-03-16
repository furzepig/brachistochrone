import csv
import datetime

ifile = open('/home/john/bookdata/gamebooks.csv', "r")
reader = csv.reader(ifile)
print('hello')
# initialization and declaration of variables
rownum = 0
readdate = 0
title = 0
author = 0
subtitle = 0
year = 1999
readdate = 2023

for row in reader:
    colnum = 0
    for col in row:
	
        if colnum == 0:
            title = col
        if colnum == 1:
            series = col
        if colnum == 2:
            year = col
        if colnum == 3:
            index = col
        colnum += 1

    if ( len(title.split())>1 ):
      imagename = "".join(item[0].lower() for item in title.split())
    else:
      imagename = title

    filetitle=title.lower().replace(" ","_")
    filename="2023-03-10-"+filetitle+".md"
    file = open("/home/john/brachistochrone/_posts/gamebooks/"+filename,"w") 
    file.write("---\n") 
    file.write("layout: gamebook\n") 
    file.write("category: gamebooks\n") 
    file.write("title: " + title + "\n")
    file.write("type: " + "campaign" + "\n")
    file.write("series: " + series + "\n")
    file.write("year: " + year + "\n")
    file.write("index: " + index + "\n")
    file.write("image: " + imagename + ".jpg\n")
    file.write("---\n") 
    file.close() 

    # time to go after the next row/bar
    rownum += 1

ifile.close()
