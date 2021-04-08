import pygame
import os
import sys
import math


class Ball(pygame.sprite.Sprite):
    def __init__(
        self, width, height, pos_x, pos_y, vel_x, vel_y, accel_x, accel_y, filePath
    ):
        super().__init__()
        self.image = pygame.image.load(filePath)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.position = pygame.math.Vector2(pos_x, pos_y)
        self.velocity = pygame.math.Vector2(vel_x, vel_y)
        self.acceleration = pygame.math.Vector2(accel_x, accel_y)

    def draw(self, display, dt):
        self.update(dt)
        display.blit(self.image, (self.position.x, self.position.y))

    def update(self, dt):
        self.x_movement(dt)
        self.y_movement(dt)
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def x_movement(self, dt):
        self.velocity.x += self.acceleration.x*dt
        self.position.x += (self.velocity.x * dt) + ((0.5 * self.acceleration.x) * (dt ** 2))
        

    def y_movement(self, dt):
        self.velocity.y += self.acceleration.y*dt
        self.position.y += (self.velocity.y * dt) + ((0.5 * self.acceleration.y) * (dt ** 2))


def main():

    FPS = 60

    clock = pygame.time.Clock()

    WIDTH = 1500
    HEIGHT = 1000

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball = Ball(100, 100, 450, 300, 10, 0, 0, 0.1, os.path.join("Assets", "ball2.png"))

    ball_group = pygame.sprite.Group()
    ball_group.add(ball)

    while True:
        pygame.init()
        clock.tick(FPS)

        dt = clock.tick(FPS) * 0.001 * FPS
        print(ball.position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((60, 60, 60))
        ball.draw(screen, dt)
        pygame.display.update()


if __name__ == "__main__":
    main()
