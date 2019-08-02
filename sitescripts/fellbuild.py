import csv
import datetime

ifile = open('/home/john/bookdata/fells.csv', "r")
reader = csv.reader(ifile)
print 'hello'
# initialization and declaration of variables
rownum = 0
readdate = 0
name = 0
height = 0
number = 0
filetitle = 0

for row in reader:
    colnum = 0
    for col in row:
	
        if colnum == 0:
            number = col
        if colnum == 1:
            name = col
        if colnum == 2:
            height = col
        colnum += 1

    filetitle=name.lower().replace(" ","_")
    filetitle=filetitle.replace("'","_")
    filetitle=filetitle.replace("(","_")
    filetitle=filetitle.replace(")","_")
    filetitle=filetitle.replace("[","_")
    filetitle=filetitle.replace("]","_")
    print(number, name, height)
    filename="1900-01-01-" + filetitle + ".md"
    file = open("/home/john/brachistochrone/_posts/fells/"+filename,"w") 
    file.write("---\n") 
    file.write("layout: fell\n") 
    file.write("category: fells\n") 
    file.write("name: " + name + "\n")
    file.write("number: " + number + "\n")
    file.write("height: " + height + "\n")
    file.write("climbed: No\n")
    file.write("---\n") 
    file.close() 

    # time to go after the next row/bar
    rownum += 1

ifile.close()
