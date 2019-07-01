# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:15:24 2019

@author: amanr
"""
import os
import cv2

for person in range(1,320):
    for cam in range(1,3):
#        data_dir = os.path.join(, 'cam'+ cam , 'person' + %03i + person)
         data_dir = "./iLIDS-VID/i-LIDS-VID/sequences/cam" + str(cam) + "/person" + f"{person:03d}"
         if (os.path.exists(data_dir) == False):
             continue
         if os.path.exists(data_dir):
             save_dir = "./iLIDS-VID/i-LIDS-VID-OF-HVP/sequences/cam" + str(cam) + "/person" + f"{person:03d}"
             if (os.path.exists(save_dir) == False):
                 os.makedirs(save_dir)
        
         list_names = os.listdir(data_dir)
         prvs = cv2.imread(os.path.join(data_dir, list_names[0]), 0)
#         prvs = cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY)
         counter = 1
         while counter < len(list_names): 
              nxt = cv2.imread(os.path.join(data_dir, list_names[counter]), 0)
#              nxt = cv2.cvtColor(nxt, cv2.COLOR_BGR2GRAY)
#              prvs = (prvs/256).astype('uint8')
#              nxt = (nxt/256).astype('uint8')
              flow = cv2.calcOpticalFlowFarneback(prvs, nxt, None, 0.5, 3, 15, 3, 5, 1.2, 0)
              horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)
              vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
              horz = horz.astype('uint8')
              vert = vert.astype('uint8')
              prvs = nxt.copy()
              horz_path = 'opticalflow_horz' + str(counter) + '-' + str(counter+1) + '.pgm'
              vert_path = 'opticalflow_vert' + str(counter) + '-' + str(counter+1) + '.pgm'
              cv2.imwrite(os.path.join(save_dir, horz_path), horz)
              cv2.imwrite(os.path.join(save_dir, vert_path), vert)
              counter += 1



         
             
         