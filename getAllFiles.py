# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:47:54 2019

@author: Saqlain
"""

import glob
import pandas as pd
import os
import urllib
import cv2
import numpy as np
import requests

allFiles=glob.glob('dataset/vgg_face_dataset/vgg_face_dataset/files/*.txt')
length=len(allFiles)
i=0
while i <length:
    i=i+1
    file=pd.read_csv(allFiles[i],sep=' ' ,names=["id","url","left","top","right","bottom","pose","detection score","curation"])
    linksOfImages=file['url']
    lengthOfLinks=len(linksOfImages)
    j=0
    allFiles[i] = allFiles[i].replace(".txt", "")
    print("getting data for : : : : ", allFiles[i])
    
    pathForFolders=allFiles[i]+"/"+"*.jpg"
    readFiles=glob.glob(pathForFolders)
    lengthOfFiles=len(readFiles)
    if lengthOfFiles < 200:
        print("getting data for ::: ", allFiles[i]) 
        try:
            os.mkdir(allFiles[i])
            print("created")
        except:
            print("error")
        finally:
            print("Succeded")
            
        pathForFolders=allFiles[i]+"/"+"*.jpg"
        readFiles=glob.glob(pathForFolders)
        length=len(allFiles)
        
        j=lengthOfFiles
        print("files existed :::: ", j)
        while j < lengthOfLinks:
            path=allFiles[i]+"/"+str(j)+".jpg"
            
            image_url = linksOfImages[j]
            if "nfs.celebrityphoto.com" in image_url or "images.cinemaring.com" in image_url or "cdn7.staztic.com" in image_url:
                print("skipping due to websites connection failure")
            else:
                try:
    #        r = requests.get(url, allow_redirects=True)
    #        open(path, 'wb').write(r.content)
    #        urllib.request.urlretrieve(linksOfImages[j], path)
    #        image = urllib.URLopener()
    #        image.retrieve(linksOfImages[j],path)
    #        urllib.request.urlretrieve(linksOfImages[j], path)
    #        resp = urllib.request.urlopen(linksOfImages[j])
    #        image = np.asarray(bytearray(resp.read()))
    
    #        cv2.imwrite(path, image)
            
      
    # URL of the image to be downloaded is defined as image_url 
                    r = requests.get(image_url) # create HTTP response object 
      
    # send a HTTP request to the server and save 
    # the HTTP response in a response object called r 
                    with open(path,'wb') as f: 
              
                # Saving received content as a png file in 
                # binary format 
              
                # write the contents of the response (r.content) 
                # to a new file in binary mode. 
                        f.write(r.content)
                        print("image number ,::: ", j)
                except:
                    print("website issues")
                finally:
                    print("i should fetch next file")
            j=j+1   
                 
    else:
        print("already exist  :: : ", allFiles[i])
    
    
    
