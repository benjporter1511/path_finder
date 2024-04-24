from re import S
import pygame as pg
import math
from queue import PriorityQueue
from settings import *
from grid import Grid

class PathFinder:

    def __init__(self) -> None:
        pg.init()
        self.window = pg.display.set_mode((WIDTH, WIDTH))

        pg.display.set_caption("Path Finding Algorithm")

    def h(p1, p2):
        ## heuristic function, this gives us the L distance between 2 points
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def main(self):
        grid_object = Grid(ROWS, WIDTH)
        grid = grid_object.make_grid()

        ## variables for start and end nodes
        start = None
        end = None

        # variables for program state
        run = True
        started = False

        """
        For Input:
        1. First left click should set the starting position (ORANGE)
        2. Second left click should set the end position (TURQUOISE)
        3. All other subsequent left clicks should set barrier nodes (BLACK)
        4. Right clicking will reset nodes, including start end which can be placed again
        5. Pressing spacebart will start the algorithm
        """

        while run:
            grid_object.draw(self.window, grid)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

                ## once started, we dont want to allow any input from the user that isnt the quit
                if started:
                    continue

                ## check mouse position
                if pg.mouse.get_pressed()[0]: ## left click
                    position = pg.mouse.get_pos()
                    row, col = grid_object.get_clicked_position(position)
                    spot = grid[row][col]

                    ## check if start position set
                    if not start and spot != end:
                        start = spot
                        start.make_start()
                    
                    ## next we set end position
                    elif not end and spot != start:
                        end = spot
                        end.make_end()

                    ## otherwise make a barrier square
                    elif spot != end and spot != start:
                        spot.make_barrier()

                elif pg.mouse.get_pressed()[2]: ## right click
                    position = pg.mouse.get_pos()
                    row, col = grid_object.get_clicked_position(position)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and not started:
                        ## here we start the algorithm
                        pass

        pg.quit()

## for testing
pf = PathFinder()
pf.main()