def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)


if __name__ == "__main__":
    graph = {
        "A": set(["D", "B", "C"]),
        "B": set(["D", "A", "C"]),
        "C": set(["D", "B", "A"]),
        "D": set(["A", "B", "C"]),
    }
    dfs(graph, "A")
