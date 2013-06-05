################################################################################
# wall.py
################################################################################
# Class for the walls that the player must avoid crashing into.
################################################################################
# 09/09 Flembobs
################################################################################

from gameObject import GameObject

class Wall(GameObject):
   
   def __init__(self,gameScene,x,y):
      GameObject.__init__(self,gameScene,x,y,16,16,(255,0,0))
      
   def hitBy(self,obj):
      self.gameScene.playerDeath(obj)
      
