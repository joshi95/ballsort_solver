import unittest

from core.solver.move import Move


class TestMove(unittest.TestCase):

    def test_constructor_sets_correct_value(self):
        move = Move(1, 2)
        self.assertTrue(move._from == 1)
        self.assertTrue(move._to == 2)

    def test_invert_function(self):
        move = Move(1, 2)
        invert_move = move.invert()
        self.assertTrue(move._from == invert_move._to)
        self.assertTrue(move._to == invert_move._from)
