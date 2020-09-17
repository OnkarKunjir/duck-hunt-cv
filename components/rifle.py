from .tracker import Tracker
class Rifle:
    def __init__(self , display_width , display_height , triggerHandler):
        # initial cursor location
        self.tracker = Tracker('orange')


        self.display_width = display_width
        self.display_height = display_height

        self.x = display_width // 2
        self.y = display_height // 2
        self.triggerHandler = triggerHandler
        self.point_radius = 5
        self.color = (255 , 0 , 0)
        self.loaded = True

        self.prev = False

    def scalePointer(self , video_width = 640 , video_height = 480 ):

        sight , trigger = self.tracker.getPos()
        if sight:
                self.x , self.y = (sight[0] + sight[2] , sight[1] + sight[3] )
                self.x = int((self.display_height * self.x)  /  video_height)
                self.y = int((self.display_width * self.y ) /  video_width)
                if trigger:
                    self.loaded = True
                elif self.loaded:
                    print('shoot')
                    self.triggerHandler(self.x , self.y)
                    self.loaded = False
        return (self.x , self.y) 

    def scalePointerExp(self ,pos , shoot, video_width = 640 , video_height = 480 ):
        self.getPosExp(pos , shoot) 
        scaled_x = int((self.display_height * self.x)  /  video_height)
        scaled_y = int((self.display_width * self.y ) /  video_width)
        return (scaled_x , scaled_y) 

    def getPosExp(self , pos , shoot):
        self.x , self.y  = pos
        if shoot:
            if not self.prev:
                self.triggerHandler(self.x , self.y)
        self.prev = shoot
        return (self.x , self.y)

    def getPos(self):
        sight , trigger = self.tracker.getPos()
        if sight:
                self.x , self.y = (sight[0] + sight[2] , sight[1] + sight[3] )
                if trigger:
                    self.loaded = True
                elif self.loaded:
                    print('shoot')
                    self.triggerHandler(self.x , self.y)
                    self.loaded = False

        return (self.x , self.y)
