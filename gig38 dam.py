# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:35:35 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

a = 0
while a<50:
    mc.setBlocks(x,y-1,z+40,x,y-30,z-40,19)
    x = x-5
    a = a+1
