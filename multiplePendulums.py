import pygame
import math
import time

def dist(a, b, x, y):
    """Return distance between 2 points"""
    d = math.hypot(a-x, b-y)
    return d

def onPath(a, b, length, pivot_y):
    """Move coordinates onto the path of the pendulum"""
    angle = 0.5*math.pi - math.atan2(b, a)
    if math.fabs(angle) > 0.48*math.pi:
        angle = 0.48*math.pi
    x = length*math.sin(angle)
    y = pivot_y + length*math.cos(angle)
    return (x, y)        
    
class Pendulum():
    def __init__(self, angle, pivot_x, pivot_y):
        self.pivot_x = pivot_x
        self.pivot_y = pivot_y
        self.length = 250
        self.angle = angle
        self.x = self.length*math.sin(self.angle)
        self.y = self.length*math.cos(self.angle)
        self.v_x = 0
        self.a_x = 0
        self.selected = False
        self.mass = 1

    def swing(self):
        """Calculate change in x & y in a time dt"""
        g = 9.8
        dt = 0.01
        self.angle = 0.5*math.pi - math.atan2(self.y, self.x)
        self.a_x = g*math.sin(self.angle)*math.sin((0.5*math.pi)-self.angle)
        self.v_x += self.a_x*dt
        self.x -= self.v_x
        self.y = self.pivot_y + (((self.length**2 - self.x**2)**2)**0.5)**0.5

    def draw(self):
        """Display pendulum on the screen"""
        bobSize = 25
        pygame.draw.line(screen, (0,0,255), (self.pivot_x, self.pivot_y),
                         (self.pivot_x + self.x, self.y), 3)
        pygame.draw.circle(screen, (230,10,10),
                           (int(self.pivot_x + self.x), int(self.y)),
                           bobSize, 0)

if __name__ == "__main__":
    (width, height) = (640, 480)
    background_colour = (255,255,255)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pendulum")
    my_pendulums = [Pendulum(0, 300, 40), Pendulum(0, 350, 40), Pendulum(0, 400, 40)]

    running = True
    selected = False
    while running:
        screen.fill(background_colour)
        pygame.draw.line(screen, (0,0,255), (120, 40),
                         (520, 40), 3)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i, p in enumerate(my_pendulums):
            if pygame.mouse.get_pressed() == (1,0,0):
                (mouseX, mouseY) = pygame.mouse.get_pos()
                a = mouseX - p.pivot_x
                b = mouseY - p.pivot_y
                if dist(a, b, p.x, p.y) < 40:
                    (p.x, p.y) = onPath(a, b, p.length, p.pivot_y)
                    p.selected = True
                elif p.selected == True:
                    (p.x, p.y) = onPath(a, b, p.length, p.pivot_y)
                p.draw()

            if event.type == pygame.MOUSEBUTTONUP:
                if selected == True:
                    p.v_x = 0
                p.selected = False
                    
            if pygame.mouse.get_pressed() == (0,0,0) or p.selected == False:
                p.swing()
                p.draw()

        time.sleep(0.5*0.01)
        pygame.display.flip()

    pygame.quit()
    
