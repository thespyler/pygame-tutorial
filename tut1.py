import pygame
display = pygame.display.set_mode((800, 600)) #design game window
		#r  g  b
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (122, 122, 122)

x = 400
y = 300
size = 20
game_on = True

#gameloop
while game_on:
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x -= 20


	display.fill(black)
	display.fill(red, rect=[x, y, size, size])
	# display.fill(blue, rect=[400, 400, 50, 100])

	pygame.display.update()
