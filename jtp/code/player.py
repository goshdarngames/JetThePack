################################################################################
# player.py
################################################################################
# Class for the object the player controls
################################################################################
# 09/09 Flembobs
################################################################################

from gameObject import GameObject
import pygame

################################################################################
# CONSTANTS
################################################################################

GRAV_ACC=0.1  #acceleration caused by gravity
HOR_ACC = 0.15 #horizontal thrust
VER_ACC =0.2 #vertical thrust
MAX_SPEED = 5
FRICTION = 0.99

################################################################################
# CLASS DEFINITION
################################################################################

class Player(GameObject):
   
   def __init__(self,gameScene,x,y):
      GameObject.__init__(self,gameScene,x,y,16,16)
      self.direction = "right"
      self.img = "stationary-right"
      
      #flag used to stop movement at the beginning of a life
      self.inMotion = False
      
      #Non-rounded versions of the x and y
      self.x = x
      self.y = y
      
      #X and Y speeds
      self.xmov = 0
      self.ymov = 0
      
   def draw(self):
      gE = self.gameScene.gameEngine
      img = gE.images[self.img]
      gE.screen.blit(img,(self.rect.x,self.rect.y))
      
   def update(self):
      
      keys = pygame.key.get_pressed()
      
      #Change image according to keys pressed
      if keys[pygame.K_UP]:
         self.img = "up-"+self.direction
         if keys[pygame.K_LEFT]:
            self.direction = "left"
            self.img = "diag-left"
         elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.img = "diag-right"
      elif keys[pygame.K_LEFT]:
         self.direction = "left"
         self.img = self.direction
      elif keys[pygame.K_RIGHT]:
         self.direction = "right"
         self.img = self.direction
      else:
         self.img = "stationary-"+self.direction
         
      #Apply thrust
      #
      #inMotion is set to true so that the player starts moving once a key is
      #pressed
      if keys[pygame.K_UP]:
         self.ymov-=VER_ACC
         self.inMotion = True
      if keys[pygame.K_LEFT]:
         self.xmov-=HOR_ACC
         self.inMotion = True
      if keys[pygame.K_RIGHT]:
         self.xmov+=HOR_ACC
         self.inMotion = True
      
      if not self.inMotion:
         return
      
      #Apply gravity
      self.ymov+=GRAV_ACC
      
      #Apply friction (horizontal only)
      self.xmov*=FRICTION
      
      #Limit speeds to the max speed
      if self.ymov>MAX_SPEED:
         self.ymov=MAX_SPEED
      if self.ymov<MAX_SPEED*-1:
         self.ymov=MAX_SPEED*-1
      if self.xmov>MAX_SPEED:
         self.xmov=MAX_SPEED
      if self.xmov<MAX_SPEED*-1:
         self.xmov=MAX_SPEED*-1
      
      #Update x and y according to speed
      self.x+=self.xmov
      self.y+=self.ymov
      
      #Apply x and y to rect
      self.rect.x = self.x
      self.rect.y = self.y
      
      #Test for collisions
      for obj in self.gameScene.gameObjects:
         if obj is self:
            continue
         
         if self.rect.colliderect(obj.rect):
            obj.hitBy(self)
            break #this will stop the player from colliding with 2 walls
