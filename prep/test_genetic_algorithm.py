import copy

import pytest

from .genetic_algorithm import GENOME, N_GENES, Population, Individual
from .config import POPULATION_SIZE, ANSWER, N_GENES


def test_genome():
    """Test if lowercase, uppercase and digits are in the genome"""
    assert "a" in GENOME
    assert "A" in GENOME
    assert "1" in GENOME
    assert " " in GENOME
    assert type(GENOME) == list


def test_random_individual():
    ind = Individual()
    assert len(ind.genome) == N_GENES
    assert type(ind.genome) == list


def test_score_genome():
    ind = Individual()
    ind.genome = ["0"] * N_GENES
    assert ind.score_genome() == 0
    ind.genome = ANSWER
    assert ind.score_genome() == 1.0
    ind.genome = list(ANSWER[:5]) + list("~" * (N_GENES - 5))
    ind.score_genome() == 5 / N_GENES
    ind.genome = list("X")
    with pytest.raises(ValueError, match="Length genome is not N_GENES"):
        ind.score_genome()


def test_create_population():
    """Test the full genetic algorithm"""
    pop = Population()
    assert len(pop.population) == POPULATION_SIZE
    assert isinstance(pop.population[0], Individual)


def test_mix_genomes():
    pop = Population()
    g1 = list("abcd")
    g2 = list("efgh")
    new_genome = pop.mix_genomes(g1, g2)
    assert len(new_genome) == len(g1)
    assert type(new_genome) == list
    g3 = list("a")
    with pytest.raises(ValueError, match="Length g1 is not length g2"):
        pop.mix_genomes(g1, g3)


def test_mutate_genome():
    pop = Population()
    test_genome = "abcdefg"
    g1 = list(test_genome)
    new_genome = pop.mutate_genome(g1, mutation_rate=1.0)
    assert len(new_genome) == len(g1)
    assert type(new_genome) == list
    assert list(test_genome) != new_genome


def test_next_generation():
    pop = Population()
    tmp_pop = copy.deepcopy(pop.population)
    pop.next_generation()
    assert [i.genome for i in tmp_pop] != [i.genome for i in pop.population]


def test_score_is_greater():
    pop = Population()
    initial_score = sum([i.score for i in pop.population])
    for _ in range(100):
        pop.next_generation()
    new_score = sum([i.score for i in pop.population])
    assert new_score > initial_score


def test_evolve_population():
    pop = Population()
    pop.evolve_population(5000)
    best_answer = pop.find_best_genome()
    assert best_answer == ANSWER
