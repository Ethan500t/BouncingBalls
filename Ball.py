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
        self.width = width
        self.height = height
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

def detect_wall_collision(windowX, windowY, ball):
    if ball.position.x > windowX - ball.width:
        ball.velocity.x = (-1 * abs(ball.velocity.x))
        ball.position.x = (windowX - ball.width)
    if ball.position.x < 0:
        ball.velocity.x = abs(ball.velocity.x)
        ball.position.x = 0
    if ball.position.y > windowY - ball.width:
        ball.velocity.y = (-1 * abs(ball.velocity.y))
        ball.position.y = (windowY - ball.width)
    if ball.position.y < 0:
        ball.velocity.y = abs(ball.velocity.y)
        ball.velocity.y = 0

def detect_ball_collision(ball1, ball2):
    if math.hypot(ball1.position.x - ball2.position.x, ball1.position.y - ball2.position.y) < 100:
        ball1.velocity.x = (-1 * (ball1.velocity.x))
        ball1.velocity.y = ((ball1.velocity.y))
        ball2.velocity.x = (-1 * (ball2.velocity.x))
        ball2.velocity.y = ((ball2.velocity.y))


def main():

    FPS = 60

    clock = pygame.time.Clock()

    WIDTH = 1500
    HEIGHT = 1000

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball = Ball(100, 100, 450, 300, 10, 0, 0, .1, os.path.join("Assets", "ball2.png"))
    ball2 = Ball(100, 100, 200, 200, -10, 0, 0, .1, os.path.join("Assets", "ball.png"))

    ball_group = pygame.sprite.Group()
    ball_group.add(ball, ball2)

    while True:
        pygame.init()
        clock.tick(FPS)

        dt = clock.tick(FPS) * 0.001 * FPS
        #print(ball.position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((60, 60, 60))
        ball_group.update(dt)
        ball_group.draw(screen)
        detect_ball_collision(ball, ball2)
        detect_wall_collision(WIDTH, HEIGHT, ball)
        detect_wall_collision(WIDTH, HEIGHT, ball2)
        pygame.display.update()




if __name__ == "__main__":
    main()
