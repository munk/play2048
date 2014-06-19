from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
import brain
import game

drv = webdriver.Firefox()
drv.get('http://gabrielecirulli.github.io/2048/')
container = drv.find_element_by_class_name('tile-container')
retry = drv.find_element_by_class_name('retry-button')

board = [[None, None, None, None],
         [None, None, None, None],
         [None, None, None, None],
         [None, None, None, None]]

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
    board = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]

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
    global board
    g = game.Game(board)
    predictions = brain.predict_next_board(g)
    scores = []
    for p in predictions[1:]:
        print(p, len(p))
        score = brain.weight_boards(predictions[0], p)
        scores.append(score)
    return brain.choose(scores)

while not retry.is_displayed():
    update_board()
    pick_move()()

sleep(2)
update_board()
for b in board:
    print(b)
sleep(2)
print("Score: ", drv.find_element_by_class_name('score-container').text.splitlines()[0])
print("Game Over")
