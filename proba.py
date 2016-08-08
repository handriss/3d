from math import *

node0 = [300, 200]


def rotate_z(theta, node):
    sin_t = sin(radians(theta))
    cos_t = cos(radians(theta))

    x = node[0]
    y = node[1]

    # node[0] = x * cos_t - y * sin_t
    # node[1] = y * cos_t + x * cos_t
    print(x * cos_t - y * sin_t)
    print(y * cos_t + x * cos_t)

    # return node

for i in range(1):
    rotate_z(i, node0)
    print("\n")
