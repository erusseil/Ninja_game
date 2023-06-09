import pygame


rouge = (229, 43, 80)
creme = (250, 235, 215)
black = (0, 0, 0)


def draw_bar(screen, hunger_current, hunger_max):

    length = 850
    bar_size = (hunger_max-hunger_current)*length/hunger_max
    border = 6
    lines = 4

    pos_x = (screen.get_width() - length)/2
    pos_y = 650
    thickness = 30

    pygame.draw.rect(screen, black, (pos_x - border - lines, pos_y - border- lines, length + 2 * (border+lines), thickness + 2 * (border+lines)))
    pygame.draw.rect(screen, creme, (pos_x-border, pos_y-border, length+2*border, thickness+2*border))
    pygame.draw.rect(screen, rouge, (pos_x, pos_y, bar_size, thickness))


def box_best(screen):

    length = 175
    lines = 3

    pos_x = (screen.get_width() - length) / 2
    pos_y = 60
    thickness = 120

    pygame.draw.rect(screen, black, (pos_x-lines, pos_y-lines, length+2*lines, thickness+2*lines))
    pygame.draw.rect(screen, creme, (pos_x, pos_y, length, thickness))


def chrono_box(screen):

    length = 150
    lines = 3

    pos_x = (screen.get_width() - length) / 2
    pos_y = 70
    thickness = 80

    pygame.draw.rect(screen, black, (pos_x-lines, pos_y-lines, length+2*lines, thickness+2*lines))
    pygame.draw.rect(screen, creme, (pos_x, pos_y, length, thickness))








