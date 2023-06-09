import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.wav"),
            'death': pygame.mixer.Sound("assets/sounds/mort.wav"),
            'las_pop': pygame.mixer.Sound("assets/sounds/las_pop.wav"),
            'las_kill': pygame.mixer.Sound("assets/sounds/las_kill.wav"),
            'music_menu': pygame.mixer.Sound("assets/sounds/menu.mp3"),
            'music_game1': pygame.mixer.Sound("assets/sounds/game1.mp3"),
            'music_game2': pygame.mixer.Sound("assets/sounds/game2.mp3"),
            'blink': pygame.mixer.Sound("assets/sounds/tp.wav"),
            'slideup': pygame.mixer.Sound("assets/sounds/up.wav"),
            'slidedown': pygame.mixer.Sound("assets/sounds/down.wav"),
            '10sec': pygame.mixer.Sound("assets/sounds/10sec.wav"),
            'crunch': pygame.mixer.Sound("assets/sounds/crunch.wav")
        }

    def play(self, name, volume=0.2, loops=0, channel=99):

        if channel != 99:
            pygame.mixer.Channel(channel).play(self.sounds[name], loops=loops)
        else:
            self.sounds[name].play(loops=loops)

        self.sounds[name].set_volume(volume)


    def stop_sound(self, name):
        self.sounds[name].stop()
