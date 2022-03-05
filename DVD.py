import pygame, sys
import random

screenSize = [1280, 800]

class SpriteLoader(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))

class DVD(SpriteLoader):
    def __init__(self):
        super().__init__("dvd logo.png", screenSize[0]/2 - 15, screenSize[1]/2 - 15)
        self.speed_x = 5
        self.speed_y = 5
    
    def update(self):
        self.rect.x  += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= screenSize[1]:
                self.speed_y *= -1
                if random.randint(1, 3) == 1:
                    self.speed_x *= -1
        if self.rect.left <= 0 or self.rect.right >= screenSize[0]:
                self.speed_x *= -1
                if random.randint(1, 3) == 1:
                    self.speed_y *= -1

clock = pygame.time.Clock()
dvd = DVD()
group = pygame.sprite.Group()
group.add(dvd)
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("DVD")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

        
        
    screen.fill((150, 150, 150))
    group.draw(screen)
    group.update()
    pygame.display.flip()
    clock.tick(120)
        