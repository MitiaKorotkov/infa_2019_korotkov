import graph
import math


def my_line(_x0, _y0, _x1, _y1, color="black"):
    if _y0 == _y1:
        for i in range(int(abs(_x0 - _x1))):
            graph.point(_y0, _x0 + i, color)
    elif abs(_x0 - _x1) > abs(_y0 - _y1):
        if _x0 > _x1:
            _x0, _x1 = _x1, _x0
        k = (_y0 - _y1) / (_x0 - _x1 + 0.001)
        for _x0 in range(_x0, _x1):
            graph.point(_x0, _y0, color)
            _y0 += k
    else:
        if _y0 > _y1:
            _y0, _y1 = _y1, _y0
        k = (_x0 - _x1) / (_y0 - _y1 + 0.001)
        for _y0 in range(_y0, _y1):
            graph.point(_x0, _y0, color)
            _x0 += k


def my_rectangle(_x1, _y1, _x2, _y2, color="black"):
    graph.line(_x1, _y1, _x1, _y2)
    graph.line(_x1, _y2, _x2, _y2)
    graph.line(_x2, _y2, _x2, _y1)
    graph.line(_x2, _y1, _x1, _y1)


def my_triangle(_x1, _y1, _x2, _y2, _x3, _y3, color):
    my_line(_x1, _y1, _x2, _y2, color)
    my_line(_x2, _y2, _x3, _y3, color)
    my_line(_x3, _y3, _x1, _y1, color)


def my_filltriangle(_x1, _y1, _x2, _y2, _x3, _y3, color="black"):
    flag = True
    print(_x1, _y1)
    print(_x2, _y2)
    print(_x3, _y3)
    if _y1 > _y2:
        y = _y1
        x = _x1
        _x1, _y1 = _x2, _y2
        _x2, _y2 = x, y
    if _y1 > _y3:
        y = _y1
        x = _x1
        _x1, _y1 = _x3, _y3
        _x3, _y3 = x, y
    if _y2 > _y3:
        y = _y2
        x = _x2
        _x2, _y2 = _x3, _y3
        _x3, _y3 = x, y
    print(_x1, _y1)
    print(_x2, _y2)
    print(_x3, _y3)
    k12 = (_y1 - _y2) / (_x1 - _x2 + 0.001)
    k13 = (_y1 - _y3) / (_x1 - _x3 + 0.001)
    k23 = (_y2 - _y3) / (_x2 - _x3 + 0.001)
    b12 = _y1 - k12 * _x1
    b13 = _y1 - k13 * _x1
    b23 = _y2 - k23 * _x2
    for i in range(_y2 - _y1):
        if i % 10 == 0:
            flag = not flag
        if flag:
            graph.penColor("black")
        else:
            graph.penColor("white")
        graph.line((_y1 + i - b12) / k12, _y1 + i, (_y1 + i - b13) / k13, _y1 + i)
    for i in range(_y3 - _y2):
        if i % 10 == 0:
            flag = not flag
        if flag:
            graph.penColor("black")
        else:
            graph.penColor("white")
        graph.line((_y2 + i - b23) / k23, _y2 + i, (_y2 + i - b13) / k13, _y2 + i)
    graph.penColor("black")


def my_fillrectangle(v1, v2, angle=50, d=10):
    flag = True
    if v1[0] > v2[0]:
        v1, v2 = v2, v1
    if v1[1] > v2[1]:
        a = v1[1]
        b = v2[1]
        v1[1] = b
        v2[1] = a
    if angle > 45:
        for i in range(int((1 + math.tan(angle * 3.14 / 180)) * (v2[0] - v1[0]))):
            if i % d == 0:
                flag = not flag
            if flag:
                graph.penColor("black")
            else:
                graph.penColor("white")

            if v2[0] - i / math.tan(angle * 3.14 / 180) < v1[0]:

                if v2[1] - i < v1[1]:
                    delta1 = (i - v2[1] + v1[1]) / math.tan(angle * 3.14 / 180)
                    delta = (v1[0] - v2[0] + i / math.tan(angle * 3.14 / 180)) * math.tan(angle * 3.14 / 180)
                    graph.line(v2[0] - delta1, v1[0], v1[0], v2[1] - delta)
                else:
                    delta = (v1[0] - v2[0] + i / math.tan(angle * 3.14 / 180)) * math.tan(angle * 3.14 / 180)
                    graph.line(v2[0], v2[1] - i, v1[0], v2[1] - delta)

            else:
                graph.line(v2[0], v2[1] - i, v2[0] - i / math.tan(angle * 3.14 / 180), v2[1])
    else:
        for i in range(int((1 + math.tan(angle * 3.14 / 180)) * (v2[0] - v1[0]))):
            if i % d == 0:
                flag = not flag
            if flag:
                graph.penColor("black")
            else:
                graph.penColor("white")

            if v2[0] - i / math.tan(angle * 3.14 / 180) < v1[0]:

                if v2[1] - i < v1[1]:
                    delta1 = (i - v2[1] + v1[1]) / math.tan(angle * 3.14 / 180)
                    delta = (v1[0] - v2[0] + i / math.tan(angle * 3.14 / 180)) * math.tan(angle * 3.14 / 180)
                    graph.line(v2[0] - delta1, v1[0], v1[0], v2[1] - delta)
                else:
                    delta = (v1[0] - v2[0] + i / math.tan(angle * 3.14 / 180)) * math.tan(angle * 3.14 / 180)
                    graph.line(v2[0], v2[1] - i, v1[0], v2[1] - delta)

            else:
                graph.line(v2[0], v2[1] - i, v2[0] - i / math.tan(angle * 3.14 / 180), v2[1])
    my_rectangle(v1[0], v1[1], v2[0], v2[1])


if __name__ == '__main__':
    a = (1, 2)
    print(a[0])

    my_fillrectangle([10, 10], [150, 100])
    # my_line(10, 100, 10, 10)
    graph.run()
