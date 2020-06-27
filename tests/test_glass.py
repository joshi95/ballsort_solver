import unittest

from glass import Glass


class TestGlass(unittest.TestCase):
    def test_empty_glass(self):
        glass = Glass()
        self.assertTrue(glass.is_empty())

    def test_push_a_single_ball_will_result_in_non_empty_glass(self):
        glass = Glass()
        glass.push_ball(0)
        self.assertFalse(glass.is_empty())

    def test_raise_exception_when_push_call_on_a_full_glass(self):
        glass = Glass()
        with self.assertRaises(Exception):
            for i in range(0, glass.capacity):
                glass.push_ball(0)
            glass.push_ball(0)

    def test_clone_is_a_hard_copy(self):
        glass = Glass()
        clonedGlass = glass.clone()
        glass.push_ball(1)
        self.assertTrue(clonedGlass.get_size() == 0)
        self.assertTrue(glass.get_size() > 0)

    def test_str_rep(self):
        glass = Glass()
        glass.push_array_of_balls([1, 2, 3])
        self.assertTrue(str(glass), "1,2,3")
