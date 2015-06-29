import pygame
import math
import time

class Pendulum():
    def __init__(self, angle):
        self.pivot_x = 320
        self.pivot_y = 40
        self.length = 250
        self.angle = angle
        self.x = self.length*math.sin(self.angle)
        self.y = self.length*math.cos(self.angle)
        self.v_x = 0
        self.a_x = 0

    def swing(self):
        g = 9.8
        dt = 0.01
        self.angle = 0.5*math.pi - math.atan2(self.y, self.x)
        self.a_x = g*math.sin(self.angle)*math.sin((0.5*math.pi)-self.angle)
        self.v_x += self.a_x*dt
        self.x -= self.v_x
        self.y = self.pivot_y + (((self.length**2 - self.x**2)**2)**0.5)**0.5
        time.sleep(dt)

    def draw(self):
        bobSize = 25
        pygame.draw.line(screen, (0,0,255), (self.pivot_x, self.pivot_y),
                         (self.pivot_x + self.x, self.y), 3)
        pygame.draw.circle(screen, (230,10,10),
                           (int(self.pivot_x + self.x), int(self.y)),
                           bobSize, 0)
