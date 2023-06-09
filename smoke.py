import pygame
import animation



class Smoke(animation.AnimateSprite):

    all_smokes = pygame.sprite.Group()

    def __init__(self, x, y):
        self.rescale = (190, 190)
        self.anim_speed = 45
        super().__init__("smoke", self.rescale, self.anim_speed)

        self.rect = self.image.get_rect()
        self.rect.x = round(x - self.image.get_width() / 2)
        self.rect.y = round(y - self.image.get_height() / 2)

    def update_animation(self):
        self.animate(self.rescale, once=True, group=Smoke.all_smokes)

    def create_smoke(x, y):
        Smoke.all_smokes.add(Smoke(x, y))

    create_smoke = staticmethod(create_smoke)

    def remove_smoke(self):
        Smoke.all_smokes.remove(self)


