from core.Snake import Snake
from core.Food import Food
from core.Mouse import Mouse
import random
import pygame

class Controller:

	global display
	global snake
	global mouse

	rects = {"snake": None, "food": None, "mouse": None}
	foods = []
	prevDirection = (0, -1)

	def __init__(self, display):
		self.display = display
		self.snake = Snake((200, 200))
		self.mouse = Mouse(display)
		self.generateFood()

	def getDirection():
		directions = {pygame.K_UP:(0, -1), 
					  pygame.K_DOWN:(0, 1), 
					  pygame.K_RIGHT:(1, 0), 
					  pygame.K_LEFT:(-1, 0)}

		pressedKeys = pygame.key.get_pressed()

		for direct in directions:
			if pressedKeys[direct]:
				return directions[direct]

	def prepareNextStep(self):
		direction = Controller.getDirection()

		if self.validateDirection(direction):
			self.prevDirection = direction

		self.display.clear()

		self.calculateSnakeStep(self.prevDirection)

		self.mouse.calcalculateMouseStep()
		

		if self.validateRects():
			del self.foods[0]
			self.generateFood()
			self.snake.addChunk(self.prevDirection)

		if self.validateMouse():
			del self.snake
			self.snake = Snake((200, 200))

		self.paintSnake()
		self.paintFood()
		self.mouse.paint(self.display)

	def validateRects(self):
		self.rects["snake"] = self.display.paint(self.snake.headPosition(), self.snake.dimensions)
		self.rects["food"] = self.display.paint(self.foods[0].pos, self.foods[0].dimensions)
		return self.rects["snake"].colliderect(self.rects["food"])

	def validateMouse(self):
		self.rects["snake"] = self.display.paint(self.snake.headPosition(), self.snake.dimensions)
		self.rects["mouse"] = self.display.paint(self.mouse.pos, self.mouse.dimensions)
		return self.rects["snake"].colliderect(self.rects["mouse"])


	def paintSnake(self):
		for pos in self.snake.position:
			self.display.paint(pos, self.snake.dimensions)
		self.display.paint(self.snake.headPosition(), self.snake.dimensions, color = (20, 170, 20))
		self.paintSnakeFace(self.snake.headPosition(), self.snake.dimensions)

	def paintSnakeFace(self, headPos, headSize, color = (0, 0, 0)):
		self.display.paint((headPos[0] + headSize[0]*0.2, headPos[1] + headSize[1]*0.2), 
						  (headSize[0]*0.2, headSize[1]*0.2), color)
		self.display.paint((headPos[0] + headSize[0]*0.6, headPos[1] + headSize[1]*0.2), 
						  (headSize[0]*0.2, headSize[1]*0.2), color)
		self.display.paint((headPos[0] + headSize[0]*0.3, headPos[1] + headSize[1]*0.6), 
						  (headSize[0]*0.4, headSize[1]*0.3), color)

	def paintFood(self):
		for food in self.foods:
			self.display.paint(food.pos, food.dimensions, color = (255, 0, 0))

	def calculateSnakeStep(self, direction):
		self.snake.calculatePosition(direction)
		self.snake.updateHeadPos(self.display.invalidatePos(self.snake.headPosition()))

	def validateDirection(self, direction):
		conflictedDirections = {(0, -1):(0, 1),
					  			(0, 1):(0, -1), 
					  			(1, 0):(-1, 0), 
					  			(-1, 0):(1, 0)}

		if direction == None:
			return False
		elif conflictedDirections[self.prevDirection] == direction:
			return False

		return True

	def generateFood(self):
		self.foods.append(Food((random.randrange(10, self.display.width - 10), 
						   		random.randrange(10, self.display.height - 10))))