import random

# TODO : make bird fly indipendent of frame rate 
import time 

class Bird:
    def __init__(self , x , y , sky_width , sky_height):
        # to check if bird is out of screen and initalize positon 
        self.sky_width = sky_width
        self.sky_height = sky_height

        self.x = random.randint(70 , sky_width - 70) 
        self.y = sky_height - 100
        self.color = (255 , 255 , 255)
        self.size = (40 , 40)
        self.is_shot = False
        self.x_direction = random.choice([-5 , 5 , -4 , 4 , -3 , 3]) # direction in which bird flies (right , left)
        self.changed_x = False 

        self.is_out_of_frame = False


    def reset(self):
        self.x = random.randint(70 , self.sky_width - 70) 
        self.y = self.sky_height  - 100
        self.color = (255 , 255 , 255)
        self.is_shot = False
        self.x_direction = random.choice([-5 , 5 , -4 , 4 , -3 , 3 ]) # direction in which bird flies (right , left)
        self.is_out_of_frame = False
        self.changed_x = False


    def move(self):
        if self.is_shot:
            self.y += 5
        else:
            self.y -= 5
            self.x += self.x_direction
            if not self.changed_x:
                if random.random() > 0.9:
                    self.changed_x = True
                    self.x_direction = - self.x_direction
            
        # checking if the bird is out of frame 
        if (self.x + self.size[0]) < 0 or self.x > self.sky_width:
            # x coordinate is out of frame
            self.is_out_of_frame = True
        elif self.y + self.size[1] < 0:
            # if bird goes stright up in sky then it never crosses x axis.
            self.is_out_of_frame = True
        elif self.y > self.sky_height:
            self.is_out_of_frame = True

    def gotShot(self):
        if self.is_shot:
            self.color = (255 , 255 , 255)
        else:
            self.color = (255 , 0 , 0)
        self.is_shot = True

    def getRect(self):
        return ((self.x , self.y) , self.size)
