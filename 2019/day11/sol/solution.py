from intcode import IntCode
from pixgrid import Grid
import numpy as np

with open("11.dat", "r") as f:
    raw = f.readline()
    code = [int(v) for v in raw.split(",")]


class Robot:
    def __init__(self):
        # intcode output buffer
        self.buf = None

        # colors
        self.BLACK = 0
        self.WHITE = 1

        # directions
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3

        self.coord = (0, 0)  # current coord in arbitrarily-sized grid
        self.coords = dict()  # visited coords
        self.robdir = self.UP  # robot direction

        # movement deltas for each turn motion
        # (x,y)
        self.deltas = [
            (0, 1),  # up
            (0, -1),  # down
            (-1, 0),  # left
            (1, 0)  # right
        ]

        # number of painted squares
        self.painted = 0
        # counter for determining read mode (color or turn direction)
        self.mode = 0

    def getdir(self, dir, turn_right):
        # get new turn direction based on current robot direction
        if dir == self.UP:
            return self.RIGHT if turn_right else self.LEFT
        elif dir == self.DOWN:
            return self.LEFT if turn_right else self.RIGHT
        elif dir == self.LEFT:
            return self.UP if turn_right else self.DOWN
        elif dir == self.RIGHT:
            return self.DOWN if turn_right else self.UP

    def getdelta(self, curdir, turn_right):
        # get new turn direction and movement delta,
        # based on current direction and turn motion (left/right)
        newdir = self.getdir(curdir, turn_right)
        return (newdir, self.deltas[newdir])

    def send_square(self):
        if self.coord in self.coords:
            # get color of already visited square
            return self.coords[self.coord]
        if self.mode == 0:
            # initial state: starting on a white square
            return self.WHITE
        else:
            # unvisited squares are black
            return self.BLACK

    def read_robot(self, v):
        # mode
        #  * odd: turn direction
        #  * even: color
        if self.mode % 2:
            # got turn command, read color command from buffer
            c = self.buf
            d = v
            # color
            if self.coord in self.coords:
                if self.coords[self.coord] != c:
                    # change color of already painted square
                    self.coords[self.coord] = c
                    # misunderstood instructions. thought these should count as
                    # painted for part A...
                    # but nope, no need for 'self.painted += 1' here
            else:
                # paint new square
                self.coords[self.coord] = c
                if c == self.WHITE:
                    self.painted += 1
            # turn direction
            newdir, delta = self.getdelta(self.robdir, d)
            self.robdir = newdir
            xd, yd = delta
            self.coord = (self.coord[0] + xd, self.coord[1] + yd)
            # clear command buffer
            self.buf = None
        else:
            # got color command, store it in buffer
            self.buf = v
        self.mode += 1


ic = IntCode(code)
rob = Robot()

ic.set_input_func(rob.send_square)
ic.set_output_func(rob.read_robot)
ic.parse()

print("Painted squares:")
print(rob.painted)

# and now for the obligatory ugly hard-coding to finalize it all!
maxx, maxy, minx, miny = 0, 0, 0, 0
for k, v in rob.coords.items():
    # get max and min grid coords
    x, y = k
    maxx = max(x, maxx)
    minx = min(x, minx)
    maxy = max(y, maxy)
    miny = min(y, miny)

# grid size
w = maxx - minx
h = maxy - miny

# create grid and plot points in it
g = Grid(w, h + 1)  # account for overflow
for k, v in rob.coords.items():
    if v:
        x, y = k
        # invert negative y. in space there's no real concept of up or down ;-)
        y *= -1
        g.plot(x, y)

print("Solution for B:")
g.to_ascii()
