from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    def getColor(self):
        return self.__color

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    @abstractmethod
    def getHitbox(self):
        pass

    def isTouching(self, shape):
        if self is shape:
            return False

        return self.getHitbox().colliderect(shape.getHitbox())

    @abstractmethod
    def draw(self, surface):
        pass
