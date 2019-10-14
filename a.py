import tkinter as tk
import random
import time


class Ball:
    def __init__(self, _x, _y, r, vx, vy, color='black'):
        self.v_x = vx
        self.v_y = vy
        self.ball = c.create_oval(_x - r, _y - r, _x + r, _y + r, fill=color, width=0)

    def ball_move(self, d_x, d_y):
        c.move(self.ball, d_x, d_y)

    def collision_with_ball(self, enother_ball):
        if True:  # условие соударения с шаром
            return True
        else:
            return False

    def collision_with_wall(self, wall):
        if True:  # условие столкновения со стеной
            return True
        else:
            return False


class Field(Ball):

    def __init__(self):
        self.balls = []

    def generation_of_ball(self):
        x = random.randrange(100, 700)
        y = random.randrange(100, 500)
        r = random.randrange(30, 50)
        d_x = random.randrange(5, 10)
        d_y = random.randrange(5, 10)
        self.balls.append(Ball(x, y, r, d_x, d_y, random.choice(colors)))

    def collision_handling(self):
        for i in range(len(self.balls) - 2):
            for j in range(i, len(self.balls) - 1):
                if self.collision_with_ball(self.balls[i], self.balls[j]):
                    pass
                    """ написать функцию соударения шаров """
                if self.collision_with_wall(self, 'right'):
                    pass
                if self.collision_with_wall(self, 'left'):
                    pass
                if self.collision_with_wall(self, 'up'):
                    pass
                if self.collision_with_wall(self, 'down'):
                    pass


root = tk.Tk()
root.geometry('1600x900+0+0')
c = tk.Canvas(root, width=1600, height=900, bg='white')
c.pack()
colors = ['black', 'yellow', 'green', 'blue']

f = Field()
b = Ball(20, 20, 20, 1, 1)


def upd():
    b.ball_move(b.v_x, b.v_y)
    f.collision_handling()
    if False:
        f.generation_of_ball()

    root.after(40, upd)


upd()
tk.mainloop()
