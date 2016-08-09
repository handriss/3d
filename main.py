from tkinter import *
from math import *
import time


class Rect(object):
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = self.width/2
        self.y = self.height/2

        self.offset_x = 400
        self.offset_y = 400

        node0 = [-100, -100]
        node1 = [100, 100]
        node2 = [100, -100]
        node3 = [-100, 100]
        self.oval0 = self.canvas.create_oval(
            self.offset_x+node0[0], self.offset_y+node0[1], self.offset_x+node0[0]+5,
            self.offset_y+node0[1]+5, fill="red"
        )
        self.oval1 = self.canvas.create_oval(
            100, 100, 105, 105, fill="red"
        )
        self.oval2 = self.canvas.create_oval(
            100, 300, 105, 305, fill="red"
        )
        self.oval3 = self.canvas.create_oval(
            300, 100, 305, 105, fill="red"
        )
        self.ova = self.canvas.create_oval(200, 200, 205, 205, fill="black")

        self.coords = []
        for i in range(360):
            time.sleep(0.005)
            shift_x, shift_y = self.rotate_z(1, node0)
            self.canvas.move(self.oval0, shift_x, shift_y)
            x1, y1, x2, y2 = self.canvas.coords(self.oval0)

            shift_x, shift_y = self.rotate_z(1, node1)
            self.canvas.move(self.oval1, shift_x, shift_y)
            shift_x, shift_y = self.rotate_z(1, node2)
            self.canvas.move(self.oval2, shift_x, shift_y)
            shift_x, shift_y = self.rotate_z(1, node3)
            self.canvas.move(self.oval3, shift_x, shift_y)
            self.canvas.update()

    def rotate_z(self, theta, node):
        sin_t = sin(radians(theta))
        cos_t = cos(radians(theta))
        x_temp = node[0]
        y_temp = node[1]
        x = node[0]
        y = node[1]

        node[0] = x * cos_t - y * sin_t
        node[1] = y * cos_t + x * sin_t

        return x_temp - node[0], y_temp - node[1]


class App(object):
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("tkinter_test01")
        self.root.geometry("{}x{}".format(self.width, self.height))

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.rect = Rect(self.canvas, 800, 800)
        self.root.mainloop()

if __name__ == "__main__":
    App()
