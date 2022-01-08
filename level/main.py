import random

import pygame

from gamelevel import GameLevel

circleRadiusChoices = [5, 20, 80, 360]
squareLengthChoices = [13, 26, 52]
squaresPerRowChoices = [5, 10]
snowflakeColorChoices = [
  [50, 10, 10],
  [200, 200, 255],
  [255, 255, 255]
]

pygame.init()
pygame.font.init()
while (True):
  gameLevel = GameLevel(
    circleRadiusChoices[random.randint(0, 3)],
    squareLengthChoices[random.randint(0, 2)],
    squaresPerRowChoices[random.randint(0, 1)],
    snowflakeColorChoices[random.randint(0, 2)]
  )
  gameLevel.run()
