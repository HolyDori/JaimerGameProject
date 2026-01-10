from src.engine.game_state import State
import pygame, os

class Dialog(State):
    def __init__(self, game, bg_filename):
        State.__init__(self, game)
        self.bg = pygame.image.load(os.path.join(game.background_dir, bg_filename))
        self.textbox = TextBox(game, rect=((self.game.Game_W/2)-300,self.game.Game_H/1.5,600,100), text="this is a dialog state")
        self.game = game

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.bg, (0, 0))
        self.textbox.render(display)

class TextBox:
    def __init__(self, game, rect, text="", bg_color=(30,30,30), border_color=(200,200,200)):
        self.game = game
        self.rect = pygame.Rect(rect)
        self.text = text
        self.bg_color = bg_color
        self.border_color = border_color

    def set_text(self, text):
        self.text = text

    def render(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)

        cx = self.rect.centerx
        cy = self.rect.centery

        self.game.draw_text(surface, self.text, (255,255,255), cx, cy)