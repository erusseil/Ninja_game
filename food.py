import animation
import random
from clavier import *

class Food(animation.AnimateSprite):
    timer_spawn_food = pygame.time.get_ticks()
    hunger = 10000
    hunger_current = 0
    last_eat = 0

    nb_food = 0

    spawn_food = 4000
    life_time = 4000

    all_ramens = pygame.sprite.Group()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rescale = (70, 70)
        self.anim_speed = 10
        super().__init__("ramen", self.rescale, self.anim_speed)

        self.spawn_date = pygame.time.get_ticks()

        self.rect = self.image.get_rect()
        self.rect.x = round(self.x - self.image.get_width() / 2)
        self.rect.y = round(self.y - self.image.get_height() / 2)

    def create_food(x, y):
        Food.all_ramens.add(Food(x, y))

    create_food = staticmethod(create_food)

    def digeste(cls):
        Food.hunger_current = pygame.time.get_ticks() - Food.last_eat

        if Food.hunger_current >= Food.hunger:
            return True
        else:
            return False

    digeste = classmethod(digeste)


    def remove_food(self):
        Food.all_ramens.remove(self)

    def create_random_food():
        i = random.randint(0, 9)
        j = random.randint(0, 3)

        x, y = get_coord_clavier(i, j)
        Food.create_food(x, y)

    create_random_food = staticmethod(create_random_food)

    def cooldown_advance(cls):
        if pygame.time.get_ticks() - Food.timer_spawn_food >= Food.spawn_food:
            Food.timer_spawn_food = pygame.time.get_ticks()
            return True
        else:
            return False

    cooldown_advance = classmethod(cooldown_advance)

    def state(self):
        if (pygame.time.get_ticks() - self.spawn_date) >= Food.life_time:
            self.remove_food()

    def update_animation(cls):
        for i in Food.all_ramens:
            i.animate(i.rescale, rotate=True)

    update_animation = classmethod(update_animation)