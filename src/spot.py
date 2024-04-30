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
        self.neighbours = []
        ## Methodology ---
        ## check we arent on the the edge of the grid and check spot in given direction is not a barrier
        ## if so add spot in given direction into list of neighbours

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): ## Spot Below
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): ## Spot Above
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): ## Spot to Right
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): ## Spot to Left
            self.neighbours.append(grid[self.row][self.col - 1])

    ## less than, for comparing spot objects
    def __lt__(self, other):
        return False