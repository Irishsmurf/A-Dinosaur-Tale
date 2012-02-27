import os
import sys

import pygame
from pygame.locals import *
from level import *

class Camera(object):
	
	def __init(self, player, width):
		self.player = player
		self.rect = pygame.display.get.surface().get_rect()
		self.world = Rect(0, 0, width, 480)
		selfrect.center = self.player.rect.center

	def update(self):
		if self.player.rect.centerx > self.rect.centerx+64:
			self.rect.centerx = self.player.rect.centerx-64
        if self.player.rect.centerx < self.rect.centerx-64:
        	self.rect.centerx = self.player.rect.centerx+64
        if self.player.rect.centery > self.rect.centery+64:
        	self.rect.centery = self.player.rect.centery-64
        if self.player.rect.centery < self.rect.centery-64:
        	self.rect.centery = self.player.rect.centery+64
        self.rect.clamp_ip(self.world)

    def draw_sprites(self, surf, sprites):
	    for s in sprites:
	    	if s.rect.colliderect(self.rect):
	    		surf.blit(s.image, RelRect(s, self))

class Game(object):

	def __init__(self, screen, continuing=False):

		self.screen = screen
		self.sprites = pygame.sprite.OrderedUpdates()
		self.players = pygame.sprite.OrderedUpdates()
		self.platforms = pygame.sprite.OrderedUpdates()
		self.grass = pyame.sprite.OrderedUpdates()

		Player.right_images = [load_image("veggie_raptor_1.png")]
		Platform.images = {"platform-top.png": load_image("platform-top.png"),
		                   "platform-middle.png": load_image("platform-top.png")}
		Grass.images = {"grass-1.png": load_image("grass-1.png"),
		                "grass-middle.png": load_image("grass-middle.png")}

		self.screen.fill((0, 0, 0))
		# self.draw_stats()
		pygame.display.flip()
		pygame.time.wait(2500)
		self.main_loop()

	def end(self):
		self.running = 0

	def clear_sprites(self):
		for s in self.sprites:
			pygame.sprite.Sprite.kill(s)

	def main_loop(self):

		while self.running:
			if not self.running:
				return

			self.clock.tick(60)
			self.camera.update()
			for s in self.sprites:
				s.update()

			for p in self.platforms:
				p.update()
			self.player.collide(self.springs)
			self.player.collide(self.platforms)

			for g in self.grass:
				g.update()
			self.player.collide(self.grass)

			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit()
				if e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						self.end()
					if e.key == K_z:
						self.player.jump()
			if not self.running:
				return
			self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640, 0))
            self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640 + 640, 0))
            self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640 - 640, 0))
            self.camera.draw_sprites(self.screen, self.sprites)

            pygame.display.flip()
            if not self.running:
                return
	# def draw_stats(self):
	# 	for i in range(1):
	# 		self.screen.blit(self.heart2, (16 + *34, 16))
	# 	for i in range(self.player.hp):
	# 		self.screen.blit(self.heroimg, (313, 16))


#we give all(more or less) credit to the inventors sans craigs hard work ok craig FUCK
