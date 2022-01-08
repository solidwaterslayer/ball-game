import pygame

from shape.Shape import Shape


class Rectangle(Shape):
    def __init__(self, color, position):
        super().__init__(color, position)

    def getHitbox(self):
        return pygame.Rect(self.getPosition())

    def draw(self, surface):
        pygame.draw.rect(surface, self.getColor(), self.getHitbox())
