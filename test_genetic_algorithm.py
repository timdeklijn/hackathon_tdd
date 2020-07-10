from .genetic_algorithm import Population, Individual, GENOME
from .config import POPULATION_SIZE, ANSWER, GENOME_SIZE



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