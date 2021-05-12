import os
import sys
import datetime


os.system('git pull origin master')
title = sys.argv[1]
print('Making Hurlant ...')
# initialization and declaration of variables
sHome =os.getenv("HOME") 
sYear = str(datetime.datetime.today().year)
imagename = "".join(item[0].lower() for item in title.split())
filetitle=title.lower().replace(" ","_")
filename=datetime.datetime.today().strftime('%Y-%m-%d')+"-"+filetitle+".md"
file = open(sHome+"/brachistochrone/_posts/hurlant/"  + filename,"w+") 
file.write("---\n") 
file.write("layout: hurlant\n") 
file.write("category: hurlant\n") 
file.write("title: " + title + "\n")
file.write("---\n") 
file.close() 
print('Made hurlant:')
print(file.name)
os.system('git add ' + file.name)
os.system('git commit -m "added ' + title + '"')
os.system('git push')
