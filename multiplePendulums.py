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

def collide(p1, p2):
    """Check if 2 pendulums have collided and if so alter v_x"""
    if dist(p1.x + p1.pivot_x, p1.y, p2.x + p2.pivot_x, p2.y) < 50:
       (p1.v_x, p2.v_x) = (p2.v_x, p1.v_x)
       if p1.x < p2.x:
           p2.x - 3
           p2.x + 3
       if p1.x > p2.x:
           p1.x + 3
           p2.x - 3
           
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
        self.ID = None
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
    my_pendulums = [Pendulum(0, 250, 40), Pendulum(0, 300, 40), Pendulum(0, 350, 40), Pendulum(0, 400, 40)]
    for i, p in enumerate(my_pendulums):
        p.ID = i
    numPen = len(my_pendulums)

    running = True
    selected = None
    while running:
        screen.fill(background_colour)
        pygame.draw.line(screen, (0,0,255), (120, 40),
                         (520, 40), 3)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for p in my_pendulums:
            if pygame.mouse.get_pressed() == (1,0,0):
                (mouseX, mouseY) = pygame.mouse.get_pos()
                a = mouseX - p.pivot_x
                b = mouseY - p.pivot_y
                if dist(a, b, p.x, p.y) < 40:
                    if selected == None:
                        selected = p.ID
                        (p.x, p.y) = onPath(a, b, p.length, p.pivot_y)
                        p.v_x = 0
                elif selected == p.ID:
                    (p.x, p.y) = onPath(a, b, p.length, p.pivot_y)
                    p.v_x = 0
                if p.ID < numPen-1:
                    for i in range(p.ID, numPen-1):
                        collide(my_pendulums[p.ID], my_pendulums[i+1])
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if selected == p.ID:
                    p.v_x = 0
                selected = None

            if p.ID < numPen-1:
                for i in range(p.ID, numPen-1):
                    collide(my_pendulums[p.ID], my_pendulums[i+1])

            if selected != p.ID:         
                p.swing()
            p.draw()

        time.sleep(0.4*0.01)
        pygame.display.flip()

    pygame.quit()
    
