import random
import time

import pygame

from level.Level import Level

if __name__ == '__main__':
    radius = [5, 80, 140]
    lengths = [13, 26, 52]
    layers = [5, 10]
    snowflakeColors = [[50, 10, 10], [255, 255, 255]]
    wind = [-20, -12, -5, 5, 12, 20]

    pygame.init()
    pygame.font.init()
    while True:
        gameLevel = Level(
            radius[random.randint(0, len(radius) - 1)],
            lengths[random.randint(0, len(lengths) - 1)],
            layers[random.randint(0, len(layers) - 1)],
            snowflakeColors[random.randint(0, len(snowflakeColors) - 1)],
            wind[random.randint(0, len(wind) - 1)]
        )
        gameLevel.run()
        time.sleep(0.5)
