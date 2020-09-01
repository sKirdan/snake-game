import pygame

from core.controller.SnakeController import SnakeController
from core.ui.GameScene import GameScene
from lib.Engine import Engine


class GameCycle:

    @staticmethod
    def start():
        Engine.init()

        display = pygame.display.set_mode((500, 500))

        currentScene = GameScene(display)
        snakeController = SnakeController(currentScene)
        while not GameCycle.gameEnd():
            currentScene.render()
            Engine.performTick()
            snakeController.test()

        pygame.quit()

    @staticmethod
    def gameEnd():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return True
