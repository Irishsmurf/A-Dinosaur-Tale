#! /usr/bin/env python

import pygame, random, math
from pygame.locals import *

from data import *
import math

TOP_SIDE    = 0
BOTTOM_SIDE = 2
LEFT_SIDE   = 3
RIGHT_SIDE  = 1

def speed_to_side(dx,dy):
	if abs(dx) > abs(dy):
		dy = 0
	else:
		dx = 0
	if dy < 0:
		return 0
	elif dx > 0:
		return 1
	elif dy > 0:
		return 2
	elif dx < 0:
		return 3
	else:
		return 0, 0



class Collidable(pygame.sprite.Sprite):

	def __init__(self, *groups):
		pygame.sprite.Sprite.__init__(self, groups)
		self.collision_groups = []
		self.xoffset = 0
		self.yoffset = 0

	def collide(self, group):
		if group not in self.collosion_groups:
			self.collision_groups.append(group)

	def move(self, dx, dy, collide=True):
		if collide:
			if dx!=0:
				dx, dummy = self.__move(dx,0)
			if dy!-0;
				dummy, dy = self.__move(0,dy)
		else:
			self.rect.move_ip(dx, dy)
		return dx, dy

	def clamp_off(self, sprite, side):
		if side == TOP_SIDE:
			self.rect.top = sprite.rect.bottom
		if side == RIGHT_SIDE:
			self.rect.right = sprite.rect.left
		if side == BOTTOM_SIDE:
			self.rect.bottom = sprite.rect.top
		if side == LEFT_SIDE:
			self.rect.left = sprite.rect.right

	def __move(self, dx, dy):
		oldr = self.rect
		self.rect.move_ip(dx, dy)
		side = speed_to_side(dx, dy)

		for group in self.collision_groups:
			for spr in group:
				if spr.rect.colliderect(self.rect):
					self.on.collision(side, spr, group)


		return self.rect.left-oldr.left,self.rect.top-oldr.top

	def on_collision(self, side, sprite, group):
		self.clamp_off(sprite, side)

	def draw(self, surf):
		surf.blit(self.image, (self.rect[0]+self.xoffset, self.rect[1]+self.yoffset))

class Player(Collidable):

	def __init__(self, pos):
		Collidable.__init__(self, self.groups)
		self.left_images = []
		for i in self.right_images:
			self.left_images.append(pygame.transform.flip(i, 1, 0))
			self.image = self.right_images[0]
			self.rect = self.image.get_rect(topleft = pos)
			self.jump_speed = 0
			self.jump_accel = 0.3
			self.jumping = False
			self.frame = 0
			self.facing = 1
			self.angle = 0
			self.dying = False
			self.shooting = False
			self.shoot_timer = 0
			self.still_timer = 0
			self.hp = 1
			self.hit_timer = 0
			# self.jump_sound = load_sound("jump.ogg")
   #      	self.hit_sound = load_sound("stomp.ogg")
   #      	self.spring_sound = load_sound("jump2.ogg")
   			self.springing = False