from collections import deque


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        next_row = row + dr
        next_col = col + dc
        if 0 <= next_row < 3 and 0 <= next_col < 3:
            new_state = list(state)
            swap_index = next_row * 3 + next_col
            new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]
            neighbors.append(tuple(new_state))

    return neighbors


def bfs_8_puzzle(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
solution = bfs_8_puzzle(start, goal)

if solution:
    print('Solution found!')
    print('Number of moves:', len(solution) - 1)
    for state in solution:
        print_puzzle(state)
else:
    print('No solution found.')
