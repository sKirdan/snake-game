import pygame

from core.ui.MainScene import MainScene
from lib.Engine import Engine
from lib.animations.Animation import Animation


class GameCycle:
    currentScene: MainScene = None

    @staticmethod
    def start():
        Engine.init()

        display = pygame.display.set_mode((500, 500))

        pygame.time.wait(2000)

        currentScene = MainScene(display)
        GameCycle.currentScene = currentScene
        time = Animation.current_time_millis()
        while not GameCycle.gameEnd():
            print(str(Animation.current_time_millis() - time) + " mls")
            time = Animation.current_time_millis()
            currentScene.render()
            Engine.performTick()

        pygame.quit()
        quit()

    @staticmethod
    def gameEnd():
        for event in pygame.event.get():
            if GameCycle.currentScene and pygame.key.get_pressed()[pygame.K_0]:
                GameCycle.currentScene.test()
            if event.type == pygame.QUIT:
                return True
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return True
