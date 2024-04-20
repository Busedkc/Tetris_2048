################################################################################
#                                                                              #
# The main program of Tetris 2048 Base Code                                    #
#                                                                              #
################################################################################

import lib.stddraw as stddraw  # for creating an animation with user interactions
from lib.picture import Picture  # used for displaying an image on the game menu
from lib.color import Color  # used for coloring the game menu
import os  # the os module is used for file and directory operations
from game_grid import GameGrid  # the class for modeling the game grid
from tetromino import Tetromino  # the class for modeling the tetrominoes
import random  # used for creating tetrominoes with random types (shapes)

# The main function where this program starts execution
def start():
    # set the dimensions of the game grid
    grid_h, grid_w = 20, 12
    # set the size of the drawing canvas
    canvas_h, canvas_w = 40 * grid_h, 35 * grid_w
    stddraw.setCanvasSize((40 * grid_w) + 120, canvas_h)
    # set the scale of the coordinate system
    stddraw.setXscale(-0.5, grid_w + 5)
    stddraw.setYscale(-0.5, grid_h - 0.5)
    # set the dimension values stored and used in the Tetromino class
    Tetromino.grid_height = grid_h
    Tetromino.grid_width = grid_w
    # create the game grid
    grid = GameGrid(grid_h, grid_w)

    # create the first tetromino to enter the game grid
    # by using the create_tetromino function defined below
    # current_tetromino = create_tetromino(grid_h, grid_w)
    # next_tetromino = create_tetromino(grid_h,grid_w)
    tetro_list1 = create_tetromino(grid_h, grid_w)
    second_tetro_list2 = create_tetromino(grid_h, grid_w)
    newList = [tetro_list1, second_tetro_list2]
    grid.newList = newList
    current_tetromino = newList[0]
    grid.current_tetromino = current_tetromino

    newList.pop(0)

    newList.append(create_tetromino(grid_h, grid_w))

    # display a simple menu before opening the game
    # by using the display_game_menu function defined below
    display_game_menu(grid, grid_h, grid_w + 5.6)

    already_dropped = False
    drop = False

    pause = False
    # main game loop (keyboard interaction for moving the tetromino)
   # the main game loop
   while True:
      # check for any user interaction via the keyboard
      if stddraw.hasNextKeyTyped():  # check if the user has pressed a key
         key_typed = stddraw.nextKeyTyped()  # the most recently pressed key
         # Pause
         if key_typed == 'p':
            print("Pause")
            if pause:
                pause = False
            else:
                pause = True
        # clear the queue of the pressed keys for a smoother interaction
        stddraw.clearKeysTyped()

        if not pause:
            # check user interactions via the keyboard
            if stddraw.hasNextKeyTyped():  # check if the user has pressed a key
                key_typed = stddraw.nextKeyTyped()  # the most recently pressed key
                    
         # if the left arrow key has been pressed
         if key_typed == "left":
            # move the active tetromino left by one
            current_tetromino.move(key_typed, grid)
         # if the right arrow key has been pressed
         elif key_typed == "right":
            # move the active tetromino right by one
            current_tetromino.move(key_typed, grid)
         # if the down arrow key has been pressed
         elif key_typed == "down":
            # move the active tetromino down by one
            # (soft drop: causes the tetromino to fall down faster)
            current_tetromino.move(key_typed, grid)

         elif key_typed == "space":
            # Moves down the tetromino all the way down until it cannot go further
            if not already_dropped:
                while True:
                    sc = current_tetromino.move("down", grid)
                    if not sc:
                        break
                dropped = True

        elif key_typed == "up":
            current_tetromino.rotate_clockwise()


        elif key_typed == "z":
            current_tetromino.rotate_counterclockwise()

            
         # clear the queue of the pressed keys for a smoother interaction
         stddraw.clearKeysTyped()


        if not pause:
            # move the active tetromino down by one at each iteration (auto fall)
            success = current_tetromino.move("down", grid)
            
      # lock the active tetromino onto the grid when it cannot go down anymore
      
        if not success and not pause:
         # get the tile matrix of the tetromino without empty rows and columns
         # and the position of the bottom left cell in this matrix
         tiles, pos = current_tetromino.get_min_bounded_tile_matrix(True)
         # update the game grid by locking the tiles of the landed tetromino
         game_over = grid.update_grid(tiles, pos)
         # end the main game loop if the game is over
         if game_over:
             show_gameOver(grid_w + 4, grid_h - 1.5)
            break
         # create the next tetromino to enter the game grid
         # by using the create_tetromino function defined below
        current_tetromino = newList[1]
            grid.current_tetromino = current_tetromino
            newList.pop(0)
            newList.append(create_tetromino(grid_h, grid_w))

        # display the game grid and the current tetromino
        grid.clear()
        # display the game grid and as well the current tetromino
        grid.display(pause)

    # print a message on the console when the game is over
    print("Game over")

