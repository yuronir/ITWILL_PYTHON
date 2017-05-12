from tkinter import *
import random

class Ball():
    def __init__(self, canvas):
        self.canvas = canvas
        self.speed = 5
        self.angle = random.randint()