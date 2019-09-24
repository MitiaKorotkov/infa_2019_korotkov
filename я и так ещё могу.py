import graph


def my_line(_x0, _y0, _x1, _y1, color="black"):
    if _y0 == _y1:
        for i in range(int(abs(_x0 - _x1))):
            graph.point(_y0, _x0 + i, color)
    elif abs(_x0 - _x1) > abs(_y0 - _y1):
        if _x0 > _x1:
            _x0, _x1 = _x1, _x0
        k = (_y0 - _y1) / (_x0 - _x1)
        for _x0 in range(_x0, _x1):
            graph.point(_x0, _y0, color)
            _y0 += k
    else:
        if _y0 > _y1:
            _y0, _y1 = _y1, _y0
        k = (_x0 - _x1) / (_y0 - _y1)
        for _y0 in range(_y0, _y1):
            graph.point(_x0, _y0, color)
            _x0 += k


def my_rectangle(_x1, _y1, _x2, _y2, color="black"):
    my_line(_x1, _y1, _x1, _y2, color)
    my_line(_x1, _y2, _x2, _y2, color)
    my_line(_x2, _y2, _x2, _y1, color)
    my_line(_x2, _y1, _x1, _y1, color)


def my_triangle(_x1, _y1, _x2, _y2, _x3, _y3, color):
    my_line(_x1, _y1, _x2, _y2, color)
    my_line(_x2, _y2, _x3, _y3, color)
    my_line(_x3, _y3, _x1, _y1, color)


def my_filltriangle(_x1, _y1, _x2, _y2, _x3, _y3, color="black"):
    flag = True
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
    k12 = (_y1 - _y2) / (_x1 - _x2)
    k13 = (_y1 - _y3) / (_x1 - _x3)
    k23 = (_y2 - _y3) / (_x2 - _x3)
    b12 = _y1 - k12 * _x1
    b13 = _y1 - k13 * _x1
    b23 = _y2 - k23 * _x2
    for i in range(_y2 - _y1):
        if i % 10 == 0:
            flag = not flag
        if flag:
            color = "black"
        else:
            color = "white"
        my_line((_y1 + i - b12) / k12, _y1 + i, (_y1 + i - b13) / k13, _y1 + i, color)
    for i in range(_y3 - _y2):
        if i % 10 == 0:
            flag = not flag
        if flag:
            color = "black"
        else:
            color = "white"
        my_line((_y2 + i - b23) / k23, _y2 + i, (_y2 + i - b13) / k13, _y2 + i, color)


if __name__ == '__main__':
    a = (1, 2)
    print(a[0])

    my_filltriangle(220, 15, 135, 135, 280, 190)
    # my_line(10, 100, 10, 10)
    graph.run()
