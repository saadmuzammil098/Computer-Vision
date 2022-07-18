# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:50:54 2020

@author: SaadMuzammil
"""

def video_blurring(self, filename):
    def video_blur(file_name):  
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
                blur_face = cv.GaussianBlur(blur_face,(45, 45),50)
                img[y:y+blur_face.shape[0], x:x+blur_face.shape[1]] = blur_face
            
            result.write(img)
            #show image
            cv.imshow("Blur Faced", img)
              
            keyCode = cv.waitKey(1)
        
            if cv.getWindowProperty('Blur Faced', cv.WND_PROP_VISIBLE) <1:
                break  
                  
        # Release the VideoCapture object  
        cap.release()
        result.release()
    video_blur(file_name)
    folder = QFileDialog.getExistingDirectory(
         self,
         caption = 'Select a folder'
         )
    name = "/obfuscated_video"
    shutil.move('C:/Users/saadm/OneDrive/Desktop/Files/programs/obfuscated_video.avi', str(folder)+ name +'.avi' )
