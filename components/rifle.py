from .tracker import Tracker
class Rifle:
    def __init__(self , display_width , display_height , triggerHandler):
        # openCV tracer
        self.tracker = Tracker('orange')

        # variables to scale the cursor to desired screen width and height 
        self.display_width = display_width
        self.display_height = display_height
        
        # initial cursor location 
        self.x = display_width // 2     
        self.y = display_height // 2    

        self.triggerHandler = triggerHandler    # function to be executed when trigger is pulled 
        self.point_radius = 5
        self.color = (255 , 0 , 0) # pointer color 
        self.loaded = True  # check if gun is ready to shoot next round 

        self.prev = False   # to keep track of shooting in EXP function

    def scalePointer(self , video_width = 640 , video_height = 480 ):
        # function to retrive the current position of the pointer and scale to current game window size.
        sight , trigger = self.tracker.getPos()
        if sight:
                self.x , self.y = (sight[0] + sight[2] , sight[1] + sight[3] )
                self.x = int((self.display_height * self.x)  /  video_height)
                self.y = int((self.display_width * self.y ) /  video_width)
                if trigger:
                    self.loaded = True
                elif self.loaded:
                    self.triggerHandler(self.x , self.y)
                    self.loaded = False
        return (self.x , self.y) 

    def scalePointerExp(self ,pos , shoot, video_width = 640 , video_height = 480 ):
        # similar to scalePointer but can set the x , y explicity (mouse)
        self.x , self.y  = pos
        if shoot:
            if not self.prev:
                self.triggerHandler(self.x , self.y)
        self.prev = shoot

        scaled_x = int((self.display_height * self.x)  /  video_height)
        scaled_y = int((self.display_width * self.y ) /  video_width)
        return (scaled_x , scaled_y) 
