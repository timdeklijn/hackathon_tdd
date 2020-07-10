import string
import random

from .config import POPULATION_SIZE, ANSWER, GENOME_SIZE

GENOME = list(string.printable)


class Individual:
    def __init__(self):
        self.genome = [random.choice(GENOME) for _ in range(GENOME_SIZE)]
        self.score = self.calculate_score()

    def calculate_score(self):
        # self.genome <-> answer
        score = 0
        for i in range(GENOME_SIZE):
            if self.genome[i] == ANSWER[i]:
                score += 1
        return score / GENOME_SIZE


class Population:
    def __init__(self):
        self.population = [Individual() for _ in range(POPULATION_SIZE)]

    def choose_parents(self):
        parents = random.choices(
            self.population, weights=[i.score for i in self.population], k=2
        )
        return parents[0], parents[1]