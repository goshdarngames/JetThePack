################################################################################
# gameObject.py
################################################################################
# Base class for objects that appear on the game scene.
################################################################################
# 09/09 Flembobs
################################################################################

import pygame

class GameObject:
   
   def __init__(self,gameScene,x,y,width,height,colour=(255,255,255)):
      self.gameScene = gameScene
      self.rect = pygame.Rect(x,y,width,height)
      self.colour = colour
      
   def draw(self):
      
      pygame.draw.rect(self.gameScene.gameEngine.screen,self.colour,self.rect)
      
   def update(self):
      pass
      
   def hitBy(self,obj):
      pass
