def predict_next_board(game):
    """Returns a list of pos2sible board positions each for left, down, right, up"""
    return [game.board,
            game.move_left(),
            game.move_down(),
            game.move_right(),
            game.move_up()]


def flatten(board):
    return [item for sublist in board for item in sublist]

def score_board(orig, new):
    if orig == new:
        return 999
    flat_orig = flatten(orig)
    flat_new = flatten(new)
    if not max(flat_new in [0, 3, 12, 15]:
        return 100
    if len([f for f in flat_orig if f is not None]) > len([g for g in flat_new if g is not None]):
        return 1
    return 10


def weight_boards(boards):
    """Returns a list of weights associated with each board"""
    orig = boards[0]
    b = boards[1:]
    return map(lambda x: score_board(orig, x), b)

def choose(scores):
    if max(scores) == 0:
        return "left"
    if max(scores) == 1:
        return "down"
    if max(scores) == 2:
        return "right"
    return "up"
