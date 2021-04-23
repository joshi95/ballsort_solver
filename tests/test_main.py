import unittest

from core.solver.board import Board
from core.solver.glass import Glass
from core.solver.solver import solver


class TestMain(unittest.TestCase):

    @staticmethod
    def try_to_solve(board):
        res = solver(board)
        if res["isSolvable"]:
            print("Solvable")
            moves = res["moves"]
            for move in moves:
                print(str(move._from) + " " + str(move._to))
            return True
        else:
            return False

    def test_can_create_multiple_glass(self):
        board = Board([
            Glass.create_glass([2, 1, 1, 1]),
            Glass.create_glass([2, 2, 2]),
            Glass.create_glass([1]),
            Glass.create_glass([])
        ])
        self.try_to_solve(board)

    def test_solve_complex_board(self):
        board = Board([
            Glass.create_glass([0, 1, 0, 2]),
            Glass.create_glass([1, 3, 4, 2]),
            Glass.create_glass([5, 6, 4, 4]),
            Glass.create_glass([7, 6, 3, 6]),
            Glass.create_glass([8, 5, 7, 7]),
            Glass.create_glass([0, 5, 5, 1]),
            Glass.create_glass([3, 3, 2, 0]),
            Glass.create_glass([4, 6, 8, 8]),
            Glass.create_glass([7, 2, 8, 1]),
            Glass.create_glass([]),
            Glass.create_glass([]),
        ])
        self.assertTrue(self.try_to_solve(board))

    def test_runs_correctly_for_wrong_board(self):
        board = Board([
            Glass.create_glass([2, 2, 1, 1]),
            Glass.create_glass([3]),
            Glass.create_glass([4]),
            Glass.create_glass([5]),
        ])
        self.assertFalse(self.try_to_solve(board))