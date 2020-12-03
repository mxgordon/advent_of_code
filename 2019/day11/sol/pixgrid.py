class Grid:
    def __init__(self, w, h, grid=None):
        self.w = w
        self.h = h
        if not grid:
            self.grid = []
            self.mkgrid()
        else:
            self.grid = grid

    def mkgrid(self):
        for r in range(self.h):
            self.grid.append([])
            for c in range(self.w):
                self.grid[-1].append(0)

    def plot(self, x, y):
        try:
            self.grid[y][x] = 1
        except IndexError as ex:
            print("IndexError x %s y %s" % (x, y))
            exit()

    def to_ascii(self, fg="O", bg=" "):
        print("+" + ("-" * (self.w)) + "+")
        for r in self.grid:
            s = "|"
            s += ''.join([fg if p else bg for p in r])
            print(s + "|")
        print("+" + ("-" * (self.w)) + "+")

    def out(self):
        for row in self.grid:
            print(row)
