# Mouse-paintable window in 10, 11 and 12 lines

import pygame, sys, time
# Start the pygame system
pygame.init()

# This will be our canvas
screen = pygame.display.set_mode((800, 600))

while True:
	# Go through pygame's list of accumulated events since the last check
	for event in pygame.event.get():
		if event.type == pygame.QUIT:		# NOT NEEDED (but makes the close button work)
			sys.exit()						# NOT NEEDED (but makes the close button work)
		pass								# NOT NEEDED (if the above two lines are used)
	# See if the left mouse button is held down
	if pygame.mouse.get_pressed()[0]:
		# Draw a 2 pixel wide white line from the last known position to the current position
		pygame.draw.line(screen, (255, 255, 255), old_position, pygame.mouse.get_pos(), 2)
		# Update the window contents
		pygame.display.update()
	# Remember the last mouse position
	old_position = pygame.mouse.get_pos()

	time.sleep(0.1)						# NOT NEEDED (but stops the CPU getting overworked)

