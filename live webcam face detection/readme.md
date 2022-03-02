

# Face detection on webcam


### Face detection
Detecting face using haar cacsade classifier. OpenCV comes with a number of built-in cascades for detecting everything from faces to eyes to hands to legs. detectMultiScale is the function to detect the face which take 3 arguments by default, image, scale factor and minimum neighbors. After the face is detected we will draw rectangle around the facce found using rectangle function of opencv.


### Capture frame from Webcam
OpenCV provides a video capture object which handles everything related to opening and closing of the webcam. VideoCapture is the function to create object captured. To read each frames from video we will user read() function. To release the frame after detection we will use release() function.


