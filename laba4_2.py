import tkinter as tk
import random
import time


class Ball:
    def __init__(self, _x, _y, _r, vx, vy, a_x=0, a_y=0, color='black'):
        self.x_acceleration = a_x
        self.y_acceleration = a_y
        self.v_x = vx
        self.v_y = vy
        self.x = _x
        self.y = _y
        self.r = _r
        self.ball = c.create_oval(_x - _r, _y - _r, _x + _r, _y + _r, fill=color, width=0)

    def ball_move(self):
        last_x = self.x
        last_y = self.y
        self.x += self.v_x
        self.y += self.v_y
        self.v_x += self.x_acceleration
        self.v_y += self.y_acceleration
        c.move(self.ball, self.x - last_x, self.y - last_y)

    def collision_with_ball(self, ball, enother_ball):
        if True:  # условие соударения с шаром
            return True
        else:
            return False

    def collision_with_wall(self, ball, wall):
        d_x = 0
        d_y = 0
        if wall == 'right':
            if ball.x + ball.r - d_x > WW:  # условие столкновения со стеной
                return True
            else:
                return False
        elif wall == 'left':
            if ball.x + ball.r + d_x < 100:  # условие столкновения со стеной
                return True
            else:
                return False
        elif wall == 'up':
            if ball.y + ball.r + d_y < 100:  # условие столкновения со стеной
                return True
            else:
                return False
        else:
            if ball.y + ball.r - d_y > WH:  # условие столкновения со стеной
                return True
            else:
                return False


class Field(Ball):
    def __init__(self):
        Ball.__init__(self, 0, 0, 0, 0, 0)
        self.balls = []
        c.bind('<Button-1>', self.click)

    def click(self, event):
        global score, score_text
        try:
            for i in range(len(self.balls)):
                if (self.balls[i].x - event.x) ** 2 + (self.balls[i].y - event.y) ** 2 < self.balls[i].r ** 2:
                    c.delete(self.balls[i].ball)
                    del self.balls[i]
                    score += 1
                    c.delete(score_text)
                    score_text = c.create_text(1450, 10, text=str(score), font='Verdana 14')
        except IndexError:
            pass

    def generation_of_ball(self):
        x = random.randrange(100, 700)
        y = random.randrange(100, 500)
        r = random.randrange(30, 50)
        d_x = random.randrange(-10, 10)
        d_y = random.randrange(-10, 10)
        a_x = random.randrange(-2, 2)
        a_y = random.randrange(-2, 2)
        self.balls.append(Ball(x, y, r, d_x, d_y, a_x, a_y, random.choice(colors)))

    def collision_handling(self):
        for i in range(len(self.balls) - 1):
            for j in range(i, len(self.balls)):
                if self.collision_with_ball(self.balls[i], self.balls[j]):
                    pass
                    """ написать функцию соударения шаров """
            if self.collision_with_wall(self.balls[i], 'right'):
                self.balls[i].v_x *= -1
            if self.collision_with_wall(self.balls[i], 'left'):
                self.balls[i].v_x *= -1
            if self.collision_with_wall(self.balls[i], 'up'):
                self.balls[i].v_y *= -1
            if self.collision_with_wall(self.balls[i], 'down'):
                self.balls[i].v_y *= -1
        try:
            if self.collision_with_wall(self.balls[-1], 'right'):
                self.balls[-1].v_x *= -1
            if self.collision_with_wall(self.balls[-1], 'left'):
                self.balls[-1].v_x *= -1
            if self.collision_with_wall(self.balls[-1], 'up'):
                self.balls[-1].v_y *= -1
            if self.collision_with_wall(self.balls[-1], 'down'):
                self.balls[-1].v_y *= -1
        except IndexError:
            pass

    def movement(self):
        for i in self.balls:
            i.ball_move()


def update_table(name, score):
    flag = True
    q = 1
    a = []
    table = open("Best_Players.txt")
    for line in table:
        a.append((int(line.split(' | ')[2]), line.split(' | ')[1]))
    table.close()
    for i in range(len(a)):
        if a[i][1] == name:
            a[i] = (score, name)
            flag = False
    if flag:
        a.append((score, name))
    a.sort(key=lambda x: x[0], reverse=True)
    table = open("Best_Players.txt", 'w')
    for i in a:
        table.write(str(q) + ' | ' + i[1] + ' | ' + str(i[0]) + '\n')
        q += 1
    table.close()


WW = 1500
WH = 800
root = tk.Tk()
root.geometry('1500x800+0+0')
c = tk.Canvas(root, width=WW, height=WH, bg='white')
c.pack()
colors = ['black', 'yellow', 'green', 'blue']

f = Field()
for i in range(10):
    f.generation_of_ball()
score = 0
speed = 0
iteration = 0
score_text = c.create_text(1450, 10, text=str(score), font='Verdana 14')
name = input('Enter your name: ')


def upd():
    try:
        table = open("Best_Players.txt")
    except FileNotFoundError:
        table = open("Best_Players.txt", 'w')
        table.write('1' + ' | ' + ' Vasya' + ' | ' + '666' + '\n' + '2' + ' | ' + ' Gosha' + ' | ' + '103' + '\n')
        table.close()
    global speed, iteration, name, score
    f.collision_handling()
    f.movement()
    if len(f.balls) > 40 or len(f.balls) == 7:
        update_table(name, score)
        exit()
    if score > 5 and speed == 0:
        speed = 2
    elif score > 10 and speed == 2:
        speed = 3
    elif score > 20 and speed == 3:
        speed = 5
    elif score > 40 and speed == 5:
        speed = 8
    if speed and iteration % 50 * speed == 0:
        iteration = 0
        f.generation_of_ball()
    root.after(40, upd)
    iteration += 1


upd()
tk.mainloop()
