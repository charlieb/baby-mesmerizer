import pygame
from pygame.locals import *
from math import sqrt, sin, cos, radians
from random import randint, random, choice

width = 1920
height = 1080

ellipse = 1
pulse = 2


class Circle:
    def __init__(self):
        self.red = False
        self.mode = ellipse + pulse
        self.randomize()

    def randomize(self):
        self.pos = (randint(0, width), randint(0, height))
        self.et = 0
        self.dt = (0.5 - random()) / 10.0
        self.major = random() * 100
        self.minor = random() * 100
        # pulse
        self.pt = 0
        self.freq = random()
        self.little = random() * 50
        self.big = random() * 100

    def update(self):
        if self.mode & pulse:
            self.pt += self.dt
        if self.mode & ellipse:
            self.et += self.dt

    def draw(self, screen):
        r = int(self.little + abs(sin(self.pt * self.freq)) * self.big)
        pos = (int(self.pos[0] + self.major * cos(self.et)),
               int(self.pos[1] + self.minor * sin(self.et)))
        pygame.draw.circle(screen,
                           (255,0,0) if self.red else (255, 255, 255),
                           pos, r, 0)
def main():
    pygame.init()
    pygame.font.init()
    size = width, height
    screen = pygame.display.set_mode(size)

    circles = [Circle() for _ in xrange(50)]
    recording = False

    its = 0
    while True:
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                return False
            elif event.key == K_e:
                for c in circles:
                    c.mode ^= ellipse
            elif event.key == K_p:
                for c in circles:
                    c.mode ^= pulse
            elif event.key == K_r:
                recording = not recording

        for c in circles:
            c.draw(screen)
            c.update()

        if its % 100 == 0:
            choice(circles).randomize()
        if its % 300 == 0:
            for c in circles:
                c.red = False
            choice(circles).red = True
        
        its += 1


        pygame.display.flip()
        if recording:
            pygame.image.save(screen, 'frame-%05d.png' % its)
            
        screen.fill((0,0,0))

if __name__ == "__main__":
    main()
