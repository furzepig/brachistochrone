import csv
import datetime

ifile = open('/home/john/bookdata/books.csv', "r")
reader = csv.reader(ifile)
print 'hello'
# initialization and declaration of variables
rownum = 0
readdate = 0
title = 0
author = 0
subtitle = 0
year = 1999

for row in reader:
    colnum = 0
    for col in row:
	
        if colnum == 0:
            title = col
        if colnum == 1:
            subtitle = col
        if colnum == 2:
            author = col
        if colnum == 3:
            readdate = col
	if colnum == 4:
            year = col
        colnum += 1

    imagename = "".join(item[0].lower() for item in title.split())

    filetitle=title.lower().replace(" ","_")
    print(readdate, author, title)
    filename=datetime.datetime.strptime(readdate, '%d/%m/%Y').strftime('%Y-%m-%d')+"-"+filetitle+".md"
    file = open("/home/john/furzepighub.io/_posts/books/"+year+"/"+filename,"w") 
    file.write("---\n") 
    file.write("layout: book\n") 
    file.write("category: book\n") 
    file.write("title: " + title + "\n")
    file.write("subtitle: " + subtitle + "\n")
    file.write("author: " + author + "\n")
    file.write("year: " + year + "\n")
    file.write("image: " + imagename + ".jpg\n")
    file.write("---\n") 
    file.close() 

    # time to go after the next row/bar
    rownum += 1

ifile.close()
