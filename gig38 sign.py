# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:13:34 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,3,"Mine","craft","is the","best.")
 