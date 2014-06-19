from game import Game, merge
import brain
from nose.tools import *

def test_merge_dups_nones():
    lst = [None, None, None, None]
    result = merge(lst)
    assert lst == result, result

def test_merge_dups_no_dupes():
    lst = [2, 4, 8, 16]
    assert lst == merge(lst)

def test_merge_dups_dupes_start():
    lst = [2, 2, 8, 16]
    assert [4, 8, 16, None] == merge(lst)

def test_merge_dups_dupes_middle():
    lst = [2, 8, 8, 16]
    assert [2, 16, 16, None] == merge(lst)

def test_merge_dups_dupes_end():
    lst = [2, 8, 16, 16]
    assert [2, 8, 32, None] == merge(lst)

def test_merge_two_dups():
    lst = [2, 2, 2, 2]
    result = merge(lst)
    assert [4, 4, None, None] == result, result

def test_merge_two_dups_different():
    lst = [2, 2, 4, 4]
    assert [4, 8, None, None] == merge(lst)

def test_move_left():
    g = Game()
    g.board = [[2, 2, 2, 2],
               [None, 8, 8, 4],
               [8, 16, 16, 64],
               [None, None, 2, 4]]

    expected = [[4, 4, None, None],
               [16, 4, None, None],
               [8, 32, 64, None],
               [2, 4, None, None]]
                
    g.move_left()
    assert_equals(g.board, expected)

def test_moves_show_correct_size():
    board = [[None, 2, None, None], [None, None, 2, None], [None, None, None, None], [None, None, None, None]]
    g = Game(board)
    predictions = brain.predict_next_board(g)
    assert len(predictions) == 5, predictions
