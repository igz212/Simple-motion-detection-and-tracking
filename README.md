# motion-detection-by-OpenCV
Simple motion detection and tracking by means of OpenCV. 


By means of showing these figures we could understand the process step by step  :) 
     Here we use OpenCV to calculate difference of frames one by one. then use Binary threshold to gain
     a gray scale images look like an image of white shadows, which we could gain contours of them.
     so we could draw contours of motion in these frame or use boundingRect to draw a Rectangle around
     of each contours.
     be aware :
        * any motion in the video could be capture, like a rope movement or animals. to gain better results,
        we could change  minimum area to detect motion to avoid small object's movement to detect.
