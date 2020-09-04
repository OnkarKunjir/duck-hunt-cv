import random
class Bird:
    def __init__(self , x , y , sky_width , sky_height):
        self.x = random.randint(70 , sky_width - 70) 
        self.y = sky_height 
        self.color = (255 , 255 , 255)
        self.size = (50 , 50)
        self.is_shot = False
        self.x_direction = random.choice((1,-1))

    def move(self):
        self.y -= 3
        self.x += self.x_direction

    def gotShot(self):
        if self.is_shot:
            self.color = (255 , 255 , 255)
        else:
            self.color = (255 , 0 , 0)
        self.is_shot = not self.is_shot
    def getRect(self):
        return ((self.x , self.y) , self.size)
