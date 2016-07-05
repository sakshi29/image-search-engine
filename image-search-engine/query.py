# -*- coding: utf-8 -*-

import numpy as np
import cv2
import csv

class Searcher:
      def __init__(self,indexpath):
          self.indexpath=indexpath
      def search(self,queryFeat,limit=3):
          results={}
          with open(self.indexpath) as f:
               reader= csv.reader(f)
               for row in reader:
                   feature=[float(x) for x in row[1:]]
                   d=self.chi2_distance(feature,queryFeat)
                   results[row[0]]=d
               f.close()    

          results=sorted([(v,k) for (k,v) in results.items()]) 
          return results[:limit]            
      def chi2_distance(self,hista,histb,eps=1e-10):
            d=0.5*np.sum([((a-b)**2)/(a+b+eps)
            for (a,b) in zip(hista,histb)])
                
            return d    
                
