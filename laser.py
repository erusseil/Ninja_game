import random
from clavier import *
import pygame


class Laser(pygame.sprite.Sprite):
    timer_spawn_laser = pygame.time.get_ticks()
    nb_laser = 0

    spawn_laser = 500
    life_time = 750
    activation = 500

    all_lasers = pygame.sprite.Group()
    all_deadly_lasers = pygame.sprite.Group()

    def __init__(self, angle, posx, posy, game):
        super().__init__()

        self.angle = angle
        self.deadly = False

        self.spawn_date = pygame.time.get_ticks()

        self.image = pygame.image.load('assets/laser/laser1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect()

        self.rect.x = round(posx - self.image.get_width() / 2)
        self.rect.y = round(posy - self.image.get_height() / 2)
        self.game = game

    def create_laser(angle, x, y, game):
        Laser.all_lasers.add(Laser(angle, x, y, game))
        game.sound_manager.play('las_pop', volume=0.15)

    create_laser = staticmethod(create_laser)

    def remove_laser(self):
        Laser.all_lasers.remove(self)
        Laser.all_deadly_lasers.remove(self)

    def create_random_laser(game):
        angle = random.choice([0, 45, 90, 135])
        i = random.randint(0, 9)
        j = random.randint(0, 3)

        x, y = get_coord_clavier(i, j)
        Laser.create_laser(angle, x, y, game)

    create_random_laser = staticmethod(create_random_laser)

    def cooldown_advance(cls):
        if pygame.time.get_ticks() - Laser.timer_spawn_laser >= Laser.spawn_laser:
            Laser.timer_spawn_laser = pygame.time.get_ticks()
            return True
        else:
            return False

    cooldown_advance = classmethod(cooldown_advance)

    def state(self):

        if ((pygame.time.get_ticks() - self.spawn_date) >= Laser.activation / 1.2) & (
                (pygame.time.get_ticks() - self.spawn_date) < Laser.activation):
            self.image = pygame.image.load('assets/laser/laser2.png').convert_alpha()
            self.image = pygame.transform.rotate(self.image, self.angle)

        elif ((pygame.time.get_ticks() - self.spawn_date) > Laser.activation) & (self.deadly == False):
            self.image = pygame.image.load('assets/laser/laser3.png').convert_alpha()
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.deadly = True
            Laser.all_deadly_lasers.add(self)
            self.game.sound_manager.play('las_kill')

        if (pygame.time.get_ticks() - self.spawn_date) >= Laser.life_time:
            self.remove_laser()
