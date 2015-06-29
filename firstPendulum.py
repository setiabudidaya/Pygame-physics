import math
import time
import pygame

def onPath(x,y):
    length = 250
    pivot_y = 40
    angle = 0.5*math.pi - math.atan2(y, x)
    if angle > 1.31:
        angle = 1.31
    elif angle < -1.31:
        angle = -1.31
    x = length*math.sin(angle)
    y = pivot_y + length*math.cos(angle)
    return (x, y)

def dist(a, b):
    d = ((a-x)**2 + (b-y)**2)**0.5
    return d

(width, height) = (640, 480)
background_colour = (255,255,255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendulum")

a = 0
b = 200
(x, y) = onPath(a, b)
# define pivot co-ordinates
pivot_x = 320
pivot_y = 40
# length of the pendulum
length = 250
angle = 0.5*math.pi - math.atan2(y, x)
# acceleration due to gravity
g = 9.8
# Initialise velocity variables
v_x = 0
v_y = 0
dt = 0.01

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)

# Calculate x component of pendulum using vector components of forces 
# acting on the pendulum. Calculate y component using pythagorous.

if __name__ == "__main__":
    running = True
    selected = False
    text = "Use the mouse to set the pendulum in motion"
    while running:
        screen.fill(background_colour)
        pygame.draw.line(screen, (0,0,255), (pivot_x-250, pivot_y),
                         (pivot_x + 250, pivot_y), 3)
        label = myfont.render(text, 1, (0,0,0))
        screen.blit(label, (70, 375))
        angle = 0.5*math.pi - math.atan2(y, x)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if pygame.mouse.get_pressed() == (1,0,0):
                (mouseX, mouseY) = pygame.mouse.get_pos()
                a = mouseX - pivot_x
                b = mouseY - pivot_y
                if dist(a, b) < 40:
                    (x, y) = onPath(a, b)
                    selected = True
                elif selected == True:
                    (x, y) = onPath(a, b)
             
            if event.type == pygame.MOUSEBUTTONUP:
                if selected == True:
                    v_x = 0
                selected = False
            
        if pygame.mouse.get_pressed() == (0,0,0) or selected == False:        
            angle = 0.5*math.pi - math.atan2(y, x)
            a_x = g*math.sin(angle)*math.sin((0.5*math.pi)-angle)
            v_x += a_x*dt
            x -= v_x
            y = pivot_y + (((length**2 - x**2)**2)**0.5)**0.5

        pygame.draw.line(screen, (0,0,255), (pivot_x, pivot_y),
                         (pivot_x + x, y), 3)
        pygame.draw.circle(screen, (255, 0, 0), (int(x + pivot_x), int(y)), 25, 0)

        pygame.display.flip()
        time.sleep(dt)

    pygame.quit()
        

