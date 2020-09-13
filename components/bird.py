import random

# TODO : make bird fly indipendent of frame rate 
import time 

class Bird:
    def __init__(self , x , y , sky_width , sky_height):
        # to check if bird is out of screen and initalize positon 
        self.sky_width = sky_width
        self.sky_height = sky_height

        self.x = random.randint(70 , sky_width - 70) 
        self.y = sky_height 
        self.color = (255 , 255 , 255)
        self.size = (50 , 50)
        self.is_shot = False
        self.x_direction = random.choice((1,-1))

        self.is_out_of_frame = False


    def reset(self):
        self.x = random.randint(70 , self.sky_width - 70) 
        self.y = self.sky_height 
        self.color = (255 , 255 , 255)
        self.is_shot = False
        self.x_direction = random.choice((1,-1))
        self.is_out_of_frame = False


    def move(self):
        #time.sleep(0.01)
        self.y -= 1
        self.x += self.x_direction

        #self.y -= 0
        #self.x += 0

        if (self.x + self.size[0] < 0 or self.x > self.sky_width)  and self.y + self.size[1] < 0:
            self.is_out_of_frame = True

    def gotShot(self):
        if self.is_shot:
            self.color = (255 , 255 , 255)
        else:
            self.color = (255 , 0 , 0)
        self.is_shot = True

    def getRect(self):
        return ((self.x , self.y) , self.size)
