from src.engine.game_state import State
import pygame, os

class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)

        self.menu_img = pygame.image.load(self.game.background_dir, "menu.png")
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (self.game.Game_W*.85, self.game.Game_H*.4)

    def update(self, delta_time, actions):
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, surface):
        self.prev_state.render(display)
        surface.blit(self.menu_img, self.menu_rect),