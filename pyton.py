# tests_12_3.py
import unittest
from pypyfile import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False # Установка флага замороженных тестов

    def setUp(self):
        self.runner = Runner("Бегун")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены') # Декоратор для пропуска тестов
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены') # Декоратор для пропуска тестов
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены') # Декоратор для пропуска тестов
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)

class TournamentTest(unittest.TestCase):
    is_frozen = True # Установка флага замороженных тестов

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены') # Декоратор для пропуска тестов
    def test_first_tournament(self):
        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()
        self.assertEqual(results[max(results.keys())], "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены') # Декоратор для пропуска тестов
    def test_second_tournament(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()
        self.assertEqual(results[max(results.keys())], "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены') # Декоратор для пропуска тестов
    def test_third_tournament(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()
        self.assertEqual(results[max(results.keys())], "Ник")
