class Ground:
    def __init__(self , display , ground_height , color = (140 , 107 , 0)):
        self.pos = (0 , display[1] - ground_height)
        self.size = (display[0] , ground_height)
        self.color = color
        self.rect = (self.pos , self.size)

    def getRect(self):
        return self.rect


class Sky:
    def __init__(self , display , sky_height , color = (47 , 179 , 254)):
        self.pos = (0 , 0)
        self.size = (display[0] , sky_height)
        self.color = color
        self.rect = (self.pos , self.size)

    def getRect(self):
        return self.rect
