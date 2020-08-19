import pygame
from pygame.time import Clock


class Engine:
    fps: int = 200
    clock: Clock

    @staticmethod
    def init():
        pygame.init()
        Engine.clock = pygame.time.Clock()

    @staticmethod
    def performTick():
        Engine.clock.tick(Engine.fps)
