import math

def minimax_alpha_beta(depth, node_index, is_maximizing, values, alpha, beta, max_depth):
    # Base case: leaf node reached
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        best = -math.inf
        for i in range(2):
            val = minimax_alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax_alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off
        return best

# Example execution on a binary game tree of depth 3 (8 leaf nodes)
leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]
tree_depth = int(math.log2(len(leaf_scores)))

optimal_value = minimax_alpha_beta(0, 0, True, leaf_scores, -math.inf, math.inf, tree_depth)
print(f"Optimal Game Value: {optimal_value}")