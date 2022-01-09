import random
import time

import pygame

from level.Level import Level

if __name__ == '__main__':
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
        gameLevel = Level(
            circleRadiusChoices[random.randint(0, 3)],
            squareLengthChoices[random.randint(0, 2)],
            squaresPerRowChoices[random.randint(0, 1)],
            snowflakeColorChoices[random.randint(0, 2)]
        )
        gameLevel.run()
        time.sleep(0.5)