# A function for creating random shaped tetrominoes to enter the game grid
def create_tetromino():
   # the type (shape) of the tetromino is determined randomly
   tetromino_type = ['I', 'O', 'Z','J','T','S','L']
   random_index = random.randint(0, len(tetromino_types) - 1)
   random_type = tetromino_types[random_index]
   # create and return the tetromino
   tetromino = Tetromino(random_type)
   return tetromino


def show_gameOver(grid_height, grid_width):
    # colors used for the menu
    background_color = Color(255, 182, 193)

    # clear the background canvas to background_color
    stddraw.clear(background_color)
    # get the directory in which this python code file is placed
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # path of the image file
    img_file = current_dir + "/images/gameover.png"
    # center coordinates to display the image
    img_center_x, img_center_y = ((grid_width - 1) / 2) - 0.4, grid_height - 6
    # image is represented using the Picture class
    image_to_display = Picture(img_file)
    # center coordinates to display the image
    img_center_x, img_center_y = ((grid_width - 1) / 2) - 0.4, grid_height - 6
    image_to_display = Picture(img_file)
    # display the image
    stddraw.picture(image_to_display, img_center_x, img_center_y)

    while True:
        # display the menu and wait for a short time (50 ms)
        # menüyü görüntüleyin ve kısa bir süre bekleyin (50 ms)
        stddraw.show(50)


# A function for displaying a simple menu before starting the game
def display_game_menu(grid_height, grid_width):
   # the colors used for the menu
   background_color = Color(42, 69, 99)
   button_color = Color(25, 255, 228)
   text_color = Color(31, 160, 239)
   # clear the background drawing canvas to background_color
   stddraw.clear(background_color)
   # get the directory in which this python code file is placed
   current_dir = os.path.dirname(os.path.realpath(__file__))
   # compute the path of the image file
   img_file = current_dir + "/images/menu_image.png"
   # the coordinates to display the image centered horizontally
   img_center_x, img_center_y = (grid_width - 1) / 2, grid_height - 7
   # the image is modeled by using the Picture class
   image_to_display = Picture(img_file)
   # add the image to the drawing canvas
   stddraw.picture(image_to_display, img_center_x, img_center_y)
   # the dimensions for the start game button
   button_w, button_h = grid_width - 1.5, 2
   # the coordinates of the bottom left corner for the start game button
   button_blc_x, button_blc_y = img_center_x - button_w / 2, 4
   # add the start game button as a filled rectangle
   stddraw.setPenColor(button_color)
   stddraw.filledRectangle(button_blc_x, button_blc_y, button_w, button_h)
   # add the text on the start game button
   stddraw.setFontFamily("Arial")
   stddraw.setFontSize(25)
   stddraw.setPenColor(text_color)
   text_to_display = "Click Here to Start the Game"
   stddraw.text(img_center_x, 5, text_to_display)
   # the user interaction loop for the simple menu
   while True:
      # display the menu and wait for a short time (50 ms)
      stddraw.show(50)
      # check if the mouse has been left-clicked on the start game button
      if stddraw.mousePressed():
         # get the coordinates of the most recent location at which the mouse
         # has been left-clicked
         mouse_x, mouse_y = stddraw.mouseX(), stddraw.mouseY()
         # check if these coordinates are inside the button
         if mouse_x >= button_blc_x and mouse_x <= button_blc_x + button_w:
            if mouse_y >= button_blc_y and mouse_y <= button_blc_y + button_h:
               break  # break the loop to end the method and start the game


# start() function is specified as the entry point (main function) from which
# the program starts execution
if __name__ == '__main__':
   start()
