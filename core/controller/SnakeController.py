import pygame

from lib.Widget import Widget

from lib.Scene import Scene


class SnakeController:
    bodyProto: Widget = Widget()
    snakeArray: [Widget] = []
    prevDirection:() = (0, 1)

    def __init__(self, scene: Scene):
        self.scene = scene
        self.initSnake()

    def addChunk(self, widget:Widget):
        self.snakeArray.append(widget)
        self.scene.addToScene(widget)

    def initSnake(self):
        self.bodyProto.setBackground("#257826")
        self.bodyProto.setLayout(0.4, 0.3, 0.05, 0.05)

        body1 = self.bodyProto.clone()
        body1.box.offsetY = 0.2

        body2 = self.bodyProto.clone()
        body2.box.offsetY = 0.1



        headContainer = Widget()
        headContainer.setLayout(0.4, 0.4, 0.05, 0.05)
        headContainer.image.set_alpha(0)

        head1 = Widget()
        head1.setBackground("#257826")
        head1.setLayout(0, 0, 1, 0.5)

        head2 = Widget()
        head2.setBackground(image="snakeHead.png")
        head2.setLayout(0, 0, 1, 1)

        headContainer.addChild(head1)
        headContainer.addChild(head2)

        self.addChunk(headContainer)
        self.addChunk(self.bodyProto.clone())
        self.addChunk(body1)
        self.addChunk(body2)

    def test(self):
        i = len(self.snakeArray) - 1
        while i > 0:
            target = self.snakeArray[i - 1].clone()
            self.snakeArray[i].animator.moveRelative((target.box.offsetX, target.box.offsetY), 200)
            i -= 1

        direction = self.getDirection()

        if self.validateDirection(direction):
            self.prevDirection = direction
        head = self.snakeArray[0]
        head.animator.moveRelative((head.box.offsetX + 0.05 *self.prevDirection[0],
                                    head.box.offsetY + 0.05 *self.prevDirection[1]), 200)

    def validateDirection(self, direction):
        conflictedDirections = {(0, -1): (0, 1),
                                (0, 1): (0, -1),
                                (1, 0): (-1, 0),
                                (-1, 0): (1, 0)}

        if direction == None:
            return False
        elif conflictedDirections[self.prevDirection] == direction:
            return False

        return True

    def getDirection(self):

        directions = {pygame.K_UP: (0, -1),
                      pygame.K_DOWN: (0, 1),
                      pygame.K_RIGHT: (1, 0),
                      pygame.K_LEFT: (-1, 0)}

        pressedKeys = pygame.key.get_pressed()

        for direct in directions:
            if pressedKeys[direct]:
                return directions[direct]


