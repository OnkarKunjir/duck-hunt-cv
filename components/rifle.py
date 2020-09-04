from .tracker import Tracker
class Rifle:
    def __init__(self , x , y , triggerHandler):
        # initial cursor location
        self.tracker = Tracker('orange')

        self.x = x
        self.y = y
        self.triggerHandler = triggerHandler
        self.point_radius = 5
        self.color = (255 , 0 , 0)
        self.loaded = True

        self.prev = False

    #def getPos(self , pos , shoot):
    #    self.x , self.y  = pos
    #    if shoot:
    #        if not self.prev:
    #            self.triggerHandler(self.x , self.y)
    #    self.prev = shoot
    #    return (self.x , self.y)

    def getPos(self):
        sight , trigger = self.tracker.getPos()
        if sight:
                self.x , self.y = (sight[0] + sight[2] , sight[1] + sight[3] )
                if trigger:
                    self.loaded = True
                elif self.loaded:
                    self.triggerHandler(self.x , self.y)
                    self.loaded = False

        return (self.x , self.y)

if __name__ == '__main__':
    rifle = Rifle()

