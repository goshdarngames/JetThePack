################################################################################
# gameOver.py
################################################################################
# Contains the class definition for the 'game over' scene.
################################################################################
# 09/09 Flembobs
################################################################################

import pygame
import operator as op
from scene import Scene

class GameOver(Scene):

   def __init__(self,gameEngine,win=False):
      Scene.__init__(self,gameEngine)
      self.win = win
   
   def render(self):
   
      if not self.win: 
         gOver_surf = pygame.font.SysFont("courier",24,True).\
                                     render("Game Over",\
                                     True,(255,0,0))
         self.gameEngine.screen.blit(gOver_surf,(self.__centerText(gOver_surf),\
                                                 100))
                                              
         cont_surf = pygame.font.SysFont("courier",16,True).\
                                     render("Press space to try again.",\
                                     True,(255,255,255))
         self.gameEngine.screen.blit(cont_surf,(self.__centerText(cont_surf),\
                                                 200))
                                                 
      else:
         gOver_surf = pygame.font.SysFont("courier",24,True).\
                                     render("You are the Win!",\
                                     True,(0,255,0))
         self.gameEngine.screen.blit(gOver_surf,(self.__centerText(gOver_surf),\
                                                 100))
                                              
         cont_surf = pygame.font.SysFont("courier",16,True).\
                                     render("Press space to play again.",\
                                     True,(255,255,255))
         self.gameEngine.screen.blit(cont_surf,(self.__centerText(cont_surf),\
                                                 200))
   
   def update(self):
      
      keys = pygame.key.get_pressed()
      
      if keys[pygame.K_SPACE]:
         from gameScene import GameScene
         self.gameEngine.scene = GameScene(self.gameEngine)
      
      
   def __centerText(self,surf):
      """
      Returns the x coordinate this surf should be drawn at to be centered
      on screen.
      """
      x = 640/2
      x -= surf.get_width()/2
      return x
