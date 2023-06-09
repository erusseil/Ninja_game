from game import Game
from button import *
from smoke import Smoke

pygame.init()

res = (1080, 720)
screen = pygame.display.set_mode(res)
background = pygame.image.load('assets/new_background.png')

bg_x = 0
bg_y = 0

bg_menu_y = 0
bg_game_y = -554

# Create a clock
clock = pygame.time.Clock()

# Set FPS (frames per second)
clock.tick(60)
score_font = pygame.font.SysFont("monospace", 60, bold=True)
compteur_font = pygame.font.SysFont("monospace", 200, bold=True)

game = Game()
game.sound_manager.play('music_menu', volume=1, loops=100)
running = True


def compteur(screen, t, duree):
    pos = (540, 200)
    if t >= duree * 2 / 3:
        rdy = compteur_font.render("1", True, (0, 0, 0))

    elif t >= duree * 1 / 3:
        rdy = compteur_font.render("2", True, (0, 0, 0))

    else:
        rdy = compteur_font.render("3", True, (0, 0, 0))

    rect = rdy.get_rect()
    screen.blit(rdy, (pos[0] - rect.width / 2, pos[1] - rect.height / 2))


def slide_screen(screen, p1, p2, duree, down):
    t = pygame.time.get_ticks() - game.time_slide
    direction = p2 - p1
    zero = p1
    music, volume = 'music_game1', 0.85

    if not down:
        direction = - direction
        zero = p2
        music, volume = 'music_menu', 0.5

    if down:
        compteur(screen, t, duree)

    if t > duree:
        game.is_sliding = False
        game.is_playing = not game.is_playing
        game.sound_manager.play(music, loops=100, volume=volume, channel=4)

        game.reset_values()

    return zero + (t * direction) / duree


while running:

    if game.is_sliding:

        screen.blit(background, (bg_x, bg_y))

        for i in Smoke.all_smokes:
            i.update_animation()
        game.joueur.update_animation()

        if game.slide_down:
            bg_y = slide_screen(screen, bg_menu_y, bg_game_y, 2000, game.slide_down)

            joueur_slide = (game.joueur.rect).copy()
            joueur_slide.y = joueur_slide.y - bg_game_y + bg_y

            for i in Smoke.all_smokes:
                smoke_slide = (i.rect).copy()
                smoke_slide.y = smoke_slide.y - bg_game_y + bg_y
                screen.blit(i.image, smoke_slide)

            screen.blit(game.joueur.image, joueur_slide)
            Laser.all_lasers.draw(screen)

        else:
            bg_y = slide_screen(screen, bg_menu_y, bg_game_y, 1000, game.slide_down)

    elif game.is_playing:
        screen.blit(background, (bg_x, bg_y))
        game.update(screen)

    else:
        screen.blit(background, (bg_x, bg_y))
        game.update_menu(screen, score_font)

    pygame.display.flip()

    for event in pygame.event.get():

        # Pour fermer le programme avec la petite croix
        if event.type == pygame.QUIT:
            running = False

        # Detecter si on appuie une touche du clavier
        if event.type == pygame.KEYDOWN:
            where = convert_key_topos(event.key)
            if where[2]:
                game.joueur.move_to(where[0], where[1])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                Button.click_on(game)
