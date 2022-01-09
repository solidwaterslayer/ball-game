import pygame

from shape.Circle import Circle


class Snowflake(Circle):
    def __init__(self, color, position, finalPosition = None):
        super().__init__(color, position)
        self.__finalPosition = finalPosition

    def draw(self, surface):
        x, y, radius = self.getPosition()[0], self.getPosition()[1], self.getPosition()[2]
        left, right, top, bottom = x - radius, x + radius, y + radius, y - radius

        pygame.draw.line(surface, self.getColor(), [left, y], [right, y])
        pygame.draw.line(surface, self.getColor(), [x, top], [x, bottom])
        pygame.draw.line(surface, self.getColor(), [left, bottom], [right, top])
        pygame.draw.line(surface, self.getColor(), [left, top], [right, bottom])

    def isInFinalPosition(self, i):
        return self.__finalPosition is not None and self.getPosition()[i] >= self.__finalPosition[i]
