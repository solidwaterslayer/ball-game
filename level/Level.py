import random
import sys

import pygame

from shape.Circle import Circle
from shape.Rectangle import Rectangle
from shape.Snowflake import Snowflake


class Level:
    def __init__(self, radius, length, layers, snowflakeColor):
        self.__radius = radius
        self.__length = length
        self.__layers = layers
        self.__snowflakeColor = snowflakeColor

        self.__screen = [900, 450]
        self.__surface = pygame.display.set_mode(self.__screen)
        self.__shapes = []
        self.__font = pygame.font.SysFont('Comic Sans MS', 100)

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
        if random.randint(0, 3) == 0:
            self.__shapes[3].append(Snowflake(
                self.__snowflakeColor,
                [random.randint(0, self.__screen[0]), 0, 5, 0],
                [None, random.randint(self.__shapes[0].getPosition()[1], self.__screen[1]), None, 600]
            ))

    def drawBackground(self):
        self.__surface.fill([220, 220, 220])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

    def drawFloor(self):
        self.__shapes[0].draw(self.__surface)

    def drawCircle(self):
        circle = self.__shapes[1]
        circle.draw(self.__surface)

        if circle.getPosition()[3] != 0 and circle.getPosition()[4] != 0:
            circle.getPosition()[0] += circle.getPosition()[3]
            circle.getPosition()[1] -= circle.getPosition()[4]
            circle.getPosition()[4] += circle.getPosition()[5]
        for event in pygame.event.get():
            if circle.getPosition()[3] == 0 and circle.getPosition()[4] == 0 and event.type == pygame.MOUSEBUTTONUP:
                circle.getPosition()[3] = pygame.mouse.get_pos()[0] - circle.getPosition()[0]
                circle.getPosition()[4] = circle.getPosition()[1] - pygame.mouse.get_pos()[1]
                circle.getPosition()[5] = 20

    def drawCrosshair(self):
        pygame.draw.line(self.__surface, [200, 255, 255], self.__shapes[1].getPosition()[:2], pygame.mouse.get_pos(), 5)

    def drawSquares(self):
        for square in self.__shapes[2]:
            square.draw(self.__surface)

            if square.isTouching(self.__shapes[1]):
                self.__shapes[2].remove(square)

    def drawScore(self):
        self.__surface.blit(
            self.__font.render(
                '{:.0f}%'.format(len(self.__shapes[2]) / self.__layers ** 2 * 100),
                True,
                [100, 100, 100]
            ),
            [int(self.__screen[0] * .40),
             int(self.__screen[1] * .43)]
        )

    def drawSnowflakes(self):
        for snowflake in self.__shapes[3]:
            snowflake.draw(self.__surface)

            if snowflake.isTouching(self.__shapes[1]):
                self.__shapes[3].remove(snowflake)
            snowflake.getPosition()[3] += 1
            if not snowflake.isInFinalPosition(1):
                snowflake.getPosition()[1] += random.randint(5, 10)
            if snowflake.isInFinalPosition(3):
                self.__shapes[3].remove(snowflake)

    def run(self):
        self.initializeShapes()
        while True:
            self.addSnowflake()

            self.drawBackground()
            self.drawFloor()
            self.drawCircle()
            self.drawCrosshair()
            self.drawSquares()
            self.drawScore()
            self.drawSnowflakes()
            pygame.display.update()
            self.__clock.tick(40)
