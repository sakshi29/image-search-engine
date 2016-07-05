

from colorDesciptor import ColorDescriptor
from query import Searcher
import cv2
cd=ColorDescriptor((8,12,3))
query=cv2.imread('download.jpg')

feature=cd.describe(query)
searcher=Searcher('D:/image processing/image-search-engine/output1.csv')
results=searcher.search(feature)

cv2.imshow('query',query)

for (score,resultid) in results:
    results=cv2.imread('D:/image processing/image-search-engine'+'/'+resultid)
    cv2.imshow('result',results)
    cv2.waitKey(0)
