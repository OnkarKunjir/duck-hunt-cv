import pygame

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

        # game components positon and size
        self.ground_height = int(self.display_height * 0.3)
        self.ground = pygame.Rect( (0 , self.display_height - self.ground_height) , (self.display_width , self.ground_height) )

    def __del__(self):
        pygame.quit()
    

    def drawFrame(self):
        pygame.draw.rect(self.display , (255 , 255 , 255) , self.ground)
        pygame.display.update()

    def eventHandler(self , event):
        if event.type == pygame.KEYDOWN:
            # quit the game 
            if event.key == pygame.K_ESCAPE:
                self.render_next_frame = False

    def play(self):
        # main game loop
        while self.render_next_frame:
            self.drawFrame()
            for event in pygame.event.get():
                self.eventHandler(event)

if __name__ == '__main__':
    duckHunt = DuckHunt()
    duckHunt.play()
