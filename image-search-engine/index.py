# -*- coding: utf-8 -*-


from colorDesciptor import ColorDescriptor
import cv2
import glob
cd=ColorDescriptor((8,12,3))

output=open('output1.csv', 'w+')
for imagepath in glob.glob('D:/image processing/image-search-engine/testimages/*'):
    imageID=imagepath[imagepath.rfind("/")+1:]
    image=cv2.imread(imagepath)
    
    feature=cd.describe(image)
    
    feature=[str(f) for f in feature]
    output.write("%s,%s\n" % (imageID,",".join(feature)))
output.close()    
