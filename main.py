import ctypes
import random
import pygame
from sys import exit
import math

from colors import color_rgb

try:
    # If password exists use main key and case
    from password import get_pass_word
    MySql_key = get_pass_word()
except:
    MySql_key = '123'

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
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

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


class Particles:
    """Set of particles"""
    def __init__(self, screen_id):
        self.particle_init_properties = {'x_coord': 0,
                                         'y_coord': 0,
                                         'size': 1,
                                         'color': (0, 0, 0),
                                         'thickness': 0,
                                         'speed': 0.5,
                                         'acceleration': 0.5,
                                         'angle': 0,
                                         'screen': screen_id}

        self.particles_set = []

    def initialize_particles(self, amount, display_width, display_height):
        for p in range(amount):
            x, y, size, color, angle, acceleration = self.randomization(display_width, display_height, (1, 40))
            properties = self.particle_init_properties
            properties.update({'x_coord': x,
                               'y_coord': y,
                               'size': size,
                               'color': color,
                               'angle': angle,
                               'acceleration': 0})

            self.particles_set.append(Particle(properties))

    @staticmethod
    def randomization(display_width, display_height, size_int):
        """
        function to get random values of size, x, y locations, color, angle of movement and acceleration
        disp_width - current display width in pixels;
        disp_fight - current display height in pixels;
        size_int - list includes two values the first min size and the second max size.
        """

        size = random.randint(size_int[0], size_int[1])
        x = random.randint(size, display_width - size)
        y = random.randint(size, display_height - size)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        angle = random.uniform(0, math.pi*2)
        acceleration = random.uniform(0.1, 1)
        return x, y, size, color, angle, acceleration


def main(fps=60):
    # Get instance of pygame
    pygame.init()

    # initialize frame rate

    clock = pygame.time.Clock()

    # Get display dimensions using "ctype" applicable for Windows only
    disp_width = ctypes.windll.user32.GetSystemMetrics(0)-200
    disp_height = ctypes.windll.user32.GetSystemMetrics(1) - 300

    # initialize screen for displaying
    screen = pygame.display.set_mode((disp_width, disp_height))
    # Set caption for screen
    pygame.display.set_caption('introduction in movement physics')

    # Create particles
    particles = Particles(screen)
    particles.initialize_particles(100, disp_width, disp_height)

    # Launch the main loop of program
    while True:
        screen.fill(color_rgb('black'))
        for particle in particles.particles_set:
            particle.move(disp_width, disp_height)
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
        clock.tick(fps)


if __name__ == "__main__":
    main(120)
