from re import S
# from networkx import reconstruct_path
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

    def h(self, p1, p2):
        ## heuristic function, this gives us the L distance between 2 points
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def reconstruct_path(self, came_from, current, draw):
        ## current node starts at end
        ## iterate through came from basically walking back through path that we came from
        ## start node not in came from so once we reach start, iteration will stop
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()
    
    def algorithm(self, draw, grid, start, end):
        count = 0
        open_set = PriorityQueue()
        ## f score, count for counting what was added first, and spot location
        ## always start by adding start node to the open set
        open_set.put((0, count, start))

        came_from = {}

        ## g_score is current shortest distance to get from start node to current node
        g_score = {spot: float("inf") for row in grid for spot in row}
        g_score[start] = 0

        ## f_score is our predicted distance from current node to end node
        f_score = {spot: float("inf") for row in grid for spot in row}
        f_score[start] = self.h(start.get_position(), end.get_position())

        ## this set will store everything that is in the priority queue
        ## but will allow us to check what is in it
        open_set_hash = {start}

        while not open_set.empty():
            for event in pg.event.get():
                ## this loop called within main game loop so we need a way to exit within this 
                if event.type == pg.QUIT:
                    pg.quit()

            ## priority queue gets us the minimal element from the queue each time
            current = open_set.get()[2]
            ## index 2 gets us the node 
            open_set_hash.remove(current)

            if current == end:
                ## this mean we have made it to the end node
                ## here we make path
                self.reconstruct_path(came_from, end, draw)
                end.make_end()
                start.make_start()
                return True
            
            for neighbour in current.neighbours:
                temp_g_score = g_score[current] + 1
                ## since neighbour is one node over form current node, makes sense to + 1 to g score from current node

                if temp_g_score < g_score[neighbour]:
                    ## if we have found a better way to reach this neighbour than before
                    ## update the path to get there
                    came_from[neighbour] = current
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_g_score + self.h(neighbour.get_position(), end.get_position())

                    if neighbour not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbour], count, neighbour))
                        open_set_hash.add(neighbour)
                        neighbour.make_open()
                        ## as we have added to open set now

            draw()

            # if the node we have just considered is not the start node
            # make it red and close it off
            if current != start:
                current.make_closed()

        return False
    
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
                    if event.key == pg.K_SPACE and start and end:
                        ## here we start the algorithm
                        for row in grid:
                            for spot in row:
                                spot.update_neighbours(grid)

                        self.algorithm(lambda: grid_object.draw(self.window, grid), grid, start, end)

                    if event.key == pg.K_c:
                        ## clear the screen and reset the grid
                        start = None
                        end = None
                        grid = grid_object.make_grid()
        pg.quit()

## for testing
pf = PathFinder()
pf.main()