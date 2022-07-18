# -*- coding: utf-8 -*-
"""
Created on Mon Jul 0 14:54:15 2020

@author: SaadMuzammil
"""

 def video_pixelating(self, filename):
     def video_pixelate(file_name):
         # Load the cascade  
         face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')  
         # To capture video from webcam.   
         cap = cv.VideoCapture(file_name) 
         frame_width = int(cap.get(3))
         frame_height = int(cap.get(4))
         size = (frame_width, frame_height)
         result = cv.VideoWriter('obfuscated_video.avi', 
                              cv.VideoWriter_fourcc(*'MJPG'),
                              10, size)  
         # To capture video from webcam.   
         cap = cv.VideoCapture(file_name)  
           
         while True:  
             # Read the frame  
             _, img = cap.read()
             
             
             
             # Convert to grayscale  
             gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
           
             # Detect the faces  
             faces = face_cascade.detectMultiScale(gray, 1.1, 4)
           
             # Draw the rectangle around each face  
             for (x, y, w, h) in faces:
                  blur_face = img[y:y+h, x:x+w]
                  distorted = distort_image(blur_face, 100)
                  img[y:y+h, x:x+w] = img_as_ubyte(distorted)
                   
             
             result.write(img)    
             # Display  
             cv.imshow('Pixelated', img)  
           
             keyCode = cv.waitKey(1)
         
             if cv.getWindowProperty('Pixelated', cv.WND_PROP_VISIBLE) <1:
                 break  
                   
         # Release the VideoCapture object  
         cap.release()
         result.release()
     video_pixelate(file_name)
     folder = QFileDialog.getExistingDirectory(
          self,
          caption = 'Select a folder'
          )
     name = "/obfuscated_video"
     shutil.move('C:/Users/saadm/OneDrive/Desktop/Files/programs/obfuscated_video.avi', str(folder)+ name +'.avi' )
