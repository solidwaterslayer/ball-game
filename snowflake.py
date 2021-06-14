import pygame
from circle import Circle

class Snowflake(Circle):
  def __init__(self, color, position, radius, fallLimit=None, temperature=None, meltingPoint=None):
    super().__init__(color, position, radius)
    self.__fallLimit = fallLimit
    self.__temperature = temperature
    self.__meltingPoint = meltingPoint

  def isGrounded(self):
    return self.getPosition()[1] >= self.__fallLimit

  def getTemperature(self):
    return self.__temperature

  def setTemperature(self, temperature):
    self.__temperature = temperature

  def isMelted(self):
    return self.__temperature >= self.__meltingPoint

  def __str__(self):
    return 'Snowflake(%r, %r, %r, %r, %r, %r)' % (
      self.getColor(),
      self.getPosition(),
      self.getRadius(),
      self.__fallLimit,
      self.__temperature,
      self.__meltingPoint
    )

  def draw(self, surface):
    x = self.getPosition()[0]
    y = self.getPosition()[1]

    pygame.draw.line(
      surface,
      self.getColor(),
      [x - self.getRadius(), y],
      [x + self.getRadius(), y]
    )
    pygame.draw.line(
      surface,
      self.getColor(),
      [x, y - self.getRadius()],
      [x, y + self.getRadius()]
    )
    pygame.draw.line(
      surface,
      self.getColor(),
      [x - self.getRadius(), y - self.getRadius()],
      [x + self.getRadius(), y + self.getRadius()]
    )
    pygame.draw.line(
      surface,
      self.getColor(),
      [x - self.getRadius(), y + self.getRadius()],
      [x + self.getRadius(), y - self.getRadius()]
    )

  def getHitbox(self):
    return pygame.Rect(
      self.getPosition()[0] - self.getRadius(),
      self.getPosition()[1] - self.getRadius(),
      self.getRadius() * 2,
      self.getRadius() * 2
    )
