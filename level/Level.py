import random
import sys

import pygame

from shape.Circle import Circle
from shape.Rectangle import Rectangle
from shape.Snowflake import Snowflake


class Level:
    def __init__(self, radius, length, layers, snowflakeColor, wind):
        self.__radius = radius
        self.__length = length
        self.__layers = layers
        self.__snowflakeColor = snowflakeColor
        self.__wind = wind

        self.__screen = [800, 450]
        self.__surface = pygame.display.set_mode(self.__screen)
        self.__shapes = []
        self.__font = pygame.font.SysFont('Comic Sans MS', 100)

        self.__energy = 80
        self.__clock = pygame.time.Clock()

    def initializeShapes(self):
        floor = .8 * self.__screen[1]
        self.__shapes = [
            Rectangle([200, 255, 200], [0, floor, self.__screen[0], .2 * self.__screen[1]]),
            Circle([80, 30, 30], [20, floor - self.__radius, self.__radius, 0, 0, 0]),
            [],
            []
        ]

        hyperLength = self.__length * self.__layers
        x = self.__screen[0] - 20 - hyperLength
        y = floor - hyperLength
        for i in range(0, hyperLength, self.__length):
            for j in range(0, hyperLength, self.__length):
                self.__shapes[2].append(Rectangle([200, 200, 150], [x + i, y + j, self.__length, self.__length]))

    def addSnowflake(self):
        self.__shapes[3].append(Snowflake(
            self.__snowflakeColor,
            [random.randint(- self.__wind ** 2, self.__screen[0] + self.__wind ** 2), 0, 5, 0, self.__wind, random.randint(5, 20)],
            [None, random.randint(self.__shapes[0].getPosition()[1], self.__screen[1]), None, 600]
        ))

    def drawBackground(self):
        self.__surface.fill([220, 220, 220])

    def drawFloor(self):
        self.__shapes[0].draw(self.__surface)

    def applyFrictionAndNormalForce(self):
        circle = self.__shapes[1]
        x, y, radius, xVelocity, yVelocity, yAcceleration = circle.getPosition()

        if circle.isTouching(self.__shapes[0]):
            if xVelocity < 0.2:
                circle.getPosition()[3] = 0
            else:
                circle.getPosition()[3] /= 1.1
            circle.getPosition()[4], circle.getPosition()[5] = 0, 0

    def applyMotionAndGravity(self):
        circle = self.__shapes[1]
        x, y, radius, xVelocity, yVelocity, yAcceleration = circle.getPosition()

        if xVelocity != 0 or yVelocity != 0:
            circle.getPosition()[0] += xVelocity
            circle.getPosition()[1] -= yVelocity
            circle.getPosition()[4] -= yAcceleration

    def applyTerminalVelocityAndLaunch(self):
        circle = self.__shapes[1]
        x, y, radius, xVelocity, yVelocity, yAcceleration = circle.getPosition()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and self.__energy >= 80:
                circle.getPosition()[3] = min(40, (pygame.mouse.get_pos()[0] - x) * .1)
                circle.getPosition()[4] = min(40, (y - pygame.mouse.get_pos()[1]) * .1)
                circle.getPosition()[5] = 0.8
                self.__energy -= 1
        if (self.__energy < 80) and (circle.getPosition()[3:] == [0, 0, 0]):
            self.__energy -= 1

    def applyWorldBorder(self):
        circle = self.__shapes[1]
        x, y, radius, xVelocity, yVelocity, yAcceleration = circle.getPosition()

        if not (- radius < x < self.__screen[0] + radius):
            circle.getPosition()[3], circle.getPosition()[4], circle.getPosition()[5] = 0, 0, 0

    def drawCircle(self):
        self.__shapes[1].draw(self.__surface)

        self.applyFrictionAndNormalForce()
        self.applyMotionAndGravity()
        self.applyTerminalVelocityAndLaunch()
        self.applyWorldBorder()

    def drawSquares(self):
        for square in self.__shapes[2]:
            square.draw(self.__surface)

            if square.isTouching(self.__shapes[1]):
                self.__shapes[2].remove(square)

    def drawCrosshair(self):
        pygame.draw.line(self.__surface, [200, 255, 255], self.__shapes[1].getPosition()[:2], pygame.mouse.get_pos(), 5)

    def drawScore(self):
        score = self.__font.render(
            '{:.0f}%'.format((self.__layers ** 2 - len(self.__shapes[2])) / self.__layers ** 2 * 100),
            True,
            [100, 100, 100]
        )
        hitbox = score.get_rect(center=(self.__screen[0] / 2, self.__screen[1] / 2))
        self.__surface.blit(score, hitbox)

    def drawSnowflakes(self):
        for snowflake in self.__shapes[3]:
            snowflake.draw(self.__surface)

            if snowflake.isTouching(self.__shapes[1]):
                self.__shapes[3].remove(snowflake)
                continue
            if not (0 < snowflake.getPosition()[0] < self.__screen[0]) and snowflake.isInFinalPosition(1):
                self.__shapes[3].remove(snowflake)
                continue

            if not snowflake.isInFinalPosition(1):
                snowflake.getPosition()[0] += snowflake.getPosition()[4]
                snowflake.getPosition()[1] += snowflake.getPosition()[5]
            if not snowflake.isInFinalPosition(3):
                snowflake.getPosition()[3] += 1
            else:
                self.__shapes[3].remove(snowflake)

    def play(self):
        self.initializeShapes()
        while self.__energy > 0:
            self.addSnowflake()

            self.drawBackground()
            self.drawFloor()
            self.drawCircle()
            self.drawSquares()
            self.drawCrosshair()
            self.drawScore()
            self.drawSnowflakes()
            pygame.display.update()
            self.__clock.tick(40)
