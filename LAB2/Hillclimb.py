def objective(x):
    return -(x - 5) ** 2 + 25


def hill_climbing(start):
    current = start
    current_value = objective(current)

    while True:
        left = current - 1
        right = current + 1
        left_value = objective(left)
        right_value = objective(right)

        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break

    return current, current_value


start = 0
best_x, best_value = hill_climbing(start)
print('Starting point:', start)
print('Best point:', best_x)
print('Best value:', best_value)
