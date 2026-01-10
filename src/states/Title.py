from src.engine.game_state import State
from src.states.Battle_stage import Dungeon

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["return"]:
            new_state = Dungeon(self.game, bg_filename="Background-d1.png")
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "Game States Demo", (0,0,0), self.game.Game_W/2 , self.game.Game_H/2)