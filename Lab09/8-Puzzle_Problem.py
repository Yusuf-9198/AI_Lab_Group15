import heapq

TARGET = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def get_manhattan(board):
    dist = 0
    for idx, val in enumerate(board):
        if val == 0:
            continue
        target_idx = val - 1
        r1, c1 = divmod(idx, 3)
        r2, c2 = divmod(target_idx, 3)
        dist += abs(r1 - r2) + abs(c1 - c2)
    return dist


def get_moves(board):
    blank = board.index(0)
    r, c = divmod(blank, 3)
    valid_states = []

    shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in shifts:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap_idx = nr * 3 + nc
            new_board = list(board)
            new_board[blank], new_board[swap_idx] = new_board[swap_idx], new_board[blank]
            valid_states.append(tuple(new_board))

    return valid_states


def solve_puzzle(start):
    start = tuple(start)
    target = tuple(TARGET)

    # Priority queue stores: (f_score, g_score, current_board, path_taken)
    queue = []
    heapq.heappush(queue, (get_manhattan(start), 0, start, [start]))

    seen = {start: 0}

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current == target:
            return path

        for nxt in get_moves(current):
            cost = g + 1
            if nxt not in seen or cost < seen[nxt]:
                seen[nxt] = cost
                est_total = cost + get_manhattan(nxt)
                heapq.heappush(queue, (est_total, cost, nxt, path + [nxt]))

    return None


# Test run
initial_board = [0, 2, 3, 1, 4, 6, 7, 5, 8]
steps = solve_puzzle(initial_board)

print(f"Solved in {len(steps) - 1} moves.\n")
for step in steps:
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print("-" * 10)