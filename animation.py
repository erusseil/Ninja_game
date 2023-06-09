import pygame
import numpy as np
import math


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name, rescale, speed, loop_to=0):
        super().__init__()
        self.image = pygame.image.load(f'assets/{name}/{name}1.png')
        self.image = pygame.transform.scale(self.image, rescale)
        self.current_image = 0
        self.images = animations.get(name, rescale)
        self.timer_current = pygame.time.get_ticks()
        self.anim_speed = speed
        self.loop_to = loop_to
        self.angle = 0

    def flip_image(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def animate(self, rescale, orientation=True, once=False, group=0, rotate=False):

        rotation_rescale = rescale

        if (pygame.time.get_ticks() - self.timer_current) >= self.anim_speed:
            self.timer_current = pygame.time.get_ticks()
            self.current_image += 1

            if self.current_image >= len(self.images):
                self.current_image = self.loop_to
                if once:
                    group.remove(self)

            self.image = self.images[self.current_image]

            if rotate:
                self.angle += 1 % 360
                radian = math.radians(self.angle)
                new_rescale = abs(rescale[0]*np.sin(radian)) + abs(rescale[1]*np.cos(radian))
                rotation_rescale = (new_rescale, new_rescale)
                self.rect.x = round(self.x - new_rescale / 2)
                self.rect.y = round(self.y - new_rescale / 2)

                self.image = pygame.transform.rotate(self.image, self.angle)

            self.image = pygame.transform.scale(self.image, rotation_rescale)
            if not orientation:
                self.flip_image()

def load_animation_images(name, num):
    images = []
    path = f"assets/{name}/{name}"

    for i in range(num):
        image_path = path + str(i + 1) + '.png'
        images.append(pygame.image.load(image_path))

    return images


animations = {"smoke": load_animation_images('smoke', 7),
              "new_ninja": load_animation_images('new_ninja', 14),
              "ramen": load_animation_images('ramen', 1)}

