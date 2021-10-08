import cv2
import numpy as np
import os
import random
def getnum(v):
	v=v.lower()
	return ord(v)-97
def get_data_mat(dir):
    X = []
    y = []
    filenames=[]
    k=0
    files = os.listdir(dir)
    random.shuffle(files)
    for file in files:
        if file[-3:] == 'jpg':
            img = cv2.imread(os.path.join(dir, file))
            
            img = img[:,:,0]
            #print(img.shape)
            #img = img.reshape((img.shape[0],img.shape[1],1))
            img = img / 255.
            X.append(img)
            row = [0 for p in range(26)]
            row[getnum(file[0])]=1
            y.append(row)
            filenames.append(file)
    print(len(y))
    return filenames,np.array(X,dtype=np.float32), np.array(y)#,dtype=object)

#files,X,y=get_data_mat("test/")
#get_data_mat("hooroof")
