import pygame
import os
import math
#import Ball

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("FIRST Physics!")

WHITE = (255, 255, 255)

FPS = 120

GRAVITY = 1

ACCELERATION = pygame.math.Vector2(0, GRAVITY)

BALL_ONE_IMG = pygame.image.load(os.path.join('Assets', 'ball.png'))
BALL_ONE_WIDTH = 100
BALL_ONE_HEIGHT = 100

BALL_ONE_X_NOT = 400
BALL_ONE_Y_NOT = 300
BallOnePosition = pygame.math.Vector2(BALL_ONE_X_NOT, BALL_ONE_Y_NOT)

BALL_ONE_X_VEL = 30
BALL_ONE_Y_VEL = -25
BallOneVelocity = pygame.math.Vector2(BALL_ONE_X_VEL, BALL_ONE_Y_VEL)


BALL_TWO_IMG = pygame.image.load(os.path.join('Assets', 'ball2.png'))
BALL_TWO_WIDTH = 100
BALL_TWO_HEIGHT = 100

BALL_TWO_X_NOT = 700
BALL_TWO_Y_NOT = 200
BallTwoPosition = pygame.math.Vector2(BALL_TWO_X_NOT, BALL_TWO_Y_NOT)

BALL_TWO_X_VEL = -6
BALL_TWO_Y_VEL = -20
BallTwoVelocity = pygame.math.Vector2(BALL_TWO_X_VEL, BALL_TWO_Y_VEL)


def draw_window(ball, ball2):
    WIN.fill(WHITE)
    WIN.blit(BALL_ONE_IMG, (ball.x, ball.y))
    WIN.blit(BALL_TWO_IMG, (ball2.x, ball2.y))
    pygame.display.update()


def ball_handle_movement(ball, BallPosition, BallVelocity, BALL_HEIGHT, BALL_WIDTH, dt):
    BallPosition.x += BallVelocity.x

    BallVelocity.y += ACCELERATION.y * dt
    limit_ball_velocity(BallVelocity, 2)
    BallPosition.y += (BallVelocity.y*dt)+(ACCELERATION.y*.5*(dt**2))

    if BallPosition.x + BallVelocity.x > WIDTH - BALL_WIDTH:
        BallVelocity.x = (-1 * abs(BallVelocity.x))
        BallPosition.x = (WIDTH - BALL_WIDTH)
    if BallPosition.x < 0:
        BallVelocity.x = abs(BallVelocity.x)
        BallPosition.x = 0
    if BallPosition.y + BallVelocity.y > HEIGHT - BALL_HEIGHT:
        BallVelocity.y = (-1*abs(BallVelocity.y))
        BallPosition.y = (HEIGHT - BALL_HEIGHT)
    if BallPosition.y < 0:
        BallVelocity.y = abs(BallVelocity.y)
        BallPosition.y = 0

    ball.x = BallPosition.x
    ball.y = BallPosition.y


def limit_ball_velocity(BallVelocity, max_vel):
    min(-max_vel, max(BallVelocity.y, max_vel))
    if abs(BallVelocity.y) < .1:
        BallVelocity.y = 0


# def ball_on_ball_collision()


def main():

    ball = pygame.Rect(BALL_ONE_X_NOT, BALL_ONE_Y_NOT,
                       BALL_ONE_WIDTH, BALL_ONE_HEIGHT)

    ball2 = pygame.Rect(BALL_TWO_X_NOT, BALL_TWO_Y_NOT,
                        BALL_TWO_WIDTH, BALL_TWO_HEIGHT)

    # ball3 =

    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(FPS)

        dt = clock.tick(FPS) * .001 * FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ball_handle_movement(
            ball, BallOnePosition, BallOneVelocity, BALL_ONE_HEIGHT, BALL_ONE_WIDTH, dt)

        ball_handle_movement(
            ball2, BallTwoPosition, BallTwoVelocity, BALL_TWO_HEIGHT, BALL_TWO_WIDTH, dt)

        draw_window(ball, ball2)

    pygame.quit()


if __name__ == "__main__":
    main()
