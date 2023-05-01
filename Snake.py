from tkinter import *
import random

#Initializing variables
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
  
class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        #want snake's body parts to start at (0,0)
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        
        #Creates snake's initial body parts
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag= "snake")
            self.squares.append(square)
            
        
class Food:
    
    def __init__(self):
        
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        
        self.coordinates = [x,y]
        
        canvas.create_oval(x,y, x+SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag="food")

        

def next_turn(snake, food):
    
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE   
    elif direction == "down":
        y += SPACE_SIZE 
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    snake.coordinates.insert(0, (x,y))
    
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    
    snake.squares.insert(0, square)
    
    #if snake meets food object
    if x == food.coordinates[0] and y==food.coordinates[1]:
        
        global score
        
        score +=1
        
        label.config(text = "Score: {}".format(score))
        canvas.delete("food")
        
        food = Food()
    
    else:
    
        del snake.coordinates[-1]
        
        canvas.delete(snake.squares[-1])
        
        del snake.squares[-1]
    
    if check_collision(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

      

def change_direction(new_direction):

    global direction
    
    if new_direction == 'left':
        if direction !='right':
            direction = new_direction
    
    elif new_direction == 'right':
        if direction !='left':
            direction = new_direction
    elif new_direction == 'up':
        if direction !='down':
            direction = new_direction
    elif new_direction == 'down':
        if direction !='up':
            direction = new_direction 

def check_collision(snake):
    
    x, y = snake.coordinates[0]
    
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False
        
    

def game_over():
    
    canvas.delete(ALL)
    
    #prints out "Game Over" when snake collides
    canvas.create_text(canvas.winfo_width()/2, (canvas.winfo_height()/2)-100, font=('consolas',50), text="GAME OVER", fill="red", tag="gameover")

    #prints out restart and exit buttons when game is over
    button_frame = Frame(canvas, bg=BACKGROUND_COLOR)
    
    restart_button = Button(button_frame, height = 2, width= 10,text="Play Again", font=('consolas', 20), command=start_game, fg="green")
    exit_button = Button(button_frame, height = 2, width= 10, text="Exit Game", font=('consolas', 20), command=exit_game,fg = "red")
    
    
    restart_button.pack(side= "top")
    exit_button.pack(side= "top", pady=20)

    canvas.create_window(canvas.winfo_width()/2, ((canvas.winfo_height()/2)+40), window=button_frame)
    

#exits program
def exit_game():
    exit()

#function to start the game
def start_game():
    
    global score, direction, canvas, window, label
    window = Tk()
    window.title("Snake Game")
    window.resizable(False, False)

    score = 0
    direction = 'down'

    #sets score properties
    label = Label(window, text = "Score: {}".format(score), font= ('consolas', 40))
    label.pack()
    
    #sets canvas dimensions
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
    canvas.pack()
    
    window.update()

    #centers pop-up to middle of screen
    window_width = window.winfo_width() #window refers to the pop-up window
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth() #screen width & height refers to dimensions of computer screen
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    #bindings keys for movement
    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))
    
    window.bind("<a>", lambda event: change_direction('left'))
    window.bind("<d>", lambda event: change_direction('right'))
    window.bind("<w>", lambda event: change_direction('up'))
    window.bind("<s>", lambda event: change_direction('down'))


    #Calling Classes & Functions
    snake = Snake()
    food = Food()

    next_turn(snake, food)

    window.mainloop()

#Starts Game
start_game()
