import unittest
import tests_12_3 as cl

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Установлено в True, как указано в задании

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = cl.Runner("Усэйн", 10)
        self.runner2 = cl.Runner("Андрей", 9)
        self.runner3 = cl.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print({place: runner.name for place, runner in result.items()})

    def skip_if_frozen(self):
        if self.__class__.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")

    def test_race_runner1_and_runner3(self):
        self.skip_if_frozen()
        tournament = cl.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        self.all_results.append(results)
        self.assertTrue(results[1] == self.runner1)
        self.assertTrue(results[2] == self.runner3)

    def test_race_runner2_and_runner3(self):
        self.skip_if_frozen()
        tournament = cl.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results.append(results)
        self.assertTrue(results[1] == self.runner2)
        self.assertTrue(results[2] == self.runner3)

    def test_race_runner1_runner2_and_runner3(self):
        self.skip_if_frozen()
        tournament = cl.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results.append(results)
        self.assertTrue(results[1] in [self.runner1, self.runner2])
        self.assertTrue(results[2] in [self.runner1, self.runner2])
        self.assertTrue(results[3] == self.runner3)

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Установлено в False, как указано в задании

    def skip_if_frozen(self):
        if self.__class__.is_frozen:
            self.skip