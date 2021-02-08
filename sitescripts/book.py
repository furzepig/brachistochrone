import os
import sys
import datetime


os.system('git pull origin master')
title = sys.argv[1]
print('Making book ...')
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
file.write("category: books\n") 
file.write("title: " + title + "\n")
file.write("author: " + author + "\n")
file.write("year: " + sYear + "\n")
file.write("image: " + imagename + ".jpg\n")
file.write("---\n") 
file.close() 
print('Made book:')
print(file.name)
print('Image name is: ' + imagename + '.jpg')
os.system('git add ' + file.name)
os.system('git commit -m "added ' + title + '"')
os.system('git push')
