from spot import Spot
from settings import *
import pygame as pg

class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.gap = width // rows

    def make_grid(self):
        """
        Makes a grid of spot objects ion the form of nested lists
        """
        grid = []

        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                spot = Spot(i, j, self.gap, self.rows)
                grid[i].append(spot)

        return grid
    
    def draw_grid(self, win):
        for i in range(self.rows):
            ## for every row draw a horizontal line 
            pg.draw.line(win, GREY, (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
            ## for every row draw a vertical line 
                pg.draw.line(win, GREY, (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self, win, grid):
        """
        This will draw everything on to the screen
        """
        win.fill(WHITE)

        for row in grid:
            for spot in row:
                spot.draw(win)

        self.draw_grid(win)
        pg.display.update()

    def get_clicked_position(self, position):
        """
        Returns which box (row/column value) we are at for a given x, y position
        """
        y, x = position

        row = y // self.gap
        col = x // self.gap

        return row, col