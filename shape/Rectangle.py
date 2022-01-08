import pygame
from shape.Shape import Shape


class Rectangle(Shape):
    def __init__(self, color, position, height, width):
        super().__init__(color, position)
        self.__height = height
        self.__width = width

    def __str__(self):
        return 'Ball(%r, %r, %r, %r)' % (self.getColor(), self.getPosition(), self.__height, self.__width)

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.getColor(),
            [
                self.getPosition()[0],
                self.getPosition()[1],
                self.__height,
                self.__width
            ]
        )

    def getHitbox(self):
        return pygame.Rect(self.getPosition()[0], self.getPosition()[1], self.__height, self.__width)
