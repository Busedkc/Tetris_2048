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

    def draw(self, position, length=1):  # Draw the tile at the specified position with a given length
        # Assign color based on the tile number
        def assign_color(number):
            color_dict = {
                2: Color(255, 255, 102),  # Light Yellow
                4: Color(255, 204, 102),  # Dark Yellow
                8: Color(255, 153, 102),  # Light Orange
                16: Color(255, 102, 102),  # Dark Orange
                32: Color(255, 51, 102),  # Light Red
                64: Color(204, 51, 153),  # Dark Red
                128: Color(153, 51, 204),  # Light Purple
                256: Color(102, 51, 255),  # Dark Purple
                512: Color(51, 102, 255),  # Light Blue
                1024: Color(51, 153, 255),  # Dark Blue
                2048: Color(0, 102, 255)  # Light Navy
            }
            # Assign black color for numbers larger than 2048
            if number > 2048:
                return Color(0, 0, 0)
            return color_dict.get(number, Color(151, 178, 199))

        # Draw the tile
        stddraw.setPenColor(assign_color(self.number))  # Assign color based on the number
        stddraw.filledSquare(position.x, position.y, length / 2)  # Draw filled square
        stddraw.setPenColor(self.box_color)  # Set pen color for boundary
        stddraw.setPenRadius(Tile.boundary_thickness)  # Set pen radius for boundary
        stddraw.square(position.x, position.y, length / 2)  # Draw boundary square
        stddraw.setPenRadius()  # Reset the pen radius to default value

        # Draw the number
        stddraw.setPenColor(self.foreground_color)  # Set pen color for number
        stddraw.setFontFamily(Tile.font_family)  # Set font family for number
        stddraw.setFontSize(Tile.font_size)  # Set font size for number
        stddraw.text(position.x, position.y, str(self.number))  # Draw number on the tile
