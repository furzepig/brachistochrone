import os
import sys
import datetime

title = sys.argv[1]
print('hello')
# initialization and declaration of variables
sHome =os.getenv("HOME") 
sYear = str(datetime.datetime.today().year)
author = sys.argv[2]

imagename = "".join(item[0].lower() for item in title.split())
filetitle=title.lower().replace(" ","_")
filename=datetime.datetime.today().strftime('%Y-%m-%d')+"-"+filetitle+".md"
file = open(sHome+"/brachistochrone/_posts/books/" + sYear + "/" + filename,"w+") 
file.write("---\n") 
file.write("layout: book\n") 
file.write("category: book\n") 
file.write("title: " + title + "\n")
file.write("author: " + author + "\n")
file.write("year: " + sYear + "\n")
file.write("image: " + imagename + ".jpg\n")
file.write("---\n") 
file.close() 

