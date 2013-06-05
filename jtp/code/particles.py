################################################################################
# particles.py
################################################################################
# Contains classes for the particle system.
################################################################################
# 09/09 Flembobs
################################################################################

import pygame

################################################################################
# Particles
################################################################################

class Particle:
   
   def __init__(self,x,y,xspeed,yspeed,colour,lifespan):
      self.x = x
      self.y = y
      self.xspeed = xspeed
      self.yspeed = yspeed
      self.colour = colour
      self.lifespan = lifespan
      
   def draw(self,surface):
      pygame.draw.rect(surface,(0,0,255),pygame.Rect((self.x,self.y),(3,3)))
      
   def update(self):
      
      self.x+=self.xspeed
      self.y+=self.yspeed
      
      self.lifespan -= 1
      
   

################################################################################
# Particle Manager
################################################################################
   
class ParticleManager:
   
   def __init__(self,gameScene):
      self.gameScene = gameScene
      self.particles = []
      self.particlesToAdd = []
      self.particlesToDel = []
      
   def update(self):
      
      for particle in self.particles:
         if particle.lifespan <= 0:
            self.queueDelParticle(particle)
            continue
         particle.update()
      
      self.delQueued()
      self.addQueued()
   
   def render(self):
      for particle in self.particles:
         particle.draw(self.gameScene.gameEngine.screen)
   
   #############################################################################
   # Adding/Removing Particles
   #############################################################################
         
   def queueAddParticle(self,particle):
      self.particlesToAdd.append(particle)
      
   def queueDelParticle(self,particle):
      self.particlesToDel.append(particle)
      
   def __addParticle(self,particle):
      self.particles.append(particle)
      
   def __delParticle(self,particle):
      self.particles.remove(particle)
      
   def addQueued(self):
      for particle in self.particlesToAdd:
         self.__addParticle(particle)
         
      del self.particlesToAdd[:]
         
   def delQueued(self):
      for particle in self.particlesToDel:
         self.__delParticle(particle)
      
      del self.particlesToDel[:]
