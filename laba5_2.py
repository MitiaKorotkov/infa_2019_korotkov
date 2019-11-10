from random import randrange as rnd, choice, randint
import tkinter as tk
import math
import time

root = tk.Tk()
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.focus_set()
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x, y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x + self.vx < 0:
            self.vx *= -1
        if self.x + self.vx > 800:
            self.vx *= -1
        if self.y - self.vy < 0:
            self.vy *= -1
        if self.y - self.vy > 600:
            self.vy *= -1

        self.vy -= 1
        if 0 < self.x + self.vx < 800:
            self.x += self.vx
        if 0 < self.y - self.vy < 600:
            self.y -= self.vy
        self.set_coords()

        self.vx -= 0.05 * self.vx / abs(self.vx)
        self.vy -= 0.05 * self.vy / abs(self.vy)

        if abs(self.vx) - 0.05 < 0 and abs(self.vy) - 0.05 < 0:
            canv.delete(self.id)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 > (self.r + obj.r) ** 2:
            return False
        else:
            return True


class gun():
    def __init__(self):
        self.x = 50
        self.y = 400
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30,
                                   width=7)  # FIXME: don't know how to set it...

    def move_up(self, event):
        self.y -= 2
        canv.move(self.id, 0, -2)

    def move_down(self, event):
        self.y += 2
        canv.move(self.id, 0, 2)

    def move_right(self, event):
        self.x += 2
        canv.move(self.id, 0, 2)

    def move_left(self, event):
        self.x -= 2
        canv.move(self.id, 0, -2)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.x - self.x) / abs(event.x - self.x) > 0:
                self.an = math.atan((event.y - self.y) / (event.x - self.x))
            else:
                self.an = -math.pi + math.atan((event.y - self.y) / (event.x - self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.vx = randint(1, 4)
        self.vy = randint(1, 4)
        self.points = 0
        self.live = 1

        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        if 5 > canv.coords(self.id)[0] or canv.coords(self.id)[0] > 795:
            self.vx *= -1
            self.x += self.vx
            canv.move(self.id, self.vx, 0)
        if 5 > canv.coords(self.id)[1] or canv.coords(self.id)[1] > 595:
            self.vy *= -1
            self.y += self.vy
            canv.move(self.id, 0, self.vy)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)


screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global t1, screen1, balls, bullet
    targets = []
    for i in range(2):
        targets.append(target())
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind("<Left>", g1.move_left)
    canv.bind("<Right>", g1.move_right)
    canv.bind("<Up>", g1.move_up)
    canv.bind("<Down>", g1.move_down)

    for i in targets:
        i.live = 1
    while len(targets) != 0 or balls:
        if len(balls) == 0:
            for i in targets:
                if (i.x < g1.x < i.x + i.r) and (i.y < g1.y < i.y + i.r):
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.bind("<Left>", '')
                    canv.bind("<Right>", '')
                    canv.bind("<Up>", '')
                    canv.bind("<Down>", '')
                    canv.bind('<Motion>', '')
                    canv.itemconfig(screen1, text='Вы проиграли')
                else:
                    i.move()
        for b in balls:
            if b.vx == 0 and b.vy == 0:
                canv.delete(b.id)
            b.move()
            for i in targets:
                if b.hittest(i) and i.live:
                    i.live = 0
                    i.hit()
                    targets.remove(i)
                if (i.x < g1.x < i.x + i.r) and (i.y < g1.y < i.y + i.r):
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.bind("<Left>", '')
                    canv.bind("<Right>", '')
                    canv.bind("<Up>", '')
                    canv.bind("<Down>", '')
                    canv.bind('<Motion>', '')
                    canv.itemconfig(screen1, text='Вы проиграли')
                else:
                    i.move()
        if len(targets) == 0:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()
tk.mainloop()
