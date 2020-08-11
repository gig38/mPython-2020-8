# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:53:22 2020

@author: USER
"""

import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


    

x,y,z = mc.player.getTilePos()
color = random.randrange(0,16)

mc.setBlocks(x+100, y-1, z+100, x-100, y-1, z-100, 95,color)
time.sleep(3)