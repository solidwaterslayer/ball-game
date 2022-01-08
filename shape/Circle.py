import pygame

from shape.Shape import Shape


class Circle(Shape):
    def __init__(self, color, position):
        super().__init__(color, position)

    def getHitbox(self):
        x, y, radius = self.getPosition()[0], self.getPosition()[1], self.getPosition()[2]
        return pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius)

    def draw(self, surface):
        pygame.draw.circle(surface, self.getColor(), self.getPosition()[:2], self.getPosition()[2])
