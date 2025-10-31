# Hardcoded tree (minimax values at leaves)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3, 'E': 5, 'F': 2, 'G': 9
}


def alphabeta(node, alpha, beta, maximizing):
    # If leaf node
    if type(tree[node]) == int:
        return tree[node]


    if maximizing:
        value = float('-inf')
        for child in tree[node]:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # beta cut-off
        return value
    else:
        value = float('inf')
        for child in tree[node]:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # alpha cut-off
        return value


# Run alpha-beta starting at root 'A' with maximizing player
best_value = alphabeta('A', float('-inf'), float('inf'), True)
print("Best Value for Maximizing Player:", best_value)