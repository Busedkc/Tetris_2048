import lib.stddraw as stddraw  # used for displaying the game grid
from lib.color import Color  # used for coloring the game grid
from point import Point  # used for tile positions
import numpy as np  # fundamental Python module for scientific computing
import random
from tetromino import Tetromino

# A class for modeling the game grid
class GameGrid:
   # A constructor for creating the game grid based on the given arguments
   def __init__(self, grid_h, grid_w):
      # set the dimensions of the game grid as the given arguments
      self.grid_height = grid_h
      self.grid_width = grid_w
      # create a tile matrix to store the tiles locked on the game grid
      self.tile_matrix = np.full((grid_h, grid_w), None)
      # create the tetromino that is currently being moved on the game grid
      self.current_tetromino = None

      self.next_tetromino = None
      self.newList = None
      
      # the game_over flag shows whether the game is over or not
      self.game_over = False
      # set the color used for the empty grid cells
      self.empty_cell_color = Color(255, 182, 193)
      # set the colors used for the grid lines and the grid boundaries
      self.line_color = Color(128, 128, 0)
      self.boundary_color = Color(255, 165, 0)
      # thickness values used for the grid lines and the boundaries
      self.line_thickness = 0.002
      self.box_thickness = 7 * self.line_thickness
      # score
      self.score = 0
      # Check reached 2046 to win
      self.reached2048 = False
      # to show next tetrominos

      self.speed = 250
   # A method for displaying the game grid
   def display(self, pause):
      # clear the background to empty_cell_color
      stddraw.clear(self.empty_cell_color)
      # draw the game grid
      self.draw_grid()
      # draw the current/active tetromino if it is not None
      # (the case when the game grid is updated)
      if self.current_tetromino is not None:
         self.current_tetromino.draw()
      # draw a box around the game grid
      self.draw_boundaries()
      self.shownextTetromino(self.newList)
      # draw a box around the game grid
      self.draw_boundaries()
      # show the resulting drawing with a pause duration = 250 ms
      stddraw.show(self.speed)

      if (pause):
         stddraw.setPenColor(stddraw.BLACK)
         stddraw.setFontSize(32)
         stddraw.text(self.grid_width / 2, self.grid_height / 2, "Game is paused")
        # show the resulting drawing with a pause duration = 1550 ms
      stddraw.show(self.speed)

   def slower(self):
      self.speed = self.speed * 1.5

   def faster(self):
      self.speed = self.speed / 4

   def shownextTetromino(self, list):
      stddraw.setPenColor(stddraw.BLACK)
      list[1].show_next_tetromino()


    # Method for drawing the cells and the lines of the game grid
    def draw_grid(self):
        # for each cell of the game grid
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                # draw the tile if the grid cell is occupied by a tile
                if self.tile_matrix[row][col] is not None:
                    self.tile_matrix[row][col].draw(Point(col, row))
        # draw the inner lines of the grid
        stddraw.setPenColor(self.line_color)
        stddraw.setPenRadius(self.line_thickness)
        # x and y ranges for the game grid
        start_x, end_x = -0.5, self.grid_width - 0.5
        start_y, end_y = -0.5, self.grid_height - 0.5
        for x in np.arange(start_x + 1, end_x, 1):  # vertical inner lines
            stddraw.line(x, start_y, x, end_y)
        for y in np.arange(start_y + 1, end_y, 1):  # horizontal inner lines
            stddraw.line(start_x, y, end_x, y)
        stddraw.setPenRadius()  # reset the pen radius to its default value

        stddraw.setPenColor(self.empty_cell_color)
        stddraw.filledRectangle(13.5, 3, 5, 4)

        # SCORE
        stddraw.setFontFamily("Times New Roman")
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 1.5, "SCORE")
        stddraw.boldText(self.grid_width + 2.45, self.grid_height - 2.5, str(self.score))

        # Controls
        stddraw.setFontFamily("Times New Roman")
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.DARK_GRAY)
        stddraw.boldText(self.grid_width + 2.4, self.grid_height - 7.8, "MOVEMENTS")

        stddraw.setFontFamily("Times New Roman")
        stddraw.setFontSize(10)
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 8.5, "Press ← to left on")
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 9, "Press → to right on")
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 11, "Space to drop tetromino")
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 9.5, "P to Pause")
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 10, "Press ↑ to Rotate (Clockwise)")
        stddraw.boldText(self.grid_width + 2.3, self.grid_height - 10.5, "Z to Rotate (Anti-Clockwise)")

        stddraw.setFontFamily("Times New Roman")
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.boldText(self.grid_width + 2, self.grid_height - 14.5, "NEXT")

   # A method for drawing the boundaries around the game grid
   def draw_boundaries(self):
      # draw a bounding box around the game grid as a rectangle
      stddraw.setPenColor(self.boundary_color)  # using boundary_color
      # set the pen radius as box_thickness (half of this thickness is visible
      # for the bounding box as its lines lie on the boundaries of the canvas)
      stddraw.setPenRadius(self.box_thickness)
      # the coordinates of the bottom left corner of the game grid
      pos_x, pos_y = -0.5, -0.5
      stddraw.rectangle(pos_x, pos_y, self.grid_width, self.grid_height)
      stddraw.setPenRadius()  # reset the pen radius to its default value

   # A method used checking whether the grid cell with the given row and column
   # indexes is occupied by a tile or not (i.e., empty)
   def is_occupied(self, row, col):
      # considering the newly entered tetrominoes to the game grid that may
      # have tiles with position.y >= grid_height
      if not self.is_inside(row, col):
         return False  # the cell is not occupied as it is outside the grid
      # the cell is occupied by a tile if it is not None
      return self.tile_matrix[row][col] is not None

   # A method for checking whether the cell with the given row and col indexes
   # is inside the game grid or not
   def is_inside(self, row, col):
      if row < 0 or row >= self.grid_height:
         return False
      if col < 0 or col >= self.grid_width:
         return False
      return True

   # A method that locks the tiles of a landed tetromino on the grid checking
   # if the game is over due to having any tile above the topmost grid row.
   # (This method returns True when the game is over and False otherwise.)
   def update_grid(self, tiles_to_lock, blc_position):
      # necessary for the display method to stop displaying the tetromino
      self.current_tetromino = None
      # lock the tiles of the current tetromino (tiles_to_lock) on the grid
      n_rows, n_cols = len(tiles_to_lock), len(tiles_to_lock[0])
      for col in range(n_cols):
         for row in range(n_rows):
            # place each tile (occupied cell) onto the game grid
            if tiles_to_lock[row][col] is not None:
               # compute the position of the tile on the game grid
               pos = Point()
               pos.x = blc_position.x + col
               pos.y = blc_position.y + (n_rows - 1) - row
               if self.is_inside(pos.y, pos.x):
                  self.tile_matrix[pos.y][pos.x] = tiles_to_lock[row][col]
               # the game is over if any placed tile is above the game grid
               else:
                  self.game_over = True
      self.merge()
      self.check_grid()
      
      # return the value of the game_over flag
      return self.game_over

    def check_grid(self):
        for row in range(self.grid_width):
            if None not in self.tile_matrix[row]:
                self.delete_row(row)
                self.move_row(row)
                self.check_grid()

    def clear(self):
        empty_rows = [i for i, row in enumerate(self.tile_matrix) if None not in row]
        self.tile_matrix = np.delete(self.tile_matrix, empty_rows, axis=0)
        for _ in empty_rows:
            self.tile_matrix = np.append(self.tile_matrix, np.full((1, self.grid_width), None), axis=0)

   
