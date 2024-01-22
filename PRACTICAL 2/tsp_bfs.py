from collections import deque
import timeit


def calculate_distance_bfs(graph, path, state, end):
    visited = set()
    distance = 0
    while state != end:
        for key in list((graph[state]).keys()):
            if key not in visited:
                distance = distance + graph[state][key]
                visited.add(key)
            if key == end:
                break
        if key == end:
            break
        count = count + 1
        state = path[count]
    return distance


def tsp_bfs(graph, start, end):
    visited = set()
    path = []
    distance = 0

    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        path.append(vertex)

        if vertex == end:
            distance = calculate_distance_bfs(graph, path, start, end)
            return path, distance

        for adj in graph[vertex]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)
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
    path, dist = tsp_bfs(graph_1, start, end)
    execution_time = timeit.default_timer() - start_time

    print("Path:", "".join(path))
    print("Cost:", dist)
    print(f"Execution Time:", execution_time)
