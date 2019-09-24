import graph
import math


def vertex_projection(_x, _y, _z):
    a = (Cw / 2 - l * (_x - Vw / 2) / (l + d + _y), Ch / 2 - l * (_z - Vh / 2) / (l + d + _y))
    return a


def matrix_multiply(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            c[i].append(0)
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c


def draw_cube(Cube):
    graph.line(vertex_projection(Cube[0][0], Cube[0][1], Cube[0][2])[0],
               vertex_projection(Cube[0][0], Cube[0][1], Cube[0][2])[1],
               vertex_projection(Cube[1][0], Cube[1][1], Cube[1][2])[0],
               vertex_projection(Cube[1][0], Cube[1][1], Cube[1][2])[1])
    graph.line(vertex_projection(Cube[1][0], Cube[1][1], Cube[1][2])[0],
               vertex_projection(Cube[1][0], Cube[1][1], Cube[1][2])[1],
               vertex_projection(Cube[2][0], Cube[2][1], Cube[2][2])[0],
               vertex_projection(Cube[2][0], Cube[2][1], Cube[2][2])[1])
    graph.line(vertex_projection(Cube[3][0], Cube[3][1], Cube[3][2])[0],
               vertex_projection(Cube[3][0], Cube[3][1], Cube[3][2])[1],
               vertex_projection(Cube[2][0], Cube[2][1], Cube[2][2])[0],
               vertex_projection(Cube[2][0], Cube[2][1], Cube[2][2])[1])
    graph.line(vertex_projection(Cube[3][0], Cube[3][1], Cube[3][2])[0],
               vertex_projection(Cube[3][0], Cube[3][1], Cube[3][2])[1],
               vertex_projection(Cube[0][0], Cube[0][1], Cube[0][2])[0],
               vertex_projection(Cube[0][0], Cube[0][1], Cube[0][2])[1])

    graph.line(vertex_projection(Cube[4][0], Cube[4][1], Cube[4][2])[0],
               vertex_projection(Cube[4][0], Cube[4][1], Cube[4][2])[1],
               vertex_projection(Cube[5][0], Cube[5][1], Cube[5][2])[0],
               vertex_projection(Cube[5][0], Cube[5][1], Cube[5][2])[1])
    graph.line(vertex_projection(Cube[5][0], Cube[5][1], Cube[5][2])[0],
               vertex_projection(Cube[5][0], Cube[5][1], Cube[5][2])[1],
               vertex_projection(Cube[6][0], Cube[6][1], Cube[6][2])[0],
               vertex_projection(Cube[6][0], Cube[6][1], Cube[6][2])[1])
    graph.line(vertex_projection(Cube[7][0], Cube[7][1], Cube[7][2])[0],
               vertex_projection(Cube[7][0], Cube[7][1], Cube[7][2])[1],
               vertex_projection(Cube[6][0], Cube[6][1], Cube[6][2])[0],
               vertex_projection(Cube[6][0], Cube[6][1], Cube[6][2])[1])
    graph.line(vertex_projection(Cube[7][0], Cube[7][1], Cube[7][2])[0],
               vertex_projection(Cube[7][0], Cube[7][1], Cube[7][2])[1],
               vertex_projection(Cube[4][0], Cube[4][1], Cube[4][2])[0],
               vertex_projection(Cube[4][0], Cube[4][1], Cube[4][2])[1])

    graph.line(vertex_projection(Cube[4][0], Cube[4][1], Cube[4][2])[0],
               vertex_projection(Cube[4][0], Cube[4][1], Cube[4][2])[1],
               vertex_projection(Cube[0][0], Cube[0][1], Cube[0][2])[0],
               vertex_projection(Cube[0][0], Cube[0][1], Cube[0][2])[1])
    graph.line(vertex_projection(Cube[5][0], Cube[5][1], Cube[5][2])[0],
               vertex_projection(Cube[5][0], Cube[5][1], Cube[5][2])[1],
               vertex_projection(Cube[1][0], Cube[1][1], Cube[1][2])[0],
               vertex_projection(Cube[1][0], Cube[1][1], Cube[1][2])[1])
    graph.line(vertex_projection(Cube[7][0], Cube[7][1], Cube[7][2])[0],
               vertex_projection(Cube[7][0], Cube[7][1], Cube[7][2])[1],
               vertex_projection(Cube[3][0], Cube[3][1], Cube[3][2])[0],
               vertex_projection(Cube[3][0], Cube[3][1], Cube[3][2])[1])
    graph.line(vertex_projection(Cube[6][0], Cube[6][1], Cube[6][2])[0],
               vertex_projection(Cube[6][0], Cube[6][1], Cube[6][2])[1],
               vertex_projection(Cube[2][0], Cube[2][1], Cube[2][2])[0],
               vertex_projection(Cube[2][0], Cube[2][1], Cube[2][2])[1])


def update():
    global cube
    graph.penColor("white")
    draw_cube(cube)
    graph.penColor("black")
    cube = matrix_multiply(cube, Mz)
    # cube = matrix_multiply(cube, My)
    # cube = matrix_multiply(cube, Mx)
    draw_cube(cube)


if __name__ == '__main__':
    d = 400
    l = 1000
    Cw = 500
    Ch = 600
    Vw = 500
    Vh = 600

    graph.windowSize(Cw, Ch)

    cube = [[100, 100, 0], [200, 100, 0], [200, 100, 100], [100, 100, 100], [100, 200, 0], [200, 200, 0],
            [200, 200, 100],
            [100, 200, 100]]

    angle = 5 * math.pi / 180
    Mz = [[math.cos(angle), -math.sin(angle), 0],
          [math.sin(angle), math.cos(angle), 0],
          [0, 0, 1]]
    My = [[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]]
    Mx = [[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]]

    graph.onTimer(update, 60)
    graph.run()
