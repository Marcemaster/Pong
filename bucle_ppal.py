import pygame as pg

pg.init()

pantalla = pg.display.set_mode((800, 600))


game_over = False
while not game_over:

    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True


    pantalla.fill((255, 0, 0))

    pg.display.flip()

pg.quit()