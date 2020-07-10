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

    def reproduce(self, a, b):
        new_genome = []
        for i in range(GENOME_SIZE):
            if random.random() < 0.5:
                new_genome.append(a.genome[i])
            else:
                new_genome.append(b.genome[i])
        return new_genome

    def mutate(self, genome, mutation_rate):
        new_genome = []
        for i in range(GENOME_SIZE):
            if random.random() < mutation_rate:
                new_genome.append(random.choice(GENOME))
            else:
                new_genome.append(genome[i])
        return new_genome