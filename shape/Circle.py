import pygame
from shape.Shape import Shape


class Circle(Shape):
    def __init__(self, color, position, radius):
        super().__init__(color, position)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def __str__(self):
        return 'Circle(%r, %r, %r)' % (self.getColor(), self.getPosition(), self.__radius)

    def draw(self, surface):
        pygame.draw.circle(surface, self.getColor(), self.getPosition(), self.__radius)

    def getHitbox(self):
        return pygame.Rect(
            self.getPosition()[0] - self.__radius,
            self.getPosition()[1] - self.__radius,
            self.__radius * 2,
            self.__radius * 2
        )
