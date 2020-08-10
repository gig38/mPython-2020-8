# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:38:05 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -216

y = 1042

z = 261

mc.player.setTilePos(x,y,z)