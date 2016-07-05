# -*- coding: utf-8 -*-


import numpy as np
import cv2

class ColorDescriptor:
     def __init__(self,bins):
        ##image=cv2.imread('jlaw2.jpg')
        self.bins=bins
         
     def describe(self,image):
        feature=[]
        img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        (h,w)=img.shape[:2]
        (cx,cy)=(int(w*0.5),int(h*0.5))
        ##print h,w
        segments=[(0,cx,0,cy),(cx,w,0,cy),(cx,w,cy,h),(0,cx,cy,h)]
        (axesx,axesy)=(int(w*0.75)/2,int(h*0.75)/2)
        emask=np.zeros(img.shape[:2],dtype = np.uint8)
        cv2.ellipse(emask,(cx,cy),(axesx,axesy),0,0,360,255,-1)
        ##print emask 
        for (startx,endx,starty,endy) in segments:
            cornermask=np.zeros(img.shape[:2],dtype = np.uint8)
            cv2.rectangle(cornermask,(startx,starty),(endx,endy),255,-1)
            cornermask=cv2.subtract(cornermask,emask)
            
            hist=self.histogram(image,cornermask)
            feature.extend(hist)
        hist=self.histogram(image,emask)
        feature.extend(hist)
        
        return feature
        
        
     def histogram(self,image,mask):
            
            hist=cv2.calcHist([image],[0,1,2],mask,self.bins,[0,180,0,256,0,256])
            hist=cv2.normalize(hist).flatten()
            return hist
