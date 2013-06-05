################################################################################
# goal.py
################################################################################
# Contains the class definition for the green square the player must navigate
# to.
################################################################################
# 09/09 Flembobs
################################################################################

from gameObject import GameObject

class Goal(GameObject):
   
   def __init__(self,gameScene,x,y):
      GameObject.__init__(self,gameScene,x,y,16,16,(0,255,0))
      
   def hitBy(self,obj):
      self.gameScene.level+=1
      self.gameScene.loadLevel()
      
