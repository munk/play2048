from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep

drv = webdriver.Firefox()
drv.get('http://gabrielecirulli.github.io/2048/')
container = drv.find_element_by_class_name('tile-container')
retry = drv.find_element_by_class_name('retry-button')

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

def move_up():
    container.send_keys(Keys.UP)

def move_down():
    container.send_keys(Keys.DOWN)

def move_left():
    container.send_keys(Keys.LEFT)

def move_right():
    container.send_keys(Keys.RIGHT)

def zero_board():
    global board
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

def update_board():
    global board
    sleep(0.1)
    tiles = container.find_elements_by_class_name('tile')
    tiledata = list(map(lambda x: x.get_attribute('class').split(), tiles))
    zero_board()
    for tile in tiledata:
        value = tile[1].split('-')[1]
        pos = tile[2].split('-')[-2:]
        board[int(pos[1]) - 1][int(pos[0]) - 1] = int(value)
    

def pick_move():
    moves = (move_up, move_down, move_left, move_right)
    return moves[max([randint(0, 3) for _ in range(4)])]

while not retry.is_displayed():
    m = randint(0, 3)
    pick_move()()
    update_board()

sleep(2)
update_board()
for b in board:
    print(b)
sleep(2)
print("Score: ", drv.find_element_by_class_name('score-container').text.splitlines()[0])
print("Game Over")
