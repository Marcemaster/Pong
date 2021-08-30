import pygame as pg
from random import randrange

TAMANNO = (800, 600)
VELOCIDAD = 5


class Movil():

    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def actualizate(self):
        pass

    def dibujate(self, lienzo):
        pg.draw.rect(lienzo, self.color,
                     pg.Rect(self.x, self.y, self.w, self.h))


class Raqueta(Movil):
    def __init__(self, x, y, color=(255, 255, 255)):
        Movil.__init__(self, x, y, 20, 120, color)


class Bola(Movil):
    def __init__(self, x, y, color=(255, 255, 255)):
        Movil.__init__(self, x, y, 20, 20, color)
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
        self.todos = []

        self.player1 = Raqueta(10, (TAMANNO[1] - 120)//2)
        self.player2 = Raqueta(TAMANNO[0]-30, (TAMANNO[1] - 120) // 2)

        self.todos.append(self.player1)
        self.todos.append(self.player2)

        bola = Bola(TAMANNO[0] // 2 - 10,
                    TAMANNO[1] // 2 - 10,
                    (255, 255, 0))
        self.todos.append(bola)


    def bucle_principal(self):
        game_over = False
        pg.init()
        while not game_over:
            self.reloj.tick(60)
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            for movil in self.todos:
                movil.actualizate()

            self.pantalla.fill((0, 0, 0))

            for movil in self.todos:
                movil.dibujate(self.pantalla)

            pg.display.flip()
        pg.quit()


if __name__ == '__main__':
    juego = Game()
    juego.bucle_principal()

print(__name__)
