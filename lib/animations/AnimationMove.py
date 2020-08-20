from lib.Engine import Engine
from lib.animations.Animation import Animation


class AnimationMove(Animation):

    def update(self) -> bool:

        leftTime = self._EndTime - Animation.current_time_millis()
        frames = (self.Duration * Engine.fps) / 1000

        if leftTime > 0:
            deltaX = (self.To.box.offsetX - self.From.box.offsetX) / frames
            deltaY = (self.To.box.offsetY - self.From.box.offsetY) / frames
            self.Widget.box.offsetX += deltaX
            self.Widget.box.offsetY += deltaY
            return True
        else:
            self.Widget.box.offsetX = self.To.box.offsetX
            self.Widget.box.offsetY = self.To.box.offsetY
            return False
