import pygame

from shape.Circle import Circle


class Snowflake(Circle):
    def __init__(self, color, position, fallLimit=None, temperature=None, meltingPoint=None):
        super().__init__(color, position)
        self.__fallLimit = fallLimit
        self.__temperature = temperature
        self.__meltingPoint = meltingPoint

    def draw(self, surface):
        x, y, radius = self.getPosition()[0], self.getPosition()[1], self.getPosition()[2]
        left, right, top, bottom = x - radius, x + radius, y + radius, y - radius

        pygame.draw.line(surface, self.getColor(), [left, y], [right, y])
        pygame.draw.line(surface, self.getColor(), [x, top], [x, bottom])
        pygame.draw.line(surface, self.getColor(), [left, bottom], [right, top])
        pygame.draw.line(surface, self.getColor(), [left, top], [right, bottom])

    def isGrounded(self):
        return self.getPosition()[1] >= self.__fallLimit

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature

    def isMelted(self):
        return self.__temperature >= self.__meltingPoint
