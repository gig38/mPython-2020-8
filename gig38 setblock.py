# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:00:40 2020

@author: USER
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,57)
mc.setBlock(x,y+1,z,57)
mc.setBlock(x,y+2,z,57)
mc.setBlock(x,y+3,z,57)
mc.setBlock(x,y+4,z,57)
mc.setBlock(x,y+5,z,57)
mc.setBlock(x,y+6,z,57)
mc.setBlock(x,y+7,z,57)
mc.setBlock(x,y+8,z,57)
mc.setBlock(x,y+9,z,57)
mc.setBlock(x,y+10,z,57)
mc.setBlock(x,y+11,z,57)
mc.setBlock(x,y+12,z,57)