import pygame
from components.static import Ground , Sky
from components.rifle import Rifle
from components.bird import Bird

# TODO : // use threading this shit is slow af.

class DuckHunt:
    def __init__(self):
        # initalize pygame and screen
        pygame.init()
        
        self.display_width = 640
        self.display_height = 480
        self.display = pygame.display.set_mode((self.display_width , self.display_height))
        pygame.display.set_caption('Duck Hunt')

        # state management variables
        self.render_next_frame = True



        # game components
        self.ground = Ground(display = (self.display_width , self.display_height) , ground_height =  int(self.display_height * 0.3))

        self.sky = Sky(display = (self.display_width , self.display_height) , sky_height =  self.display_height - self.ground.size[1] )

        self.rifle =  Rifle(self.display_width//2 , self.display_height//2 , self.triggerHandler)

        self.test_bird = Bird(300 , 300 ,self.display_width , self.sky.size[1]  )

        self.score = 0
        
    def __del__(self):
        pygame.quit()
    
    def triggerHandler(self , x , y):
        # function to be executed when trigger is pulled 
        if x >= self.test_bird.x and x <= self.test_bird.x + self.test_bird.size[0]:
            if y >= self.test_bird.y and y <= self.test_bird.y + self.test_bird.size[1]:
                self.test_bird.gotShot()
        
    def updateScore(self):
        if self.test_bird.is_shot:
            self.score += 1
            self.test_bird.reset()
        elif self.test_bird.is_out_of_frame:
            self.test_bird.reset()




    def drawFrame(self):
        pygame.draw.rect(self.display , self.ground.color , self.ground.getRect())
        pygame.draw.rect(self.display , self.sky.color , self.sky.getRect())
        pygame.draw.rect(self.display , self.test_bird.color , self.test_bird.getRect())
        # for testing purposes
        pygame.draw.circle(self.display , self.rifle.color , self.rifle.getPosExp(pygame.mouse.get_pos() , pygame.mouse.get_pressed()[0]) , self.rifle.point_radius )
        #pygame.draw.circle(self.display , self.rifle.color , self.rifle.getPos() , self.rifle.point_radius )
        pygame.display.update()

    def eventHandler(self , event):
        if event.type == pygame.KEYDOWN:
            # quit the game 
            if event.key == pygame.K_ESCAPE:
                self.render_next_frame = False

    def play(self):
        # main game loop
        while self.render_next_frame:
            self.test_bird.move()
            self.updateScore()
            self.drawFrame()
            for event in pygame.event.get():
                self.eventHandler(event)

if __name__ == '__main__':
    duckHunt = DuckHunt()
    duckHunt.play()
