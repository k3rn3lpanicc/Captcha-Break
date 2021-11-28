# Captcha-Break
Using AI to break University's Login page captcha.

# How does login page work ?
Well i keep tracking the requests wich were sent from my pc to university's login page and noticed that it used a cookie named : JSESSIONID to keep track of user session.

# The Captcha Generator
Each Captcha is a 5 character word that uses only english uppercase alphabet. And while the JSESSIONID remains same , the generated captcha will be same text with different noise and rotations on it.
so i used this to gather data and automatically label them.

# Gathering Data and labeling them
I wrote a python script that sends a request to load login page and get's JSESSIONID from it and uses it to get one image from captcha generator. then it asks me to label it and after that it would automatically download 30 more 
captchas (that are the same in text) and labels them automatically . then we go for second captcha and more 30 images and so on. 
With this method i gathered aroun 2000 images that were labeled.

# Preprocessing part
I used Opencv library in python to do some preprocessing before using CNN . First I did 2 thresholds on input captcha image (a TOZERO and a BINARY_INV) , then i used median blur to remove some noise from it.
after that i turned it into black and white picture and after that used median blur to denoise it once more. then i used a delation to make noise lines thiner to use openning on them and remove them.
after opening we do a closing to make it back to it's natural size and we do a canny edge detection on them and inverse the output image . 
The out put of this whole process is something like this: 
Before Pre-Processing : ![Captchas before Preprocessing](https://dl.dropboxusercontent.com/s/t1idg5igqjb810i/0B222A9756B5822F495B04F93A76C049_22_UHMXM.jpg?dl=0)
After Pre-Processing : ![After](https://dl.dropboxusercontent.com/s/dudesuy0i6pd7fn/0A11D1818BFD488783C04974D9019DCE_2_RPRWW.jpg?dl=0)

After Doing this Preprocessing , I cut each image into 5 equal slices (each slice would have a char in it) and automatically labeled and saved them as my training data.
sofar we have 2000 * 5 = 10000 characters to train out CNN on them.

# Training 
I used Keras Library and made a CNN Model and this is the structur of it :
Model: sequential    
'      conv2d (Conv2D)      64Filters with kernel of 2        (None, 38, 28, 64)            
'      conv2d_1 (Conv2D)    32Filters with kernel of 2        (None, 36, 26, 32)            
'      flatten (Flatten)            (None, 29952)                    
'      dense (Dense)                (None, 150)                 
'      dense_1 (Dense)              (None, 26)                     

'      Total params: 4,515,980
'      Trainable params: 4,515,980
'      Non-trainable params: 0
      
I Trained it with Input Images (that were single characters) and after about 10 epochs , the acurasy get to 1 (100%)

# Building it up together
So i did all of it , now it was the time to gatherup all the parts into one single code.
so in "captchatotext.py" i used all the steps and simply by typing : readit() , it would download a new captcha from the university's login page and breaks it and shows the captchas text to me.

Picture of readit() function : ![Working Fine](https://dl.dropboxusercontent.com/s/hsjjrex9usx9y7b/capt.jpg?dl=0)
