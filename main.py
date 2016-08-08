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
        self.canvas.create_oval(self.x, self.y, self.x+5, self.y+5, fill="blue")

        self.offset_x = 400
        self.offset_y = 400

        node0 = [0, 100]
        for i in range(360):
            self.rotate_z(1, node0)

    def rotate_z(self, theta, node):
        sin_t = sin(radians(theta))
        cos_t = cos(radians(theta))

        x = node[0]
        y = node[1]

        node[0] = x * cos_t - y * sin_t
        node[1] = y * cos_t + x * sin_t

        self.oval = self.canvas.create_oval(
            self.offset_x+node[0], self.offset_x+node[1], self.offset_x+node[0]+5, self.offset_y+node[1]+5, fill="red"
        )
        time.sleep(0.025)
        self.canvas.update()
        self.canvas.delete('all')


class App(object):
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("tkinter_test01")
        self.root.geometry("{}x{}".format(self.width, self.height))

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        # Create our Rect object:
        self.rect = Rect(self.canvas, 800, 800)
        self.root.mainloop()

if __name__ == "__main__":
    App()
