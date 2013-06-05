################################################################################
# freeLife.py
################################################################################
# Class for the free life powerup.
################################################################################
# 09/09 Flembobs
################################################################################

from gameObject import GameObject

class FreeLife(GameObject):
   
   def __init__(self,gameScene,x,y):
      GameObject.__init__(self,gameScene,x,y,16,16,(0,125,125))
      
   def draw(self):
      gE = self.gameScene.gameEngine
      img = gE.images["1-up"]
      gE.screen.blit(img,(self.rect.x,self.rect.y))   
     
   def hitBy(self,obj):
      self.gameScene.lives+=1
      self.gameScene.gameObjects.remove(self)
