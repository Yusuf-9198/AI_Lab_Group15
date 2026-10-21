
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
       
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

          
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


result = dfs(graph, 'A')
print(result)