import ctypes
import random
import pygame
from sys import exit
import math

import calculations

class Particle:
    """Class of particle"""

    def __init__(self, prop):
        self.name = ''
        self.x = prop['x_coord']
        self.y = prop['y_coord']
        self.size = prop['size']
        self.color = prop['color']
        # if we set thickness = 0 then we fill entire circle
        self.thickness = prop['thickness']
        self.speed = prop['speed']
        self.acceleration = prop['acceleration']
        self.angle = prop['angle']
        self.screen = prop['screen']

    def display(self):
        """Displaying particle on the screen"""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)

    def move(self, width, height):
        """move particle to to the new location
        According its x,y and speed and angle(moving vector)"""
        self.speed = self.speed + self.acceleration
        self.x += math.sin(self.angle) * (self.speed)
        self.y -= math.cos(self.angle) * (self.speed)

        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle

        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle


def randomization(disp_width, disp_hight, size_int):
    """Get random values of size, x, y locations and color"""
    size = random.randint(size_int[0], size_int[1])
    x = random.randint(size, disp_width - size)
    y = random.randint(size, disp_hight - size)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    angle = random.uniform(0, math.pi*2)
    acceleration = random.uniform(0.1, 1)
    return x, y, size, color, angle, acceleration

"""
pygame.draw.polygon(screen, (70, 70, 70), ((0, 0), (100, 0), (100, 100), (0, 100)))
pygame.draw.polygon(screen, (0, 0, 255), ((100, 100), (200, 200), (100, 200)))
#Рисуем желтую окружность с радиусом 100 пикселей
pygame.draw.circle(screen, (255, 255, 0), (400, 200), 100)


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Левая стрелка')
            elif event.key == pygame.K_RIGHT:
                print('Правая стрелка')
            elif event.key == pygame.K_UP:
                print('Стрелка вверх')
            elif event.key == pygame.K_DOWN:
                print('Стрелка вниз')
"""



# Get instance of pygame
pygame.init()

# initialize frame rate
FPS = 60
clock = pygame.time.Clock()

# Get display dimensions using "ctype" applicable for Windows only
disp_width = ctypes.windll.user32.GetSystemMetrics(0)-200
disp_hight = ctypes.windll.user32.GetSystemMetrics(1)-300
# initialize screen for displaying
screen = pygame.display.set_mode((disp_width, disp_hight))
# Set caption for screen
pygame.display.set_caption('introduction in physics')
# Set white color for screen filling
background_colour = (255, 255, 255)
screen.fill(background_colour)


number_particles = 300
particles_container = []

particle_properties = {'x_coord': 0,
              'y_coord': 0,
              'size': 1,
              'color': (0, 0, 0),
              'thickness': 0,
              'speed': 0.1,
              'acceleration': 0.5,
              'angle': 0,
              'screen': screen}

for particle in range(number_particles):
    x, y, size, color, angle, acceleration = randomization(disp_width, disp_hight, (1, 40))
    particle_properties.update({'x_coord': x,
                                'y_coord': y,
                                'size': size,
                                'color': color,
                                'angle': angle,
                                'acceleration': 0})

    particles_container.append(Particle(particle_properties))

while True:
    screen.fill(background_colour)
    for particle in particles_container:
        particle.move(disp_width, disp_hight)
        particle.display()

    # Passing through events appeared
    for event in pygame.event.get():
        # if type of event corresponds to quit then quit))
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Update the screen on the each step of main loop of the game
    pygame.display.update()
    # Set up the frame rate
    clock.tick(FPS)
