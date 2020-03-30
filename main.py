#!/usr/bin/python3

import tkinter
from tkinter import Canvas
from random import choice, randint

def run():
    global balls
    while True:
        for b in balls:
            b.move()
        canvas.update()

class ball:
    '''
        This is a lass of ball, for create ball create object ans send radius to constructor

        For example: 
            ball1 = ball(45)

        Author: Ilyosiddin Kalandar 2020(C)
        A special thanks to http://younglinux.info for tkinter tutorial
    '''
    def choice_move_to1(self):
        positions = ['LEFT','RIGHT','RIGHT']
        self.move_to = choice(positions)
        
    def choice_move_to2(self):
        positions = ['UP','LOW']
        self.move_to2 = choice(positions)

    def __init__(self,radius):
        colors = [
            'lightblue','lightgreen','red','blue','brown','green','pink', 'magenta', 'yellow','orange'
        ]
        self.choice_move_to1()
        self.choice_move_to2()
        self.STEP = 0.05
        self.x1 =  0
        self.y1 =  0
        self.x2 = radius * 2
        self.y2 = radius * 2
        color = choice(colors)
        self.ball_object = canvas.create_oval(0,0,radius*2,radius*2,fill=color)

    def move_low(self): 
        if self.y2 < 500:
            canvas.move(self.ball_object, 0, self.STEP)
            self.y1 += self.STEP
            self.y2 += self.STEP
        else:
            self.choice_move_to1()
            return "Impossible"

    def move_up(self):
        if self.y1 > 0:
            canvas.move(self.ball_object, 0, -self.STEP)
            self.y2 -= self.STEP
            self.y1 -= self.STEP
        else:
            return "Impossible"

    def move_to_right(self):
        if self.x2 < 500:
            canvas.move(self.ball_object, self.STEP, 0)
            self.x1 += self.STEP
            self.x2 += self.STEP
            self.choice_move_to2()
        else:
            return "Impossible"

    def move_to_left(self):
        if self.x1 > 0:
            canvas.move(self.ball_object, -self.STEP, 0)
            self.x1 -= self.STEP
            self.x2 -= self.STEP
        else:
            self.choice_move_to2()
            return 'Impossible'

    def move(self):
        if self.move_to == 'LEFT':
            if self.move_to_left():
                self.move_to = 'RIGHT'

        elif self.move_to == 'RIGHT':
            if self.move_to_right():
                self.move_to = 'LEFT'

        if self.move_to2 == 'UP':
            if self.move_up():
                self.move_to2 = "LOW"
        elif self.move_to2 == 'LOW':
            if self.move_low():
                self.move_to2 = "UP"
        
if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('500x600')
    canvas = Canvas(width=500,height=500,bg='black')
    canvas.pack()
    root.resizable(False, False)
    root.title('Balls.Py by Ilyosiddin =)')    
    balls = [ball(randint(40,80)) for i in range(5)]
    bt = tkinter.Button(text='RUN GAME!',command=run)
    bt.pack()
    root.mainloop()
