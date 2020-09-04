import numpy as np
import cv2
import pickle

class Tracker:
    def __init__(self , color_name):
        self.lower_bound = None
        self.upper_bound = None
        self.opened_kernel = np.ones((5 , 5))
        self.closed_kernel = np.ones((20 , 20))
        print(f'Detecting {color_name}')
        self.load(color_name) #load upper and lower bound of color from pickle
        
        # initalize camera and other 
        print('Capturing camera 0')
        self.camera = cv2.VideoCapture(0)
        self.frame = None
        # cv2.namedWindow('frame')

    def load(self , file_name):
        file_name = 'colors/' + file_name
        with open(file_name + '_lower.pkl' , 'rb') as f:
            self.lower_bound = pickle.load(f)
        with open(file_name + '_upper.pkl' , 'rb') as f:
            self.upper_bound = pickle.load(f)

    def getPos(self):
        trigger = None
        sight = None

        ret , self.frame = self.camera.read()
        self.frame = cv2.flip(self.frame , 1)

        hsv_frame = cv2.cvtColor(self.frame , cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame , self.lower_bound , self.upper_bound)
        opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.opened_kernel)
        closed = cv2.morphologyEx(opened, cv2.MORPH_OPEN, self.closed_kernel)

        contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        if len(contours) > 1:
            b1 = cv2.boundingRect(contours[0])
            b2 = cv2.boundingRect(contours[1])
            (sight , trigger) = (b1 , b2) if (b1[1] > b2[1]) else (b2 , b1)
        elif len(contours) == 1:
            sight = cv2.boundingRect(contours[0])


        # displaying the frame 
        if sight:
            x , y , w , h = sight
            cv2.rectangle(self.frame , (x, y) , (x + w , y + h) , (255 , 0 , 0) , 4)

        if trigger:
            x , y , w , h = trigger
            cv2.rectangle(self.frame , (x, y) , (x + w , y + h) , (0 , 255 , 0) , 4)

        cv2.imshow('frame' , self.frame)
        cv2.waitKey(1)

        # end displaying
        return (sight , trigger)

    def __del__(self):
        self.camera.release()

if __name__ == '__main__':
    tracker = Tracker('orange')
    while True:
        tracker.getPos()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
