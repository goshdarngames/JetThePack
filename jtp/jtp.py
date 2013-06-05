################################################################################
# jtp.py
################################################################################
# Main game engine for Jet The Pack.
################################################################################
# 09/09 Flembobs
################################################################################


import os
import pygame

from code.gameScene import GameScene

################################################################################
# Game Engine
################################################################################

class GameEngine:
   
   #############################################################################
   # INIT
   #############################################################################
   
   def __init__(self):      
      #Initialise pygame
      os.environ["SDL_VIDEO_CENTERED"] = "1"
      pygame.init()

      # Set up the display
      pygame.display.set_caption("Jet The Pack")
      self.screen = pygame.display.set_mode((640, 480))

      self.clock = pygame.time.Clock()
      
      #Stores loaded images in the form (name:surface)
      self.images = dict()
      self.__loadImages()
      
      self.scene = GameScene(self)
   
   #############################################################################
   # MAIN GAME LOOP
   #############################################################################
   
   def loop(self):
   
      while not self.__checkQuit():
         
         self.clock.tick(60)
         self.screen.fill((0,0,0))
         
         self.scene.update()
         self.scene.render()
         
         pygame.display.flip()
         
   #############################################################################
   # FUNCTIONS
   #############################################################################
   
   def __checkQuit(self):
   
      for e in pygame.event.get():
         if e.type == pygame.QUIT:
            return True
         if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            return True
   
      return False
      
   def __loadImages(self):
      image_path = "data/images"
      for img in os.listdir(image_path):
         surf = pygame.image.load(image_path+"/"+img)
         surf.convert()
         surf.set_colorkey((255,255,255))
         
         #remove the png and use filename as dict key
         self.images[img[:-4]]=surf
   
################################################################################
# Executable Logic
################################################################################

gE = GameEngine()
gE.loop()
