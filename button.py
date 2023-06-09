from laser import *
import pygame

class Button(pygame.sprite.Sprite):

    scale_ratio = 1
    ratio_acti = 0.85
    first_spawn_laser = 550
    first_life_time = 1300
    first_activation = ratio_acti * first_life_time



    def __init__(self,image_path, game):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (Button.scale_ratio*self.image.get_width(), Button.scale_ratio*self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 360 - self.image.get_height()/2

        self.game = game


    def click_on(game):
        if (not game.is_playing) & (not game.is_sliding):
            Laser.spawn_laser = Button.first_spawn_laser
            Laser.life_time = Button.first_life_time
            Laser.activation = Button.first_activation
            game.time_slide = pygame.time.get_ticks()
            game.slide_down = True
            game.is_sliding = True
            game.sound_manager.play('click')
            game.sound_manager.play('slidedown')
            game.sound_manager.stop_sound('music_menu')

    click_on = staticmethod(click_on)

def marathon_diff(time):

    if 0 < time < 10:
        Laser.spawn_laser = Button.first_spawn_laser
        Laser.life_time = Button.first_life_time
        Laser.activation = Button.first_activation

    elif 10 < time < 20:
        Laser.spawn_laser = 500
        Laser.life_time = 1275

    elif 20 < time < 30:
        Laser.spawn_laser = 450
        Laser.life_time = 1250

    elif 30 < time < 40:
        Laser.spawn_laser = 425
        Laser.life_time = 1225

    elif 40 < time < 50:
        Laser.spawn_laser = 400
        Laser.life_time = 1200

    elif 50 < time < 60:
        Laser.spawn_laser = 385
        Laser.life_time = 1175

    elif 60 < time < 70:
        Laser.spawn_laser = 370
        Laser.life_time = 1150

    elif 70 < time < 80:
        Laser.spawn_laser = 350
        Laser.life_time = 1125

    elif 80 < time < 90:
        Laser.spawn_laser = 340
        Laser.life_time = 1100

    elif 90 < time < 100:
        Laser.spawn_laser = 330
        Laser.life_time = 1075

    elif 100 < time < 110:
        Laser.spawn_laser = 320
        Laser.life_time = 1050

    elif 110 < time < 120:
        Laser.spawn_laser = 310
        Laser.life_time = 1025

    elif time > 120:
        Laser.spawn_laser = 300
        Laser.life_time = 1000

    Laser.activation = Laser.life_time * Button.ratio_acti

