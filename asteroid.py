from constants import ASTEROID_MIN_RADIUS
import pygame
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # moving in a straight line.
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # asteroid is too smaller to break up more.

        random_angle = random.uniform(20, 50)
        random_vector_1 = self.velocity.rotate(random_angle)
        random_vector_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = random_vector_1 * 1.2
        asteroid_2.velocity = random_vector_2
