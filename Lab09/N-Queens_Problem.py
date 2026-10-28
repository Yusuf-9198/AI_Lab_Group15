import random


def fitness(board):
    n = len(board)
    max_pairs = (n * (n - 1)) // 2
    attacking_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Check same row or same diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1

    return max_pairs - attacking_pairs


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    return parent1[:point] + parent2[point:]


def mutate(board, mutation_rate=0.1):
    if random.random() < mutation_rate:
        col = random.randint(0, len(board) - 1)
        board[col] = random.randint(0, len(board) - 1)
    return board


def genetic_n_queens(n=8, pop_size=100, generations=1000):
    max_fitness = (n * (n - 1)) // 2
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(pop_size)]

    for gen in range(generations):
        population.sort(key=fitness, reverse=True)

        if fitness(population[0]) == max_fitness:
            return population[0], gen

        # Keep top 20% as parents for the next generation
        elites = population[:pop_size // 5]
        next_gen = elites[:]

        while len(next_gen) < pop_size:
            p1, p2 = random.sample(elites, 2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)

        population = next_gen

    return population[0], generations


# Example execution
solution, gen_count = genetic_n_queens(n=8)
print(f"Best N-Queens Board: {solution} (Found at generation {gen_count}, Fitness: {fitness(solution)}/28)")