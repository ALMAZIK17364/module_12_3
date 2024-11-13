import unittest
import suite_12_3

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break
        return finishers

if __name__ == '__main__':
    import unittest
    import suite_12_3

    sTester = unittest.TestSuite()
    sTester.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))
    sTester.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sTester)