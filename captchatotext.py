import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import jesus

#create model
model = Sequential()
#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(40,30,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(150, activation='relu'))
model.add(Dense(26, activation='softmax'))
#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#import read_caltech
#files1,X_train, y_train = read_caltech.get_data_mat('hooroof')
model.load_weights("model.h5")
import cv2
path="id.jpg"


def getchar(num):
    return chr(num+97).upper()
    

def getharf(img):
    X_train=np.array([img])
    X_train=np.expand_dims(X_train, axis=-1)
    predicted=list(model.predict(X_train)[0])
    return getchar(predicted.index(max(predicted)))
    #print(predicted)
    #print(X_train.shape)

def remove_noise(image):
    return cv2.medianBlur(image,3)
def canny(image):
    return cv2.Canny(image, 100, 200)

def karkhune(img):
    th, img = cv2.threshold(img, 110, 255, cv2.THRESH_TOZERO)
    th, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)        
    img = remove_noise(img)
    kernel1 = np.ones((2,2),np.uint8)
    kernel2 = np.ones((2,2),np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = remove_noise(img)
    img = cv2.dilate(img,kernel1,iterations = 1)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel2)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel2)
    img = canny(img)
    img = 255-img
    
    return img


def output(path):
    img = cv2.imread(path)
    img=karkhune(img)
    kk=""
    for i in range(5):
        imgs=img[:,30*i:30*(i+1)]
        #cv2.imshow(str(i),imgs)
        #imgs=imgs[:,:,1]
        word = getharf(imgs)
        kk+=word
        #print(imgs.shape)
        #cv2.imwrite("hooroof/"+word[i]+"_"+str(random.randint(0,1000))+".jpg",imgs)
        #cv2.imshow(str(i),imgs)
    return kk
def readit():
    jesus.getss()
    cv2.imshow("asd",cv2.imread("id.jpg"))
    print(output("id.jpg"))
