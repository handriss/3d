from tkinter import *
from math import *
import time


class Rect(object):
    def __init__(self, canvas, width, height):
        self.canvas = canvas

        center = [400, 400]
        node0 = [100, 100]
        node1 = [-100, 100]
        node2 = [-100, -100]
        node3 = [100, -100]
        nodes = [node0, node1, node2, node3]

        vertices = []
        edges = []
        for node in nodes:
            vertices.append(self.draw_circle(center[0]+node[0], center[1]+node[1], 5, fill="red"))

        for i in range(len(nodes)):
            edges.append(self.canvas.create_line(
                nodes[i][0]+center[0], nodes[i][1]+center[1],
                nodes[i-1][0]+center[0], nodes[i-1][1]+center[1], fill="black"
            ))

        self.coords = []
        for i in range(360):
            time.sleep(0.025)

            for node, vortex in zip(nodes, vertices):
                shift_x, shift_y = self.rotate_z(1, node)
                self.canvas.move(vortex, shift_x, shift_y)
                self.canvas.update()

    def draw_circle(self, x, y, size, **kwargs):
        return self.canvas.create_oval(x-size/2, y-size/2, x+size/2, y+size/2, **kwargs)

    def rotate_z(self, theta, node):
        x_temp = node[0]
        y_temp = node[1]
        x = node[0]
        y = node[1]

        node[0] = x * cos(radians(theta)) - y * sin(radians(theta))
        node[1] = y * cos(radians(theta)) + x * sin(radians(theta))

        return -(x_temp - node[0]), -(y_temp - node[1])


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
