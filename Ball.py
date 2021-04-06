import pygame
import os
import sys
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, vel_x, vel_y, accel_x, accel_y, filePath):
        super().__init__()
        self.image = pygame.image.load(filePath)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.position, self.velocity = pygame.math.Vector2(
            pos_x, pos_y), pygame.math.Vector2(vel_x, vel_y)
        self.acceleration = pygame.math.Vector2(accel_x, accel_y)

    def draw(self, display)
    pass

    def update(self, dt)
    self.horizontal_movement(dt)
    self.vertical_movement(dt)

    def horizontal_movement(self, dt):


def possition():


def main():
    pygame.init()
    clock = pygame.time.Clock()

    WIDTH = 1000
    HEIGHT = 700

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball = Ball(100, 100, 450, 300, os.path.join('Assets', 'ball2.png'))

    ball_group = pygame.sprite.Group()
    ball_group.add(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()
        screen.fill((60, 60, 60))
        ball_group.draw(screen)
        clock.tick(60)


if __name__ == '__main__':
    main()
