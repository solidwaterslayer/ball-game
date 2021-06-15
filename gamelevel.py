import random
import time
import pygame
from rectangle import Rectangle
from circle import Circle
from snowflake import Snowflake

class GameLevel():
  def __init__(self, circleRadius, squareLength, squaresPerRow, snowflakeColor):
    self.__screen = [600, 450]
    self.__floor = int(self.__screen[1] * .8)
    self.__circleStartingPosition = [20, self.__floor]
    self.__surface = pygame.display.set_mode(self.__screen)

    self.__gravitationalAcceleration = 6.67
    self.__deltaTime = 0.1

    self.__font = pygame.font.SysFont('Comic Sans MS', 100)
    self.__clock = pygame.time.Clock()

    self.__circleRadius = circleRadius
    self.__squareLength = squareLength
    self.__squaresPerRow = squaresPerRow
    self.__snowflakeColor = snowflakeColor

  def __str__(self):
    return 'GameState(%r, %r, %r, %r)' % (
      self.__circleRadius,
      self.__squareLength,
      self.__squaresPerRow,
      self.__snowflakeColor
    )

  def getShapes(self):
    shapes = [Circle((80, 30, 30), self.__circleStartingPosition, self.__circleRadius)]

    lengthPerRow = self.__squareLength * self.__squaresPerRow;
    squarePosition = [
      self.__screen[0] - self.__squareLength * (self.__squaresPerRow + 2),
      self.__floor - lengthPerRow
    ]
    for i in range (0, lengthPerRow, self.__squareLength):
      for j in range (0, lengthPerRow, self.__squareLength):
        x = squarePosition[0]
        y = squarePosition[1]

        shapes.append(Rectangle(
          [200, 200, 150],
          [x + i, y + j],
          self.__squareLength,
          self.__squareLength)
        )

    return shapes

  def drawBackground(self, shapes):
    self.__surface.fill([220, 220, 220])
    pygame.draw.rect(
      self.__surface,
      [200, 255, 200],
      [0, self.__floor, self.__screen[0], self.__screen[1] - self.__floor]
    )
    if (random.randint(0, 3) == 2):
      shapes.append(Snowflake(
        self.__snowflakeColor,
        [random.randint(0, self.__screen[0]), 0],
        5,
        random.randint(self.__floor, self.__screen[1]),
        0,
        600
      ))

  def drawShapes(self, shapes):
    score = 0

    for shape in shapes:
      shape.draw(self.__surface)

      if (shapes[0].isTouched(shape)):
        if isinstance(shape, Rectangle):
          score += 1

        shapes.remove(shape)
        continue
      
      if isinstance(shape, Snowflake):
        if not shape.isGrounded():
          shape.setPosition(
            [shape.getPosition()[0],
            shape.getPosition()[1] + random.randint(5, 10)]
          )
        if shape.isMelted():
          shapes.remove(shape)
        
        shape.setTemperature(shape.getTemperature() + 1)

    return score

  def drawCrosshair(self, circle):
    pygame.draw.line(
      self.__surface,
      [200, 255, 255],
      circle.getPosition(),
      pygame.mouse.get_pos(),
      5
    )

  def drawScore(self, score):
    self.__surface.blit(
      self.__font.render(
        str(int(score / self.__squaresPerRow ** 2 * 100)) + '%', True,
        [100, 100, 100]
      ),
      [int(self.__screen[0] * .40),
      int(self.__screen[1] * .43)]
    )
  
  def handleCircleLaunchEvent(self, circleVelocity):
    for event in pygame.event.get():
      if (event.type == pygame.MOUSEBUTTONUP):
        if (circleVelocity[0] == 0 and circleVelocity[1] == 0):
          circleVelocity[0] = pygame.mouse.get_pos()[0] - self.__circleStartingPosition[0]
          circleVelocity[1] = self.__circleStartingPosition[1] - pygame.mouse.get_pos()[1]

  def handleCircleFlyingEvent(self, circle, circleVelocity, levelTransitionDelay):
    if (circleVelocity[0] != 0 and circleVelocity[1] != 0):
      if (circle.isTouched(Rectangle([0, 0, 0, 0], [0, 0], self.__screen[0], self.__floor))):
        circleVelocity[1] -= self.__gravitationalAcceleration * self.__deltaTime
        circle.setPosition(
          [circle.getPosition()[0] + int(self.__deltaTime * circleVelocity[0]),
          circle.getPosition()[1] - int(self.__deltaTime * circleVelocity[1])]
        )
      else:
        return levelTransitionDelay - 1
    return levelTransitionDelay

  def run(self):
    shapes = self.getShapes()
    score = 0
    
    circleVelocity = [0, 0]
    
    levelTransitionDelay = 100
    while levelTransitionDelay > 0:
      self.drawBackground(shapes)
      score += self.drawShapes(shapes)
      self.drawCrosshair(shapes[0])
      self.drawScore(score)

      self.handleCircleLaunchEvent(circleVelocity)
      levelTransitionDelay = self.handleCircleFlyingEvent(shapes[0], circleVelocity, levelTransitionDelay)

      pygame.display.update()
      self.__clock.tick(40)
    
    time.sleep(0.5)
