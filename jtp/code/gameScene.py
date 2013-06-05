################################################################################
# gameScene.py
################################################################################
# Scene for the main game action.
################################################################################
# 09/09 Flembobs
################################################################################

import pygame
import random

from scene import Scene
from gameOver import GameOver
from wall import Wall
from player import Player
from goal import Goal
from freeLife import FreeLife
from particles import *

################################################################################
# GAMESCENE CLASS
################################################################################

class GameScene(Scene):
   
   def __init__(self,gameEngine):
      Scene.__init__(self,gameEngine)
      
      self.particleManager = ParticleManager(self)
      self.gameObjects = []
      
      self.lives = 5
      self.spawn =(32,32) #coordinates that the player spawned on
      self.spawnTimer = 0
      
      self.level = 1
      self.loadLevel()
   
   #############################################################################
   # FUNCTIONS
   #############################################################################
   
   def update(self):
      
      for obj in self.gameObjects:
         obj.update()
         
      self.particleManager.update()
      
      if self.spawnTimer>0:
         self.spawnTimer-=1
         
         if self.spawnTimer is 0:
            
            if self.lives<0:
               self.gameEngine.scene = GameOver(self.gameEngine)
               return
         
            player = Player(self,self.spawn[0],self.spawn[1])
            self.gameObjects.append(player)
   
   #----------------------------------------------------------------------------
   
   def render(self):
      #draw game objects
      for obj in self.gameObjects:
         obj.draw()
         
      self.particleManager.render()
      
      #draw HUD
      lives_surf = pygame.font.SysFont("courier",12,True).\
                                  render("lives:"+str(self.lives),\
                                  True,(0,0,0))
      self.gameEngine.screen.blit(lives_surf,(10,465))
      
   #----------------------------------------------------------------------------
         
   def loadLevel(self):
      """
      Loads the level specified by the level argument.
      """
      
      #Try open the level, if it doesn't exist go to the win screen
      try:
         f = open("data/levels/level_%03d"%self.level)
      except IOError:
         self.gameEngine.scene = GameOver(self.gameEngine,True)
         return
      
      del self.gameObjects[:]
      
      x=y=0
      while 1:
         row = f.readline()
         if not row:
            break
         for col in row:
            
            obj = None #object to be added at the end of each iteration
         
            if col == "W":
               obj = Wall(self,x,y)
            if col == "E":
               obj = Goal(self,x,y)
            if col == "L":
               obj = FreeLife(self,x,y)
            if col == "B":
               obj = Player(self,x,y)
               self.spawn = (x,y)
            
            if obj is not None:
               self.gameObjects.append(obj)
            
            x += 16
            
         y += 16
         x = 0
         
   #----------------------------------------------------------------------------
   
   def playerDeath(self,player):
      self.lives-=1
      self.gameObjects.remove(player)
      self.explosion(player.x+8,player.y+8)
      self.spawnTimer = 120
   
   #----------------------------------------------------------------------------
   
   def explosion(self,x,y):
      numParticles = random.random()*100+100
      
      for i in range(0,int(numParticles)):
         
         xspeed = random.random()*5
         yspeed = random.random()*5
         
         if int(xspeed) is 0:
            yspeed+=1
         
         if random.random()<0.5:
            xspeed *= -1
         
         if random.random()<0.5:
            yspeed *= -1 
         
         particle = Particle(x,y,xspeed,yspeed,(0,0,255),random.random()*90+30)
         
         self.particleManager.queueAddParticle(particle)
