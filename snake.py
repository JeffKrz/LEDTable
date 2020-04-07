from pixellib import pixel, show
import config
import time
import random


class Cords(object):
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

direction = "r"
SNAKECOLOR = "blue"
gameover = False

def gameOverAnimation():
    for i in range (0,5):
        for x in range(0,config.NUM_ROWS):
            for y in range(0,config.NUM_COLLS):
                pixel(x, y, "red")
        show()
        time.sleep(0.1)
        for x in range(0,config.NUM_ROWS):
            for y in range(0,config.NUM_COLLS):
                pixel(x, y, "off")
        show()
        time.sleep(0.1)

def checkGameOver():
    #check for game over
    for i in range(1,len(snake)-1):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            gameOverAnimation()
            return True
    return False

def snakepixelOn():
    #turn on each segment of the snake except for the last one (old tail position)
    for i in range(0,len(snake)-1):
        pixel(int(snake[i].x),int(snake[i].y),SNAKECOLOR)
    show()

def checkFood():
    #if snake head position is equal to food position, insert food position into snake list
    if snake[0].x == food.x and snake[0].y == food.y:
        snake.insert(len(snake)-2, Cords(int(food.x), int(food.y)))
#       print("found food, current snake length:" + str(len(snake)-1))
        #turn off old food
        pixel(food.x, food.y, "off")
        #find new position for food that is not in snake
        while True:
            inSnake = False
            food.x = random.randint(0, config.NUM_COLLS - 1)
            food.y = random.randint(0, config.NUM_ROWS - 1)
            for obj in snake:
                if obj.x == food.x and obj.y == food.y:
                    inSnake = True
            if not inSnake:
                break
        pixel(int(food.x), int(food.y), "green")
        show()

def forwardInDirection():
    if direction == "u":
        if snake[0].y < config.NUM_ROWS - 1 :
            snake[0].y = snake[0].y + 1
        else:
            snake[0].y = 0

    if direction == "l":
        if snake[0].x > 0:
            snake[0].x = snake[0].x - 1
        else:
            snake[0].x = config.NUM_COLLS - 1

    if direction == "d":
        if snake[0].y > 0:
            snake[0].y = snake[0].y - 1
        else:
            snake[0].y = config.NUM_ROWS

    if direction == "r":
        if snake[0].x < config.NUM_COLLS - 1:
            snake[0].x = snake[0].x + 1
        else:
            snake[0].x = 0

def shiftSnake():
    #shifting each snake element to the back by one
    for i in range(len(snake)-1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y
    # turning off the last pixel of snake
    pixel(int(snake[len(snake) - 1].x), int(snake[len(snake) - 1].y), "off")




#initialize food
food = Cords
food.x = random.randint(0,config.NUM_COLLS-1)
food.y = random.randint(0,config.NUM_ROWS-1)
pixel(int(food.x), int(food.y), "green")
show()

#initialize snake
snake = []
snake.append(Cords(config.NUM_COLLS/2, config.NUM_ROWS/2))
snake.append(Cords(config.NUM_COLLS/2-1, config.NUM_ROWS/2)) #aus pixel

#main
while not gameover:

    f = open("direction.txt", "r")
    direction = str(f.read(1))
    f.close()

    snakepixelOn()
    time.sleep(0.5)
    gameover = checkGameOver()
    checkFood()
    shiftSnake()
    forwardInDirection()