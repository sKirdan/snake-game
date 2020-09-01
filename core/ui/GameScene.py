from django.utils.termcolors import background

from lib.Scene import Scene
from lib.Widget import Widget


class GameScene(Scene):

    def setup(self):
        eat = Widget()
        eat.setBackground(image="eat.png")
        eat.setLayout(0.8, 0.6, .1, .1)



        background = Widget()
        background.setBackground(image="qq.jpg")
        background.setLayout(0, 0, 1, 1)

        self.addToScene(background)
        self.addToScene(eat)
