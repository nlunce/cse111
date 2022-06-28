import tkinter as tk
import random

# Initializing constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 80
SPACE_SIZE = 10
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

gl_direction = 'down'
gl_score = 0


def main():

    global window
    global canvas
    global score_label
    

    window = tk.Tk()
    window.title('Snake')
    window.resizable(False, False)

    
    

    score_label = tk.Label(window, text='Score:{}'.format(gl_score), font=('consolas', 40))
    score_label.pack()

    canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

   

    snake = Snake()
    food = Food()

    next_turn(snake, food)


    window.mainloop()

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        
        x = random.randint(0, ( GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, ( GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if gl_direction == 'up':
        y -= SPACE_SIZE
    elif gl_direction == 'down':
        y += SPACE_SIZE
    elif gl_direction == 'left':
        x -= SPACE_SIZE
    elif gl_direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)


    # If the snakes head overlaps the same coordintes of the food then its
    # last square is not deleted yielding a plus one effect
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global gl_score

        gl_score += 1

        score_label.config(text='Score:{}'.format(gl_score))

        canvas.delete('food')

        food = Food()
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    
    if check_collisions(snake):
        game_over()
    else:     
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global gl_direction

    if new_direction == 'left':
        if gl_direction != 'right':
            gl_direction = new_direction
    elif new_direction == 'right':
        if gl_direction != 'left':
            gl_direction = new_direction
    elif new_direction == 'up':
        if gl_direction != 'down':
            gl_direction = new_direction
    elif new_direction == 'down':
        if gl_direction != 'up':
            gl_direction = new_direction
    return gl_direction

def check_collisions(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print('GAME OVER')
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print('GAME OVER')
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print('GAME OVER')
            return True
    
    return False

def game_over():
    
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='GAME OVER', fill='red', tag='gameover')
    
    
if __name__ == "__main__":
    main()