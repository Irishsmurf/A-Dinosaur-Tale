import sys
import pygame
from pygame.locals import *

from game import *
from ezmenu import *
from data import *
from cutscenes import *

def RunGame(screen):
	Game(screen)
	#play_music("sqwuak.ogg", 0.75)

def ContinueGame(screen):
	Game(screen, True)
	#play_music("sqwuak.ogg", 0.75)

def Help(screen):
	cutscene(screen, ["HELP",
		"",
		"Move: Arrow Keys",
		"Jump: z"
	])

class Menu:
	def __init__(self, screen):
		self.screen = screen
		self.menu = EzMenu(["NEW GAME", lambda: RunGame(screen)], ["CONTINUE GAME", lambda: ContinueGame(screen)], ["HELP", lambda: Help(screen)], ["QUIT GAME", lambda: sys.exit(0)])
		self.menu.set_highlight_color((255, 0, 0))
		self.menu.set_normal_color((255, 255, 255))
		self.menu.center_at(300, 400)
		self.menu.set_font(pygame.font.Font(filepath("fonts/font.ttf"), 16))
		self.bg = load_image_smaller("graphics/menu_background.png", 1)
		self.font = pygame.font.Font(filepath("fonts/font.ttf"), 16)
		self.font2 = pygame.font.Font(filepath("fonts/Jurassic-Park.ttf"), 90)
		#play_music("title.ogg", 0.75)
		self.clock = pygame.time.Clock()
		events = pygame.event.get()
		self.menu.update(events)
		self.menu.draw(self.screen)
		self.main_loop()

	def main_loop(self):
		while 1:
			self.clock.tick(40)
			events = pygame.event.get()
			self.menu.update(events)
			for e in events:
				if e.type == QUIT:
					pygame.quit()
					return
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					pygame.quit()
					return
				
			self.screen.blit(self.bg, (0, 0))
			ren = self.font.render("GAMECRAFT", 1, (255, 255, 255))
			self.screen.blit(ren, (320-ren.get_width()/2, 70))

			ren = self.font2.render("A DINOSAUR", 1, (255, 255, 255))
			self.screen.blit(ren, (320-ren.get_width()/2, 120))

			ren = self.font2.render("TALE", 1, (255, 255, 255))
			self.screen.blit(ren, (320-ren.get_width()/2, 175))

			self.menu.draw(self.screen)
			pygame.display.flip()
