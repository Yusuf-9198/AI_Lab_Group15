import heapq


def a_star_search(graph, heuristic, start, goal):
    open_list = [(heuristic.get(start, 0), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}

    while open_list:
        _, cost_so_far, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, goal), cost_so_far

        for neighbor, weight in graph.get(current, []):
            new_cost = g_score[current] + weight
            if neighbor not in g_score or new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                came_from[neighbor] = current
                priority = new_cost + heuristic.get(neighbor, 0)
                heapq.heappush(open_list, (priority, new_cost, neighbor))

    return None, float('inf')


def reconstruct_path(came_from, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    return path[::-1]


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {'A': 5, 'B': 3, 'C': 1, 'D': 0}

path, cost = a_star_search(graph, heuristic, 'A', 'D')
print('A* Path:', path)
print('A* Cost:', cost)
