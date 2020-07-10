from .genetic_algorithm import Population, Individual, GENOME
from .config import POPULATION_SIZE, ANSWER, GENOME_SIZE
import random


def test_create_population_class():
    pop = Population()
    assert isinstance(pop, Population)


def test_create_individual_class():
    ind = Individual()
    assert isinstance(ind, Individual)
    assert ind.score != None
    # TODO: test genome init


def test_create_individual_list():
    pop = Population()
    assert type(pop.population) == list
    assert len(pop.population) == POPULATION_SIZE
    # pop = Population(population_size="TIM")


def test_genome():
    assert type(GENOME) == list
    assert "a" in GENOME
    assert "A" in GENOME
    assert "1" in GENOME
    assert " " in GENOME


def test_init_individual():
    ind = Individual()
    assert type(ind.genome) == list
    assert len(ind.genome) == GENOME_SIZE


def test_score_genomes():
    ind = Individual()
    # TODO: write test to check length
    ind.genome = ["X"] * GENOME_SIZE
    score = ind.calculate_score()
    assert score == 0
    ind.genome = ANSWER
    score = ind.calculate_score()
    assert score == 1


def test_choose_parents():
    pop = Population()
    a, b = pop.choose_parents()
    assert isinstance(a, Individual)
    assert isinstance(b, Individual)


def test_reproduction():
    pop = Population()
    a, b = pop.choose_parents()
    new_genome = pop.reproduce(a, b)
    assert type(new_genome) == list
    assert len(new_genome) == GENOME_SIZE
    for i, gene in enumerate(new_genome):
        assert gene == a.genome[i] or gene == b.genome[i]


def test_mutation():
    pop = Population()
    start_genome = [random.choice(GENOME) for _ in range(GENOME_SIZE)]
    new_genome = pop.mutate(start_genome, mutation_rate=1.0)
    assert type(new_genome) == list
    assert len(new_genome) == GENOME_SIZE
    assert new_genome != start_genome
    newer_genome = pop.mutate(start_genome, mutation_rate=0.0)
    assert start_genome == newer_genome


def test_evolution():
    pop = Population()
    init_score = sum([i.score for i in pop.population])
    for _ in range(100):
        pop.evolve()
    final_score = sum([i.score for i in pop.population])
    assert init_score < final_score


def test_best_individual():
    pop = Population()
    pop.population[0].genome = ANSWER
    for ind in pop.population[1:]:
        ind.genome = ["X"] * GENOME_SIZE
    for _ in range(10):
        pop.evolve()
    best, worst = pop.best_individual()
    assert best.score >= worst.score


def test_integration():
    pop = Population()
    for i in range(100):
        pop.evolve()
    best, _ = pop.best_individual()
    assert best.genome == ANSWER
