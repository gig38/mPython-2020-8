# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:26:44 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


length = 30
width = 30
height = 30

x,y,z = mc.player.getTilePos()

x2 = x+length
y2 = y+height
z2 = z+width

mc.setBlocks(x, y, z, x2, y2, z2, 57)
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, 0)