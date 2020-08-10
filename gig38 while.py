# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:38:02 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("我正在看著你X:"+str(x)+"Y:"+str(y)+"z:"+str(z))
    time.sleep(1)