# from math import fabs
import copy
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

import numpy as np


class Planet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.pos = np.array((x, y, z))
        self.velocity = np.array((0, 0, 0))
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def update(self):
        self.x, self.y, self.z = tuple(self.pos)
        self.vx, self.vy, self.vz = tuple(self.velocity)

    def step(self):
        self.pos += self.velocity
        self.update()

    def __or__(self, other):
        for i in range(3):
            if self.pos[i] < other.pos[i]:
                self.velocity[i] += 1
                other.velocity[i] -= 1
            elif self.pos[i] > other.pos[i]:
                self.velocity[i] -= 1
                other.velocity[i] += 1
        return self, other

    def energy(self):
        return self.pos.__abs__().sum() * self.velocity.__abs__().sum()

    def __repr__(self):
        return f"Planet(x= {self.x}, y= {self.y}, z= {self.z}, " \
               f"vx= {self.vx}, vy= {self.vy}, vz= {self.vz})"


planets = [
    Planet(-4, 3, 15),  # io
    Planet(-11, -10, 13),  # europa
    Planet(2, 2, 18),  # ganymede
    Planet(7, -1, 0)  # callisto
]

io_pos = []
europa_pos = []
ganymede_pos = []
callisto_pos = []

# planets = [
#     Planet(x=-8, y=-10, z=0),
#     Planet(x=5, y=5, z=10),
#     Planet(x=2, y=-7, z=3),
#     Planet(x=9, y=-8, z=-3)
# ]

cop = copy.deepcopy(planets)


if __name__ == '__main__':

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')


    counter = 0

    while counter < 100:
        # print(counter) if counter % 100 == 0 else ''
        for i in range(len(planets)):

            # if i == 0:
            #     io_pos.append(planets[i].pos.copy())
            # elif i == 1:
            #     europa_pos.append(planets[i].pos.copy())
            # elif i == 2:
            #     ganymede_pos.append(planets[i].pos.copy())
            # elif i == 3:
            #     callisto_pos.append(planets[i].pos.copy())

            for j in range(len(planets)):
                if j > i:
                    planets[j], planets[j] = planets[i] | planets[j]
            planets[i].step()
        counter += 1
        # if planets == cop:
        #     print("--- DONE ---")
        #     print(counter)
        #     raise SystemExit
    print(len(io_pos))
    # print(io_pos)
    # # ax.plot((1, 2), (1, 2))
    # ax.plot(list(map(lambda x: x[0], io_pos)), list(map(lambda x: x[1], io_pos)), list(map(lambda x: x[2], io_pos)), 'b')
    #
    # ax.plot(list(map(lambda x: x[0], europa_pos)), list(map(lambda x: x[1], europa_pos)), list(map(lambda x: x[2], europa_pos)), 'r')
    #
    # ax.plot(list(map(lambda x: x[0], ganymede_pos)), list(map(lambda x: x[1], ganymede_pos)), list(map(lambda x: x[2], ganymede_pos)), 'g')
    # ax.plot(list(map(lambda x: x[0], callisto_pos)), list(map(lambda x: x[1], callisto_pos)), list(map(lambda x: x[2], callisto_pos)), 'y')
    #
    # ax.scatter(io_pos[-1][0], io_pos[-1][1], io_pos[-1][2], 'b')
    #
    # ax.scatter(europa_pos[-1][0], europa_pos[-1][1], europa_pos[-1][2], 'r')
    #
    # ax.scatter(ganymede_pos[-1][0], ganymede_pos[-1][1], ganymede_pos[-1][2], 'g')
    # ax.scatter(callisto_pos[-1][0], callisto_pos[-1][1], callisto_pos[-1][2], 'yp')


    # plt.show()

    print(sum(map(lambda x: x.energy(), planets)))
    print(*planets, sep='\n')

