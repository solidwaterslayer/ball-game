from abc import ABC, abstractmethod

class Shape(ABC):
  def __init__(self, color, position):
    self.__color = color
    self.__position = position

  def getColor(self):
    return self.__color

  def getPosition(self):
    return self.__position

  def setPosition(self, position):
    self.__position = position

  @abstractmethod
  def draw(self, surface):
    pass

  @abstractmethod
  def getHitbox(self):
    pass

  def isTouched(self, shape):
    if (self is shape):
      return False

    hitbox0 = self.getHitbox()
    hitbox1 = shape.getHitbox()

    return (
      (hitbox0.x < hitbox1.x + hitbox1.width) and
      (hitbox0.y < hitbox1.y + hitbox1.height) and
      (hitbox1.x < hitbox0.x + hitbox0.width) and
      (hitbox1.y < hitbox0.y + hitbox0.height)
    )
