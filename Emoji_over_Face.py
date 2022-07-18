# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:49:45 2022

@author: SaadMuzammil
"""

 def blushing(self, filename):
     def blush(file_name):
         #load image
         image = cv.imread(file_name)
         image = image.copy()
         
         
         #convert image to grayscale image
         gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
         
         #read the harr_face_detect_classifier.xml
         harr_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
         
         face_cords = harr_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5 )
         print(face_cords)
         back = Image.open(file_name)
         front = Image.open("emoji.png")   #take any image of emoji from internet....
         
         back_image = back.copy()
         for x, y, w, h in face_cords:
             
             front = front.resize((w,h))
             mask_im = Image.new("L", front.size, 0)
             draw = ImageDraw.Draw(mask_im)
             draw.ellipse((2, 2, w-2, h-2), fill=255)
             mask_im.save('masked.jpg', quality=95)
             back = Image.open(file_name)
             back_image.paste(front,(x,y), mask_im)
                 
             
         back_image.show()
         return back_image
     image = blush(str(file_name))
     folder = QFileDialog.getExistingDirectory(
          self,
          caption = 'Select a folder'
          )
     name = "/obfuscated"
     image.save(str(folder) + name +".jpeg")