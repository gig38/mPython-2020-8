from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlocks(x+75, y-1, z+75, x-75, y-6, z-75, 3)
mc.setBlocks(x+75, y-6, z+75, x-75, y-76, z-75, 1)
mc.setBlocks(x+75, y-76, z+75, x-75, y-77, z-75,7)

