import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_top_scorers_found(self):
        sorted = self.statistics.top_scorers(2)
        tops = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]
        self.assertIsInstance(sorted, list)
        self.assertEqual(sorted[0].name, tops[0].name)
        self.assertEqual(sorted[2].name, tops[2].name)
        
    
    def test_search_by_wrong_team_name_returns_emptylist(self):
        self.assertEqual(self.statistics.team("Keijo"), list())

    def test_search_by_team_returns_all_team_players(self):
        self.assertEqual(self.statistics.team("EDM"), [\
            Player("Semenko", "EDM", 4, 12),\
            Player("Kurri", "EDM", 37, 53),\
            Player("Gretzky", "EDM", 35, 89)])

    def test_search_finds_correct_player(self):
        self.assertEqual(self.statistics.search("Semenko").name,"Semenko" )
    
    def test_search_returns_none_if_player_not_found(self):
        self.assertEqual(self.statistics.search("Luupää"), None)
    
    