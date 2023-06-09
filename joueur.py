import pygame
import animation
import smoke

class Joueur(animation.AnimateSprite):
    def __init__(self, game):
        self.rescale = (70, 70)
        self.anim_speed = 80
        self.left = False
        super().__init__("new_ninja", self.rescale, self.anim_speed, loop_to=8)

        self.last_tp = pygame.time.get_ticks()
        self.cooldown = 30

        self.rect = self.image.get_rect()

        self.correc_y = 0
        self.rect.x = round(577 - self.image.get_width()/2)
        self.rect.y = round(405 - self.image.get_height()/2) - self.correc_y
        self.game = game

    def update_animation(self):
        self.animate(self.rescale, orientation=self.left)

    def move_to(self, coord_x, coord_y):
        if self.game.is_playing | self.game.is_sliding:
            if (pygame.time.get_ticks()-self.last_tp) >= self.cooldown:
                self.last_tp = pygame.time.get_ticks()

                move_to_x = round(coord_x - self.image.get_width()/2)
                move_to_y = round(coord_y - self.image.get_height()/2) - self.correc_y

                initial_x = round(self.rect.x + self.image.get_width()/2)
                initial_y = round(self.rect.y + self.image.get_height() / 2) + self.correc_y

                # On ne déplace le joueur que si le joueur n'est pas déjà sur la case
                if (self.rect.x != move_to_x) | (self.rect.y != move_to_y):

                    if (self.rect.x > move_to_x) & (self.left == False):
                        self.left = True
                        self.flip_image()

                    elif (self.rect.x < move_to_x) & (self.left == True):
                        self.left = False
                        self.flip_image()

                    #smoke.Smoke.create_smoke(coord_x, coord_y)
                    smoke.Smoke.create_smoke(initial_x, initial_y)
                    self.game.sound_manager.play('blink')
                    self.rect.x = move_to_x
                    self.rect.y = move_to_y
                    self.current_image = 0