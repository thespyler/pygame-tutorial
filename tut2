import pygame
height = 800
width = 600
display = pygame.display.set_mode((height, width)) #design game window
		#r  g  b
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (122, 122, 122)

x = height / 2
y = width / 2
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
			if event.key == pygame.K_RIGHT:
				x += size
				# x = x + 20

			if event.key == pygame.K_LEFT:
				x -= size
	display.fill(black)
	display.fill(red, rect=[x, y, size, size])
	pygame.display.update()
