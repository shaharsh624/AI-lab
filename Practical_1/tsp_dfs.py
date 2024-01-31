import timeit


def calculate_distance_dfs(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]

    distance += graph[path[-1]][path[0]]
    return distance


def tsp_dfs(graph, start, stop):
    visited = set()
    stack = [start]
    path = []
    distance = 0

    while stack:
        vertex = stack.pop()
        path.append(vertex)
        visited.add(vertex)

        if vertex == stop:
            distance = calculate_distance_dfs(graph, path)
            return path, distance

        temp_stack = []
        for adj in graph[vertex]:
            if adj not in visited:
                temp_stack.append(adj)

        stack.extend(temp_stack[::-1])

    return path, distance


if __name__ == "__main__":
    graph_1 = {
        "A": {"B": 22, "C": 48, "D": 28},
        "B": {"A": 22, "C": 20, "D": 18},
        "C": {"A": 48, "B": 20, "D": 32},
        "D": {"A": 28, "B": 18, "C": 32},
    }
    start = input("Enter the starting node: ")
    end = input("Enter the ending node: ")

    start_time = timeit.default_timer()
    path, dist = tsp_dfs(graph_1, start, end)
    execution_time = timeit.default_timer() - start_time

    print("Path:", "".join(path))
    print("Cost:", dist)
    print(f"Execution Time:", execution_time)
