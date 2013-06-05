################################################################################
# scene.py
################################################################################
# Base class for scenes.  A scene is basically a stage for game objects.  There
# would be a scene for the game over screen, the main menu and the main game.
################################################################################
# 09/09 Flembobs
################################################################################

class Scene:

   def __init__(self,gameEngine):
      self.gameEngine = gameEngine

   def update(self):
      pass
   def render(self):
      pass
