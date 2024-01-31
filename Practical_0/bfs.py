from collections import deque


def bfs(graph, start):
    visited = set()

    queue = deque([start])
    visited.add(start)

    print("BFS Traversal of graph: ")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for adj in graph[vertex]:
            if adj not in visited:
                queue.append(adj)
                visited.add(adj)
    return


if __name__ == "__main__":
    graph = {
        "A": set(["D", "B", "C"]),
        "B": set([]),
        "C": set(["E", "F"]),
        "D": set(["F"]),
        "E": set([]),
        "F": set([]),
    }
    bfs(graph, "A")
