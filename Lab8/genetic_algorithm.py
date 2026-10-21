import random


def bit_string(value, length):
    return format(value, f'0{length}b')


def fitness(chromosome):
    value = int(chromosome, 2)
    return value * value


def initialize_population(size, length):
    return [''.join(random.choice('01') for _ in range(length)) for _ in range(size)]


def select_parent(population):
    total = sum(fitness(chromosome) for chromosome in population)
    if total == 0:
        return random.choice(population)

    pick = random.uniform(0, total)
    current = 0
    for chromosome in population:
        current += fitness(chromosome)
        if current >= pick:
            return chromosome
    return population[-1]


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutate(chromosome, mutation_rate):
    mutated = list(chromosome)
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = '1' if mutated[i] == '0' else '0'
    return ''.join(mutated)


def genetic_algorithm(population_size=10, chromosome_length=8, generations=20, mutation_rate=0.05):
    population = initialize_population(population_size, chromosome_length)

    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            if len(new_population) < population_size:
                new_population.append(mutate(child2, mutation_rate))
        population = new_population

        best = max(population, key=fitness)
        print(f'Generation {generation + 1}: best = {best}, fitness = {fitness(best)}')

    best_final = max(population, key=fitness)
    print('\nBest solution:', best_final)
    print('Best value:', int(best_final, 2))
    print('Best fitness:', fitness(best_final))


genetic_algorithm()
