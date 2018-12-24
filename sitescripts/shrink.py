import os
import sys
sHome=os.getenv("HOME")
title = sys.argv[1]
bigImage=sHome+"/brachistochrone/images/books/2018/"+title
smlImage=sHome+"/brachistochrone/images/books/2018/small/"+ title
print('Shrinking ' + bigImage + ' to ' +smlImage)
os.system('convert -resize 50% '+bigImage + ' ' + smlImage)
os.system('git add ' + smlImage)
os.system('git commit -m "added ' + title + '"')

