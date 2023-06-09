import bar
import button
from joueur import Joueur
from laser import Laser
from button import Button
from smoke import Smoke
from sounds import SoundManager
from food import Food
from bar import *


class Game():

    def __init__(self):

        # Definir si le jeu a commencé ou non
        self.is_playing = False
        self.is_sliding = False
        self.joueur = Joueur(self)
        self.infinite_button = Button('assets/start_button.png', self)
        self.score = 0
        self.timer_start = 0
        self.timer_current = 0
        self.best_score = 0
        self.best_score_code = 0
        self.time_slide = 0
        self.slide_down = True
        self.sound_manager = SoundManager()
        self.once_score_sound = False

    def reset_values(self):
        self.timer_start = pygame.time.get_ticks()
        self.timer_current = pygame.time.get_ticks()
        Food.last_eat = pygame.time.get_ticks()
        Laser.nb_laser = 0
        Food.nb_food = 0

    def check_collision(self, sprite, group):
        return len(pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)) != 0

    def sound_score(self):
        if (self.timer_current % 10 == 0) & (not self.once_score_sound) & (self.timer_current != 0) & (self.timer_current <= 120):
            self.once_score_sound = True
            if self.timer_current >= 120:
                self.sound_manager.play('10sec', volume=1, channel=2, loops=3)
            else:
                self.sound_manager.play('10sec', volume=1, channel=2)


        elif (self.timer_current % 10 != 0):
            self.once_score_sound = False

    def update(self, screen):
        score_font = pygame.font.SysFont("monospace", 60, bold=True)
        screen.blit(self.joueur.image, self.joueur.rect)
        Laser.all_lasers.draw(screen)
        Smoke.all_smokes.draw(screen)
        Food.all_ramens.draw(screen)

        self.sound_score()
        self.timer_current = round((pygame.time.get_ticks()-self.timer_start)/1000)
        self.joueur.update_animation()
        Food.update_animation()

        for i in Smoke.all_smokes:
            i.update_animation()

        button.marathon_diff(self.timer_current)

        # Evolve l'etat de deadly du laser
        for i in Laser.all_lasers:
            i.state()

        for i in Food.all_ramens:
            i.state()

        # Faire avancer le temps de spawn du laser
        if Laser.cooldown_advance():
            Laser.create_random_laser(self)

        if Food.cooldown_advance():
            Food.create_random_food()

        # Destroy ramen if touched by player
        if self.check_collision(self.joueur, Food.all_ramens):
            pygame.sprite.spritecollide(self.joueur, Food.all_ramens, True, pygame.sprite.collide_mask)
            Food.last_eat = pygame.time.get_ticks()
            self.sound_manager.play('crunch', volume=1, channel=3)

        # Verifier que le joueur n'est pas mort
        if self.check_collision(self.joueur, Laser.all_deadly_lasers):
            self.end_game()

        if Food.digeste():
            self.end_game()


        bar.draw_bar(screen, Food.hunger_current, Food.hunger)
        logo_bar = pygame.image.load('assets/ramen/ramen1.png')
        screen.blit(logo_bar, (80, 625))
        chrono_box(screen)

        score_text = score_font.render(str(self.timer_current), True, (0, 0, 0))
        text_size = score_text.get_rect().width
        screen.blit(score_text, (540-(text_size/2), 80))

    def end_game(self):

        self.time_slide = pygame.time.get_ticks()
        self.is_sliding = True
        self.slide_down = False
        self.sound_manager.stop_sound('music_game1')
        self.sound_manager.stop_sound('music_game2')
        self.sound_manager.play('death', volume=1, channel=0)
        self.sound_manager.play('slideup', volume=0.2, channel=1)

        for i in Laser.all_lasers:
            i.remove_laser()

        for i in Smoke.all_smokes:
            i.remove_smoke()

        for i in Food.all_ramens:
            i.remove_food()

        if self.timer_current > self.best_score:
            self.best_score = self.timer_current
            self.best_score_code = ((((self.best_score ** 3)-14)*3)**1/4 + 12 + (self.best_score/4)**4)/(self.best_score+1)

    def update_menu(self, screen, font):

        code_font = pygame.font.SysFont("monospace", 15, bold=True)
        screen.blit(self.infinite_button.image, self.infinite_button.rect)
        box_best(screen)

        record_text = font.render("BEST", True, (0, 0, 0))
        text_size = record_text.get_rect().width
        screen.blit(record_text, (540-(text_size/2), 60))

        best_score_text = font.render(str(self.best_score), True, (0, 0, 0))
        text_size = best_score_text.get_rect().width
        screen.blit(best_score_text, (540-(text_size/2), 120))

        best_score_code = code_font.render(str(self.best_score_code), True, (0, 0, 0))
        screen.blit(best_score_code, (10, 10))
