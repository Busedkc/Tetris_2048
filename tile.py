import lib.stddraw as stddraw  # used for drawing the tiles to display them
from lib.color import Color  # used for coloring the tiles
import random  # used for creating tetrominoes with random types/shapes
import copy as cp
from point import Point

# A class for modeling numbered tiles as in 2048
class Tile:
   # Class variables shared among all Tile objects
   # ---------------------------------------------------------------------------
   # the value of the boundary thickness (for the boxes around the tiles)
   boundary_thickness = 0.004
   # font family and font size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # A constructor that creates a tile with 2 as the number on it
       def __init__(self, position=Point(0, 0)):
        # set the number on this tile
        # self.number = random.randint(2, 4)
        # self.number=2
        initial_list = [2, 4]
        self.number = random.choice(initial_list)
        # set the color of this tile
        self.foreground_color = Color(113, 121, 126)  # foreground (number) color yazının rengi
        self.box_color = Color(158, 138, 120)  # box (boundary) color çerçeve rengi
        self.position = Point(position.x, position.y) # set the position of the tile as the given position

    def double(self):
        self.number *= 2


    def set_position(self, position):
        # set the position of the tile as the given position
        self.position = cp.copy(position)

    # Getter method for the position of the tile
    def get_position(self):
        # return the position of the tile
        return cp.copy(self.position)

    # Method for moving the tile by dx along the x axis and by dy along the y axis
    def move(self, dx, dy):
        self.position.translate(dx, dy)



   # A method for drawing this tile at a given position with a given length
   def draw(self, position, length=1):  # length defaults to 1
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
