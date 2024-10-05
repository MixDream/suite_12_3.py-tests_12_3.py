# suite_12_3.py
import unittest
from pyton import RunnerTest, TournamentTest

suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
