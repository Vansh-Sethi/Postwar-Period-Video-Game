import math, random, sys
import pygame
from pygame.locals import *
from pygame_functions  import *
from Asian import asianGame
from Solider import SoliderGame
from Woman import womanGame
from Bman import bmanGame

screenSize(1280,720)
setBackgroundImage("C:/Users/vansh/Desktop/gameforHistory/assets/intro.png")
button1 = pygame.Rect(393, 136, 472, 97)
button2 = pygame.Rect(391, 270, 472, 97)
button3 = pygame.Rect(393, 409, 472, 97)
button4 = pygame.Rect(393, 551, 472, 97)

def fix():
	screenSize(1280,720)
	setBackgroundImage("C:/Users/vansh/Desktop/gameforHistory/assets/intro.png")
	button1 = pygame.Rect(393, 136, 472, 97)
	button2 = pygame.Rect(391, 270, 472, 97)
	button3 = pygame.Rect(393, 409, 472, 97)
	button4 = pygame.Rect(393, 551, 472, 97)

while True:
    
	for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
				if button1.collidepoint(mouse_pos):
					a = asianGame()
					fix()

				if button2.collidepoint(mouse_pos):
					womanGame()
					fix()

				if button3.collidepoint(mouse_pos):
					bmanGame()
					fix()

				if button4.collidepoint(mouse_pos):
					SoliderGame()
					fix()



	
	