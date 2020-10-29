#first we import pygame
import pygame


#then we have to initialize pygame
pygame.init()

#in this line we create our display "((800,600))"was pixels
screen=pygame.display.set_mode((800,600))

#this line creates game time
clock=pygame.time.Clock()


#in this line we we define bg variable as background img

bg=pygame.image.load("sky-full-stars-silhouettes-trees.jpg")

#then we have to create loop

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	#then we have to fill screen with any colour ,this is necessary		
	screen.fill((0,0,0))
	
	#in this line we have to draw background image
	screen.blit(bg,(0,0))
	
	#this is clock is a variable that we define on 12th line and FPS was in bracket
	clock.tick(30)
	
	#this we have to do update
	pygame.display.update()
