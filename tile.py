import lib.stddraw as stddraw  # stddraw is used as a basic graphics library
from lib.color import Color  # used for coloring the tile and the number on it
import random  # used for creating tetrominoes with random types/shapes
import copy as cp
from point import Point
from random import randint


# Class used for modeling numbered tiles as in 2048
class Tile:
    # Class attributes shared among all Tile objects
    # ---------------------------------------------------------------------------
    # the value of the boundary thickness (for the boxes around the tiles)
    boundary_thickness = 0.001
    # font family and size used for displaying the tile number
    font_family, font_size = "Arial", 14

    # Constructor that creates a tile with 2 as the number on it
    def __init__(self, position=Point(0, 0)):
        # set the number on the tile as 2 and 4
        # self.number = random.randint(2, 4)
        # self.number=2
        my_list = [2, 4]
        self.number = random.choice(my_list)
        # assign the number on the tile

        self.foreground_color = Color(113, 121, 126)  # foreground (number) color yazının rengi
        self.box_color = Color(158, 138, 120)  # box (boundary) color çerçeve rengi
        # set the position of the tile as the given position
        self.position = Point(position.x, position.y)

    def set_position(self, position):
        # set the position of the tile as the given position
        self.position = cp.copy(position)

        # Getter method for the position of the tile

    def get_position(self):
        # return the position of the tile
        return cp.copy(self.position)

    def double(self):
        self.number *= 2

    # Method for moving the tile by dx along the x axis and by dy along the y axis
    def move(self, dx, dy):
        self.position.translate(dx, dy)

    # Method for drawing the tile
    def draw(self, position, length=1):
        # draw the tile as a filled square
        if (self.number == 2):
            self.background_color = Color(238, 228, 218)  # background (tile) color
        if (self.number == 4):
            self.background_color = Color(237, 224, 200)  # background (tile) color
        if (self.number == 8):
            self.background_color = Color(242, 177, 121)  # background (tile) color
        if (self.number == 16):
            self.background_color = Color(245, 149, 99)  # background (tile) color
        if (self.number == 32):
            self.background_color = Color(246, 124, 95)  # background (tile) color
        if (self.number == 64):
            self.background_color = Color(246, 94, 59)  # background (tile) color
        if (self.number == 128):
            self.background_color = Color(237, 207, 114)  # background (tile) color
        if (self.number == 256):
            self.background_color = Color(237, 204, 97)  # background (tile) color
        if (self.number == 512):
            self.background_color = Color(237, 200, 80)  # background (tile) color
        if (self.number == 1024):
            self.background_color = Color(237, 197, 63)  # background (tile) color
        if (self.number == 2048):
            self.background_color = Color(237, 194, 46)  # background (tile) color
        # used proper colors until 2048
        # used remainder in order to get a proper color for every number
        # with this the value will never exceed 255 however better solution may be proposed
        if (self.number > 2048):
            self.background_color = Color((self.number % 255), (self.number % 20), (self.number % 255))

        # draw the tile as a filled square
        stddraw.setPenColor(self.background_color)
        stddraw.filledSquare(position.x, position.y, length / 2)
        # draw the bounding box around the tile as a square
        stddraw.setPenColor(self.box_color)
        stddraw.setPenRadius(Tile.boundary_thickness)
        stddraw.square(position.x, position.y, length / 2)
        stddraw.setPenRadius()  # reset the pen radius to its default value
        # draw the number on the tile
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(Tile.font_size)
        stddraw.text(position.x, position.y, str(self.number))


