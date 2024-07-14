import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        # create the screen
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Ninja Game")

        self.clock = pygame.time.Clock()

        # Load the image
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0,0,0))
        self.img_pos = [160,160]

        self.movement = [False, False]

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.img_pos[1] += self.movement[1] - self.movement[0] * 5
            # show the image on the screen
            self.screen.blit(self.img, self.img_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    sys.exit

                # MOVEMENT
                # We are using the arrow keys due to the differences in keyboard layouts
                # This is also why we will be using x and c
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            pygame.display.update()
            # 60fps
            self.clock.tick(60)

Game().run()