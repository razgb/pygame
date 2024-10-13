from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot

class Player(CircleShape):
    PLAYER_SHOOT_COOLDOWN = 0.2

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # takes in the Delta Time: time since last frame refresh.
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.cooldown <= 0:
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity += forward * PLAYER_SHOOT_SPEED
            self.cooldown = Player.PLAYER_SHOOT_COOLDOWN
        else:
            self.cooldown -= dt


    def update(self, dt):
        # seems like an object
        keys = pygame.key.get_pressed()

        # if any of these keys exist do an event
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
