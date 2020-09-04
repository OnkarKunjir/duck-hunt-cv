from tracker import Tracker
import pygame


class TrackTest:
    def __init__(self):
        pygame.init()
        self.tracker = Tracker('orange')

        self.display_size = (640 , 480)
        self.display = pygame.display.set_mode(self.display_size)
        pygame.display.set_caption('TrackTest')
        self.clock = pygame.time.Clock()

        #pygame.mixer.init(frequency = 4000)
        #pygame.mixer.music.load('Desert Eagle Sound effects.mp3')
        #pygame.mixer.music.set_volume(0.7)
        #pygame.mixer.music.play()
        
        # simulation variables
        self.shots = [None]*10
        self.current_round = 0
        self.loaded = True

        self.render_frame = True


    def drawFrame(self):
        while self.render_frame:
            self.display.fill((255 , 255 , 255))
            sight , trigger = self.tracker.getPos() 
            # calculate the center of rectangle 
            if sight:
                sight = (sight[0] + sight[2] , sight[1] + sight[3] )
                pygame.draw.circle(self.display , (255 , 0 , 0) , sight , 10)

                if trigger:
                    self.loaded = True
                elif self.loaded:
                    #pygame.mixer.music.play()
                    self.loaded = False
                    if self.current_round < len(self.shots):
                        self.shots[self.current_round] = sight 
                        self.current_round += 1
                    else:
                        self.shots[0] = sight 
                        self.current_round = 1

            for shot in self.shots:
                if shot == None:
                    break
                pygame.draw.circle(self.display , (0 , 255 , 0) , shot , 10)



            pygame.display.update()


            # handle game events
            for event in pygame.event.get():
                pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        self.render_frame = False
                        break


if __name__ == '__main__':
    test = TrackTest()
    test.drawFrame()
