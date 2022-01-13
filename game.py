import pygame as p
import random as r
from pygame.locals import *
import copy

#цвет обьектов
game_colour = (0, 1, 215)
#задний фон
background = (255, 91, 192)
#цвет текста
text_colour = (0, 0, 0)
# экран
p.display.set_caption('игра жизнь)))')
#размеры
size = p.display.set_mode((600, 600))
n = size.get_height() // 20
m = size.get_width() // 20

class Cell:
    cells = set()
    def __init__(self, coor1, coor2, alive):
        self.coor1 = coor1
        self.coor2 = coor2
        self.alive = alive
        Cell.cells.add(self)
        return

    def kill(self):
        self.alive = False
        return

    def rekyrsia(self):
        self.alive = True
        return

    def neibours(self):
        count = 0
        for coor3 in Cell.cells:
            if coor3.alive:
                if coor3.coor1 == (self.coor1 + 1) and coor3.coor2 == self.coor2:
                    count += 1
                elif coor3.coor1 == (self.coor1 - 1) and coor3.coor2 == self.coor2:
                    count += 1
                elif coor3.coor1 == self.coor1 and coor3.coor2 == self.coor2 + 1:
                    count += 1
                elif coor3.coor1 == self.coor1 and coor3.coor2 == self.coor2 - 1:
                    count += 1
                elif coor3.coor1 == (self.coor1 + 1) and coor3.coor2 == self.coor2 + 1:
                    count += 1
                elif coor3.coor1 == self.coor1 - 1 and coor3.coor2 == self.coor2 + 1:
                    count += 1
                elif coor3.coor1 == self.coor1 + 1 and coor3.coor2 == self.coor2 - 1:
                    count += 1
                elif coor3.coor1 == self.coor1 - 1 and coor3.coor2 == self.coor2 - 1:
                    count += 1
        return count


class Game:
    krug = 0

    def __init__(self, n, m):
        self.n = n
        self.m = m
        return

    def setup(self):
        for i in range(n):
            for j in range(m):
                Cell(i, j, r.choice([True, False]))
        return

    def stage(self):
        for i in p.event.get():
            if i.type == QUIT:
                quit()
        for s in Cell.cells:
            p.draw.rect(size, (game_colour if s.alive else background), [s.coor2 * 25, s.coor1 * 25, 25, 25])
        self.krug += 1


        new_cells = set()
        for cell in Cell.cells:
            new_cell = copy.deepcopy(cell)
            if cell.neibours() not in (2, 3):
                new_cell.kill()
            if cell.neibours() == 3:
                new_cell.rekyrsia()
            new_cells.add(new_cell)
        Cell.cells = copy.deepcopy(new_cells)
        p.display.update()
        return

    def play(self):
        self.setup()
        while 1:
            self.stage()
        return


a = Game(n, m)
a.play() 