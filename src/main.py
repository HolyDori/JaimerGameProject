import pygame, time, os
from engine.game_state import Title

class Game:

    def __init__(self):
        pygame.init()
        self.Game_W, self.Game_H = 480, 270
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 960, 540
        self.gameCanvas = pygame.Surface((self.Game_W, self.Game_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.action = {"up": False, "down": False, "left": False, "right": False, "escape": False, "return": False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.load_states()


    def get_event(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running, self.playing = False, False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: self.action["up"] = True
                if event.key == pygame.K_s: self.action["down"] = True
                if event.key == pygame.K_a: self.action["left"] = True
                if event.key == pygame.K_d: self.action["right"] = True
                if event.key == pygame.K_ESCAPE: self.action["escape"] = True
                if event.key == pygame.K_RETURN: self.action["return"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: self.action["up"] = False
                if event.key == pygame.K_s: self.action["down"] = False
                if event.key == pygame.K_a: self.action["left"] = False
                if event.key == pygame.K_d: self.action["right"] = False
                if event.key == pygame.K_ESCAPE: self.action["escape"] = False
                if event.key == pygame.K_RETURN: self.action["return"] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.action)

    def render(self):
        self.state_stack[-1].render(self.gameCanvas)
        self.screen.blit(pygame.transform.scale(self.gameCanvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, color, x_pos, y_pos):
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x_pos, y_pos)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        # Create pointers to directories
        self.assets_dir = os.path.join("assets")
        self.sprites_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "fonts")
        #self.font = pygame.font.Font(os.path.join(self.font_dir, ""))
        self.font = pygame.font.SysFont("Consolas", 24)

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.action:
            self.action[action] = False

    def mainloop(self):
        while self.playing:
            self.get_dt()
            self.get_event()
            self.update()
            self.render()

if __name__ == "__main__":
    game = Game()
    if game.running:
        game.mainloop()