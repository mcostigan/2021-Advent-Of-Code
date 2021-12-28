import math
import networkx


def model(d_x, d_y, box):
    pos = [0, 0]
    t = 0
    while pos[1] >= box[-1] and pos[0] < box[1]:
        t += 1
        pos[0] += d_x
        pos[1] += d_y
        d_x = max(d_x - 1, 0)
        d_y -= 1
        if box[0] <= pos[0] <= box[1] and box[2] >= pos[1] >= box[3]:
            return True
    return False


if __name__ == '__main__':
    # Part 1: algebraic solution
    # projectile will take a "symmetrical" route 1,2,...n-1,n,n-1...,2,1
    # so all projectiles, regardless of initial velocity return to vertical displacement 0
    # the maximum speed it can be going after position 0 is the bottom border of the target.
    # in example data box:=(20, 30, -5, -10), it can reach 0 and then travel 10 units in the next second and still intersect
    # if it intersects at velocity n, then it was at velocity n-1 at vertical displacement=0, when it was initially shot and when it returns
    # so max vert height = b-1(b)/2 where b is the abs(bottom border of the box)

    box = (20, 30, -5, -10)
    max_vert = (abs(box[-1]) - 1) * abs(box[-1]) / 2
    print('maximum vertical height:', max_vert)

    # Part 2: brute force (sorry!)
    # calculate min and max x and y velocities
    x_range = range(int(math.sqrt(box[0] * 2)), box[1] + 1)
    y_range = range(box[-1], -box[-1] + 1)

    # test every combination within range
    cnt = 0
    for x in x_range:
        for y in y_range:
            if model(x, y, box):
                cnt += 1
    print(cnt)
