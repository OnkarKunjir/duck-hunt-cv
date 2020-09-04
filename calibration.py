import numpy as np
import pickle
import cv2

def nothing(x):
    pass

def dump(lower_bound , upper_bound , file_name):
    with open(file_name + '_lower.pkl' , 'wb') as f:
        pickle.dump(lower_bound , f)
    with open(file_name + '_upper.pkl' , 'wb') as f:
        pickle.dump(upper_bound , f)

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)

    opened_kernel = np.ones((5,5))
    closed_kernel = np.ones((20,20))

    cv2.namedWindow('applied mask')
    lower_bound = np.array([0 , 0 , 0])
    upper_bound = np.array([0 , 0 , 0])
    
    cv2.createTrackbar('hl', 'applied mask' , 0, 179 , nothing )
    cv2.createTrackbar('sl', 'applied mask' , 0, 255 , nothing )
    cv2.createTrackbar('vl', 'applied mask' , 0, 255 , nothing )

    cv2.createTrackbar('hu', 'applied mask' , 0, 179 , nothing )
    cv2.createTrackbar('su', 'applied mask' , 0, 255 , nothing )
    cv2.createTrackbar('vu', 'applied mask' , 0, 255 , nothing )
    
    while True:
        ret , frame = camera.read()
        if not ret:
            print('Something went wrong while reading camera input')
            break
        else:
            lower_bound[0] = cv2.getTrackbarPos('hl' , 'applied mask')
            lower_bound[1] = cv2.getTrackbarPos('sl' , 'applied mask')
            lower_bound[2] = cv2.getTrackbarPos('vl' , 'applied mask')

            upper_bound[0] = cv2.getTrackbarPos('hu' , 'applied mask')
            upper_bound[1] = cv2.getTrackbarPos('su' , 'applied mask')
            upper_bound[2] = cv2.getTrackbarPos('vu' , 'applied mask')

            hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_frame , lower_bound , upper_bound)
            
            opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, opened_kernel)
            closed = cv2.morphologyEx(opened, cv2.MORPH_OPEN, closed_kernel)

            obj = cv2.bitwise_and(frame , frame , mask = closed)
            cv2.imshow('applied mask' , obj[: , ::-1])
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    camera.release()
    
    intent = input(f'pickle lower_bound {lower_bound} , upper_bound {upper_bound} (y/n) : ')
    if intent.strip() == 'y':
        file_name = input('file name : ').strip()
        dump(lower_bound , upper_bound , file_name)

