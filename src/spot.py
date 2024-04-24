from settings import *
import pygame as pg

class Spot:
    
    def __init__(self, row, col, width, total_rows) -> None:
        self.row = row
        self.col = col
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.x = row * width
        self.y = col * width
        self.total_rows = total_rows

    """
    Methods to check state of a Spot
    """
    def get_position(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.colour == RED
    
    def is_open(self):
        return self.colour == GREEN
    
    def is_barrier(self):
        return self.colour == BLACK
    
    def is_start(self):
        return self.colour == ORANGE
    
    def is_end(self):
        return self.colour == TURQUOISE
    
    
    def reset(self):
        self.colour = WHITE

    """
    Methods to update state of a Spot
    """
    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_barrier(self):
        self.colour = BLACK

    def make_start(self):
        self.colour = ORANGE

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE


    def draw(self, win):
        pg.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        pass

    ## less than, for comparing spot objects
    def __lt__(self, other):
        return False