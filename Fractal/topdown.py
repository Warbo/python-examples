import random, pygame, time
pygame.init()
screen = pygame.display.set_mode((600,600))

class Square:

	def __init__(self, side, topleft, height):
		self.side = side
		self.topleft = topleft
		self.height = height

	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255 / self.height, 0), (self.topleft, (self.side, self.side)))

	def subdivide(self):
		new_squares = []
		new_squares.append(Square(self.side/2, self.topleft, self.height + random.randint(-1, 1)))
		new_squares.append(Square(self.side/2, (self.topleft[0] + self.side/2, self.topleft[1]), self.height + random.randint(-1, 1)))
		new_squares.append(Square(self.side/2, (self.topleft[0], self.topleft[1] + self.side/2), self.height + random.randint(-1, 1)))
		new_squares.append(Square(self.side/2, (self.topleft[0] + self.side/2, self.topleft[1] + self.side/2), self.height + random.randint(-1, 1)))
		return new_squares

square = Square(600, (0, 0), 128)
#subdivided = []
square.draw(screen)
subdivided1 = square.subdivide()
subdivided2 = []
for subsquare in subdivided1:
	subdivided2.append(subsquare.subdivide())
for subsquare in subdivided2:
	for element in subsquare:
		element.draw(screen)
pygame.display.update()
while True:
	time.sleep(1)
