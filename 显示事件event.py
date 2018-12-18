#Python 3.7 
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 19:32:59
# @Author  : sjp (3152506@qq.com)
# @Link    : http://www.jp166.com
# @Version : 1.0

import pygame,time
from pygame.locals import *
from sys import exit

pygame.init()
scr_size=(640,480)

screen=pygame.display.set_mode(scr_size,0,32)
pygame.display.set_caption('你好，第二课')

font=pygame.font.SysFont('ariar',22)
font_height=font.get_linesize()
event_text=[]

while True:
	event=pygame.event.wait()
	event_text.append(str(event))
	event_text=event_text[-round(scr_size[1]/font_height):]

	if event.type==QUIT:
		exit()

	screen.fill((180,180,180))

	y=scr_size[1]-font_height
	for text in reversed(event_text):
		screen.blit(font.render(text,True,(0,0,0)),(0,y))
		y-=font_height
	# for event in pygame.event.get():
	# 	if event.type==QUIT:
	# 		exit()
		# x,y= pygame.mouse.get_pos()
	# x-=mouse_cursor.get_width()/2
	# y-=mouse_cursor.get_height()/2
	# screen.blit(mouse_cursor,(x,y))

	pygame.display.update()
	time.sleep(0.2)
	pass
