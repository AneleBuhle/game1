import unittest
import sys
import game


class Game_TestCase(unittest.TestCase):

    def test_win(self):

        game.player_score = 2
        game.computer_score = 1

        results = game.score()
        self.assertEqual("You are the Overall Winner!", results)
