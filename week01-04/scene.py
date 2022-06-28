# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from curses import can_change_color
from curses.panel import top_panel
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    ground_height = 100

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, ground_height)
    draw_clouds(canvas)
    draw_mountains(canvas, 200, 100, 350, 250, 500, 100 )
    
    for x in range(0, 900, 20):
        draw_tree(canvas, x, 100, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, width, height):
    draw_rectangle(canvas, 0, 0, width, height, width=1, fill="dodgerBlue1")


def draw_ground(canvas, width, height):
    draw_rectangle(canvas, 0, 0, width, height, width=1, outline='', fill="saddleBrown")

def draw_clouds(canvas):
    draw_oval(canvas, 0, 300, 250, 450, outline='gray95', fill="gray95")
    draw_oval(canvas, 175, 400, 400, 500, outline='gray95', fill="gray95")
    draw_oval(canvas, 225, 350, 600, 410    , outline='gray95', fill="gray95")
    draw_oval(canvas, 100, 350, 400, 410    , outline='gray95', fill="gray95")
    draw_oval(canvas, 250, 400, 550, 500    , outline='gray95', fill="gray95")

def draw_tree(canvas, trunk_center_x, trunk_center_y, tree_height):
    trunk_bottom_left_x = trunk_center_x - (tree_height/10)
    trunk_bottom_left_y = trunk_center_y
    trunk_top_right_x = trunk_center_x + (tree_height/10)
    trunk_top_right_y = trunk_center_y + (tree_height/6)
    draw_rectangle(canvas,trunk_bottom_left_x, trunk_bottom_left_y, trunk_top_right_x, trunk_top_right_y, outline='', fill='tan4')
    leaves_top_x = trunk_center_x
    leaves_top_y = trunk_center_y + tree_height
    leaves_left_x = leaves_top_x - (tree_height/3)
    leaves_left_y = leaves_top_y - (tree_height - (trunk_top_right_y - trunk_bottom_left_y))
    leaves_right_x = leaves_top_x + (tree_height/3)
    leaves_right_y = leaves_top_y - (tree_height - (trunk_top_right_y - trunk_bottom_left_y))
    draw_polygon(canvas, leaves_left_x, leaves_left_y, leaves_top_x, leaves_top_y, leaves_right_x, leaves_right_y, outline='', fill='forestGreen')



def draw_mountains(canvas, left_x, left_y, top_x, top_y, right_x, right_y):
    draw_polygon(canvas, left_x, left_y, top_x, top_y, right_x, right_y, outline='', fill='gray54')
    snow_left_x = top_x - 50
    snow_left_y = top_y - 50
    snow_right_x = top_x + 50
    snow_right_y = top_y - 50
    snow_top_x = top_x
    snow_top_y = top_y
    draw_polygon(canvas, snow_left_x, snow_left_y, snow_top_x, snow_top_y, snow_right_x, snow_right_y, outline='', fill='snow1')




    



# Call the main function so that
# this program will start executing.
main()