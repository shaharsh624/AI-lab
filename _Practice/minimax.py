def minimax(node, depth, is_maximizing, graph):
    if depth == 0 or not graph[node]:
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        children = get_children(node, graph)

        for child in children:
            eval = minimax(child, depth - 1, False, graph)
            max_eval = max(eval, max_eval)

        print(max_eval)
        return max_eval

    else:
        min_eval = float("inf")
        children = get_children(node, graph)

        for child in children:
            eval = minimax(child, depth - 1, True, graph)
            min_eval = min(eval, min_eval)

        print(min_eval)
        return min_eval


def get_children(node, graph):
    return graph.get(node, [])


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": ["J", "K"],
        "F": ["L", "M"],
        "G": ["N", "O"],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": [],
        "O": [],
    }

    ans = minimax("A", 6, True, graph)
    print(ans)
