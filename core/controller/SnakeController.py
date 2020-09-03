import pygame

from lib.Widget import Widget

from lib.Scene import Scene


class SnakeController:
    snakeSize: float = 0.05
    bodyProto: Widget = Widget()
    snakeArray: [Widget] = []
    prevDirection: () = (0, 1)

    def __init__(self, scene: Scene):
        self.scene = scene
        self.initSnake()

    def addChunk(self, widget: Widget):
        widget.box = self.snakeArray[-1].box.clone()
        self.snakeArray.append(widget)
        self.scene.addToScene(widget)

    def initSnake(self):
        self.bodyProto.setBackground("#257826")
        self.bodyProto.setLayout(0.4, 0.3, self.snakeSize, self.snakeSize)

        headContainer = Widget()
        headContainer.setLayout(0.4, 0.4, self.snakeSize, self.snakeSize)
        headContainer.image.set_alpha(0)

        head1 = Widget()
        head1.setBackground("#257826")
        head1.setLayout(0, 0, 1, 0.5)

        head2 = Widget()
        head2.setBackground(image="snakeHead.png")
        head2.setLayout(0, 0, 1, 1)

        headContainer.addChild(head1)
        headContainer.addChild(head2)

        self.snakeArray.append(headContainer)
        self.scene.addToScene(headContainer)
        self.snakeArray.append(self.bodyProto)
        self.scene.addToScene(self.bodyProto)
        self.addChunk(self.bodyProto.clone())


    def test(self):
        print(str(self.snakeArray[2].box.offsetX) + ' ' + str(self.snakeArray[2].box.offsetY))
        if self.snakeArray[0].animator.currentAnimation:
            return
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.addChunk(self.bodyProto.clone())
        i = len(self.snakeArray) - 1
        while i > 0:
            target = self.snakeArray[i - 1].clone()
            self.snakeArray[i].animator.moveRelative((target.box.offsetX, target.box.offsetY), 200)
            i -= 1

        direction = self.getDirection()

        if self.validateDirection(direction):
            self.prevDirection = direction
        head = self.snakeArray[0]
        head.animator.moveRelative((head.box.offsetX + self.snakeSize * self.prevDirection[0],
                                    head.box.offsetY + self.snakeSize * self.prevDirection[1]), 200)

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
