import pygame as pg
from random import randrange

TAMANNO = (800, 600)
VELOCIDAD = 5


class Bola():
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.incremento_x = VELOCIDAD
        self.incremento_y = -VELOCIDAD

    def actualizate(self):

        self.x += self.incremento_x
        self.y += self.incremento_y

        if self.x + self.w > TAMANNO[0] or self.x < 0:
            self.incremento_x *= -1

        if self.y + self.h > TAMANNO[1] or self.y < 0:
            self.incremento_y *= -1


class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode(TAMANNO)
        self.reloj = pg.time.Clock()
        self.bolas = []
        for i in range(10):
            tamanyo = randrange( 10, 41)
            bola = Bola(randrange(0, TAMANNO[0]),
            randrange(9, TAMANNO[1]),
            tamanyo,
            tamanyo,
            (randrange(256), randrange(256), randrange(256)))

            
            self.bolas.append(bola)

        self.bucle_principal()


    def bucle_principal(self):
        game_over = False
        pg.init()
        while not game_over:
            self.reloj.tick(60)
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            for i in range(len(self.bolas)):
                self.bolas[i].actualizate()
        
            self.pantalla.fill((0, 0, 0))
            for bola in self.bolas:
                pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))

            pg.display.flip()
        pg.quit()


juego = Game()
