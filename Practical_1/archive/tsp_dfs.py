def calculate_dist(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]
    return total_distance


def tsp_dfs(graph, current, visited, path, min_distance, optimal_path):
    if len(visited) == len(graph):
        distance = calculate_dist(graph, path)
        if distance < min_distance[0]:
            min_distance[0] = distance
            optimal_path[0] = path[:]
        return

    # Visit all unvisited neighbours
    for neighbour in range(len(graph)):
        if neighbour not in visited:
            path.append(neighbour)
            visited.add(neighbour)
            tsp_dfs(graph, neighbour, visited, path, min_distance, optimal_path)
            # Backtrack: remove current from path and visited set
            path.pop()
            visited.remove(neighbour)


def tsp_wrapper(graph):
    start = 0
    visited = {start}
    min_distance = [float("inf")]
    optimal_path = [None]
    tsp_dfs(graph, start, visited, [start], min_distance, optimal_path)
    return optimal_path[0], min_distance[0]


def generate_adj_matrix(graph):
    cities = sorted(list(set(city for city in graph.keys())))
    matrix_size = len(cities)
    adj_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    for i, city1 in enumerate(cities):
        for j, city2 in enumerate(cities):
            if city2 in graph[city1]:
                adj_matrix[i][j] = graph[city1][city2]
    return adj_matrix


if __name__ == "__main__":
    # Define the graph with cities as nodes and distances as edges
    graph_1 = {
        "A": {"B": 22, "C": 48, "D": 28},
        "B": {"A": 22, "C": 20, "D": 18},
        "C": {"A": 48, "B": 20, "D": 32},
        "D": {"A": 28, "B": 18, "C": 32},
    }

    graph_2 = {
        "A": {"B": 2, "G": 6},
        "B": {"A": 2, "C": 7, "E": 2},
        "C": {"B": 7, "D": 3, "F": 3},
        "D": {"C": 3, "H": 2},
        "E": {"B": 2, "F": 2, "G": 1},
        "F": {"C": 3, "E": 2, "H": 2},
        "G": {"A": 6, "E": 1, "H": 4},
        "H": {"D": 2, "F": 2, "G": 4},
    }

    adj_matrix = generate_adj_matrix(graph_2)
    optimal_path, min_distance = tsp_wrapper(adj_matrix)

    nodes = list(graph_2.keys())
    path = ""

    for x in optimal_path:
        path += nodes[int(x)]

    print("Optimal Path:", optimal_path)
    print("Minimum Distance:", min_distance)
