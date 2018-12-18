import os
import sys

title = sys.argv[1]
bigImage ="/brachistochrone/images/books/2018/" + title
smlImage ="/brachistochrone/images/books/2018/small" + title
print('Shrinking ' + bigImage + ' to ' + smlImage)
os.system('convert -resize 50% ' + bigimage + ' ' + smlImage
os.system('git add ' + smlImage)
os.system('git commit -m "added ' + title + '"')

