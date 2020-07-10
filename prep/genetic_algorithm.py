import string
import random

from .config import POPULATION_SIZE, ANSWER, N_GENES, MUTATION_RATE

GENOME = list(string.printable)


class Individual:
    def __init__(self):
        self.genome = self.init_genome()
        self.score = self.score_genome()

    def init_genome(self):
        return random.choices(GENOME, k=N_GENES)

    def score_genome(self):
        if len(self.genome) != N_GENES:
            raise ValueError("Length genome is not N_GENES")
        score = 0
        for i in range(N_GENES):
            if self.genome[i] == ANSWER[i]:
                score += 1
        return score / N_GENES

    def set_new_score(self):
        self.score = self.score_genome()


class Population:
    def __init__(self):
        # A list of randomly initialized individuals
        self.population = [Individual() for _ in range(POPULATION_SIZE)]

    def next_generation(self):
        new_genomes = []
        score_list = [i.score for i in self.population]
        for _ in range(POPULATION_SIZE):
            while True:
                parents = random.choices(self.population, weights=score_list, k=2)
                if parents[0] != parents[1]:
                    break
            new_genomes.append(
                self.mutate_genome(
                    self.mix_genomes(parents[0].genome, parents[1].genome),
                    mutation_rate=MUTATION_RATE,
                ),
            )
        for i, genome in enumerate(new_genomes):
            self.population[i].genome = genome
            self.population[i].set_new_score()

    def mix_genomes(self, g1, g2):
        if len(g1) != len(g2):
            raise ValueError("Length g1 is not length g2")
        new_genome = []
        for i in range(len(g1)):
            new_genome.append(random.choice([g1[i], g2[i]]))
        return new_genome

    def mutate_genome(self, genome, mutation_rate=0.02):
        for i in range(len(genome)):
            if random.random() < mutation_rate:
                genome[i] = random.choice(GENOME)
        return genome

    def evolve_population(self, generations=1000):
        for _ in range(generations):
            self.next_generation()

    def find_best_genome(self):
        min_score = self.population[0].score
        best_genome = self.population[0].genome
        for i in self.population[1:]:
            if i.score > min_score:
                min_score = i.score
                best_genome = i.genome
        return best_genome
