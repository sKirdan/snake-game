from lib.animations.Animation import Animation
from lib.animations.AnimationMove import AnimationMove


class Animator:
    widget: object

    currentAnimation: Animation

    def __init__(self, widget):
        self.widget = widget

        self.currentAnimation = None

    def update(self):
        if self.currentAnimation:
            if not self.currentAnimation.update():
                self.currentAnimation = None

    def moveRelative(self, pos: (), mls: int):
        if self.currentAnimation:
            return
        pointB = self.widget.clone()
        pointB.box.offsetX = pos[0]
        pointB.box.offsetY = pos[1]
        pointA = self.widget.clone()
        self.currentAnimation = AnimationMove(self.widget).From(pointA).To(pointB).Duration(mls)

        self.currentAnimation.start()
