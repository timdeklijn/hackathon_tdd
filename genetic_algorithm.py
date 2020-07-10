import string
import random

from .config import POPULATION_SIZE, ANSWER, GENOME_SIZE, MUTATION_RATE

GENOME = list(string.printable)


class Individual:
    def __init__(self, genome=None):
        if genome == None:
            self.genome = [random.choice(GENOME) for _ in range(GENOME_SIZE)]
        else:
            self.genome = genome
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

    def evolve(self):
        new_population = []
        for _ in range(POPULATION_SIZE):
            mom, dad = self.choose_parents()
            baby_genome = self.reproduce(mom, dad)
            baby = Individual(baby_genome)
            new_population.append(baby)
        self.population = new_population

    def best_individual(self):
        best_score = -1000
        best_individual = None
        worst_score = 1000
        worst_individual = None
        for i in self.population:
            if i.score > best_score:
                best_score = i.score
                best_individual = i
            if i.score < worst_score:
                worst_score = i.score
                worst_individual = i
        return best_individual, worst_individual