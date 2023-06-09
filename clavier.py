import numpy as np
import pygame


def get_coord_clavier(x,y):

    half_square = 37
    x_clavier = np.array([148, 227, 306, 384, 463, 542, 621, 700, 778, 858]) + half_square
    y_clavier = np.array([286, 365, 445, 523]) + half_square

    mesh = np.meshgrid(x_clavier, y_clavier)

    return (mesh[0][y][x], mesh[1][y][x])


def convert_key_topos(key):

    exist = True
    if key == pygame.K_1:
        coord = get_coord_clavier(0, 0)
    elif key == pygame.K_2:
        coord = get_coord_clavier(1, 0)
    elif key == pygame.K_3:
        coord = get_coord_clavier(2, 0)
    elif key == pygame.K_4:
        coord = get_coord_clavier(3, 0)
    elif key == pygame.K_5:
        coord = get_coord_clavier(4, 0)
    elif key == pygame.K_6:
        coord = get_coord_clavier(5, 0)
    elif key == pygame.K_7:
        coord = get_coord_clavier(6, 0)
    elif key == pygame.K_8:
        coord = get_coord_clavier(7, 0)
    elif key == pygame.K_9:
        coord = get_coord_clavier(8, 0)
    elif key == pygame.K_0:
        coord = get_coord_clavier(9, 0)
    # ------------------------------------
    elif key == pygame.K_a :
        coord = get_coord_clavier(0,1)
    elif key == pygame.K_z :
        coord = get_coord_clavier(1, 1)
    elif key == pygame.K_e :
        coord = get_coord_clavier(2, 1)
    elif key == pygame.K_r :
        coord = get_coord_clavier(3, 1)
    elif key == pygame.K_t :
        coord = get_coord_clavier(4, 1)
    elif key == pygame.K_y :
        coord = get_coord_clavier(5, 1)
    elif key == pygame.K_u :
        coord = get_coord_clavier(6, 1)
    elif key == pygame.K_i :
        coord = get_coord_clavier(7, 1)
    elif key == pygame.K_o :
        coord = get_coord_clavier(8, 1)
    elif key == pygame.K_p :
        coord = get_coord_clavier(9, 1)
    # ------------------------------------
    elif key == pygame.K_q :
        coord = get_coord_clavier(0,2)
    elif key == pygame.K_s :
        coord = get_coord_clavier(1,2)
    elif key == pygame.K_d :
        coord = get_coord_clavier(2,2)
    elif key == pygame.K_f :
        coord = get_coord_clavier(3,2)
    elif key == pygame.K_g :
        coord = get_coord_clavier(4,2)
    elif key == pygame.K_h :
        coord = get_coord_clavier(5,2)
    elif key == pygame.K_j :
        coord = get_coord_clavier(6,2)
    elif key == pygame.K_k :
        coord = get_coord_clavier(7,2)
    elif key == pygame.K_l :
        coord = get_coord_clavier(8,2)
    elif key == pygame.K_m :
        coord = get_coord_clavier(9,2)
    # ------------------------------------
    elif key == pygame.K_w :
        coord = get_coord_clavier(0,3)
    elif key == pygame.K_x :
        coord = get_coord_clavier(1,3)
    elif key == pygame.K_c :
        coord = get_coord_clavier(2,3)
    elif key == pygame.K_v :
        coord = get_coord_clavier(3,3)
    elif key == pygame.K_b :
        coord = get_coord_clavier(4,3)
    elif key == pygame.K_n :
        coord = get_coord_clavier(5,3)
    elif key == pygame.K_COMMA :
        coord = get_coord_clavier(6,3)
    elif key == pygame.K_SEMICOLON :
        coord = get_coord_clavier(7,3)
    elif key == pygame.K_COLON :
        coord = get_coord_clavier(8,3)
    elif key == pygame.K_EXCLAIM :
        coord = get_coord_clavier(9,3)
    else :
        coord = (0,0)
        exist = False

    return ([coord[0],coord[1],exist])