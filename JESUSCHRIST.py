import cv2
import numpy as np
import os
import random

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,3)
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def get_data_mat(dir):
    X = []
    y = []
    filenames=[]
    k=0
    files = os.listdir(dir)
    random.shuffle(files)
    for file in files:
        if file[-3:] == 'jpg':
            word = file[-9:][:5]
            print(word)
            img = cv2.imread(os.path.join(dir, file))
            #1_Thresholding
            th, img = cv2.threshold(img, 110, 255, cv2.THRESH_TOZERO)
            th, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)
            
            
            img = remove_noise(img)
            kernel1 = np.ones((2,2),np.uint8)
            kernel2 = np.ones((2,2),np.uint8)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("1)black and whited",img)
            img = remove_noise(img)
            
            img = cv2.dilate(img,kernel1,iterations = 1)
            cv2.imshow("2)dilated",img)            
            #img = cv2.erode(img,kernel1,iterations = 1)
            #cv2.imshow("2)eroded",img)
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel2)
            cv2.imshow("3)opened",img)
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel2)
            cv2.imshow("4)closed",img)
            
            #print(img.shape)
            img = canny(img)
            cv2.imshow("6)canny",img)
            img = 255-img 
            cv2.imshow("7)img",img)
            for i in range(5):
                imgs=img[:,30*i:30*(i+1)]
                cv2.imwrite("hooroof/"+word[i]+"_"+str(random.randint(0,4000))+".jpg",imgs)
                #cv2.imshow(str(i),imgs)
                
            #return
            
            #cv2.imwrite("captchas2/"+file,img)    
            continue
        
            img = img.reshape((img.shape[0]*img.shape[1],))
            img = img / 255.
            X.append(img)
            if(file[0]=='f'):
                y.append([0,1])

            else :
                y.append([1,0])
            
            #y.append(0 if file[0] == 'f' else 1)

            filenames.append(file)
    print(len(y))
    print("done")
    return
    return filenames,np.array(X,dtype=np.float32), np.array(y)#,dtype=object)

#files,X,y=get_data_mat("test/")
get_data_mat("captchas")
