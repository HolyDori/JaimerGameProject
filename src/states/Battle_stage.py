from src.engine.game_state import State
from src.states.Dialog import Dialog
import pygame, os

class Dungeon(State):
    def __init__(self, game, bg_filename):
        State.__init__(self, game)
        self.Dungeon_Bg = pygame.image.load(os.path.join(game.background_dir, bg_filename))
        #self.player = Player(self.game)

    def update(self, delta_time, actions):
        #self.player.update(delta_time, actions)
        if actions["return"]:
            new_state = Dialog(self.game, bg_filename="Background-d1.png")
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.Dungeon_Bg, (0, 0))
        #self.player.render(display)

#class Player():
    #def __init__(self, game):
        #self.game = game
        #self.load_sprites()
        #self.position_x, self.position_y = 200,200
        #self.current_frame, self.last_frame_update = 0,0

    #def update(self, delta_time, actions):
        #pass

    #def render(self, display):
        #display.blit(self.curr_image, (self.position_x, self.position_y))

    #def animate(self, delta_time, actions):
        #self.last_frame_update += delta_time
        #if actions["idle"]:
            #self.curr_image = self.curr_anim_list[0]
            #return
        #if self.last_frame_update > .15:
            #self.last_frame_update = 0
            #self.current_frame = (self.current_frame + 1) % len(self.curr_anim_list)
           # self.curr_image = self.curr_anim_list[self.current_frame]

    #def load_sprites(self):
        #self.sprite_dir = os.path.join(self.game.sprites_dir, "player")
        #self.idle_sprites, self.attacking_sprites, self.special_sprites, self.talking_sprites = [],[],[],[]
        #for i in range(1,5):
            #self.idle_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_idle" + str(i) + ".png")))
            #self.attacking_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_attacking" + str(i) + ".png")))
            #self.special_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_special" + str(i) + ".png")))
            #self.talking_sprites.append(pygame.image.load(os.path.join(self.sprite_dir, "player_talking" + str(i) + ".png")))
       # self.curr_image = self.idle_sprites[0]
        #self.curr_anim_list = self.idle_sprites