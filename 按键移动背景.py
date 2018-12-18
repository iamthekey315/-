#Python 3.7 
# -*- coding: utf-8 -*-
# @Date    : 2018-11-26 18:16:32
# @Author  : sjp (3152506@qq.com)
# @Link    : http://www.jp166.com
# @Version : 1.0

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
thelist=pygame.display.list_modes()
print(thelist)

screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load('bgimg.jpg')
Fullscr=False

x,y=0,0
move_x,move_y=0,0

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
		if event.type==KEYDOWN:
			if event.key==27:
				exit()
			elif event.key==K_f:
				Fullscr=not Fullscr
				if Fullscr:
					screen=pygame.display.set_mode((640,480),FULLSCREEN,32)
				else:
					screen=pygame.display.set_mode((640,480),0,32)
			elif event.key==K_LEFT:
				move_x=-1
			elif event.key==K_RIGHT:
				move_x=1
			elif event.key==K_UP:
				move_y=-1
			elif event.key==K_DOWN:
				move_y=1
		elif event.type==KEYUP:
			if event.key==K_LEFT:
				move_x=0
			elif event.key==K_RIGHT:
				move_x=0
			elif event.key==K_UP:
				move_y=0
			elif event.key==K_DOWN:
				move_y=0
			# move_x=0
			# move_y=0
	x+=move_x
	y+=move_y
	screen.fill((0,0,0))
	screen.blit(background,(x,y))
	pygame.display.update()

	pass