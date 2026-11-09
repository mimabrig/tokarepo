import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytyi(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_ei_ole(self):
        player = self.stats.search("Mikki")
        self.assertIsNone(player)

    def test_team_oikea_maara(self):
        tiimi = self.stats.team("EDM")
        self.assertEqual(len(tiimi), 3)

    def test_top_yksi(self):
        paras = self.stats.top(1)
        self.assertEqual(paras[0].name, "Gretzky")