# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:48:40 2020

@author: SaadMuzammil
"""

def pixelating(self, filename):
     def pixelate(file_name):
         #load image
         image = cv.imread(file_name)
         
         #convert image to grayscale image
         gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
         
         #read the harr_face_detect_classifier.xml
         harr_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
         
         face_cords = harr_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5 )
         print(face_cords)
         image_1 = Image.open(file_name)
         
         image = Image.open(file_name)
         for x, y, w, h in face_cords:
         
             #load image
             
             croped_image = image_1.crop((x,y,x+w,y+h))
             croped_image.save("croped_image.jpeg")
             #Open Paddington
             
             img = Image.open("croped_image.jpeg")
             # Resize smoothly down to 16x16 pixels
             imgSmall = img.resize((5,5),resample=Image.BILINEAR)
             # Scale back up using NEAREST to original size
             result = imgSmall.resize(img.size,Image.NEAREST)
             image.paste(result,(x,y,x+w,y+h))
             
         # Save
         image.show()
         return image
     image = pixelate(str(file_name))
     folder = QFileDialog.getExistingDirectory(
           self,
           caption = 'Select a folder'
           )
     name = "/obfuscated"
     image.save(str(folder) + name +".jpeg")
