# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:19:12 2020

@author: USER
"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(5)

x,y,z = mc.player.getTilePos()

mc.setBlocks(x+100, y-1, z+100, x-100, y-1, z-100, 57)

