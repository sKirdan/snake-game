from django.utils.termcolors import background

from lib.Scene import Scene
from lib.Widget import Widget


class GameScene(Scene):

    def setup(self):
        eat = Widget()
        eat.setBackground(image="eat.png")
        eat.setLayout(0.8, 0.6, .1, .1)

        body = Widget()
        body.setBackground(image="body.png")
        body.setLayout(0.4, 0.3, 0.1, 0.1)

        bodyX = body.clone()
        bodyX.box.offsetX = 0.4
        bodyX.box.offsetY = 0.2

        head = Widget()
        head.setBackground(image="SnakeHead.png")
        head.setLayout(0.4, 0.4, 0.1, 0.1)


        background = Widget()
        background.setBackground(image="qq.jpg")
        background.setLayout(0, 0, 1, 1)

        self.addToScene(background)
        self.addToScene(head)
        self.addToScene(body)
        self.addToScene(bodyX)
        self.addToScene(eat)

