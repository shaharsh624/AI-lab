from collections import deque


def bfs(start, end, graph):
    visited = set()
    path = []
    cost = 0

    queue = deque([start])
    visited.add(start)

    while queue:
        x = queue.popleft()
        path.append(x)

        if x == end:
            return path, cost

        for y in graph[x]:
            if y not in visited:
                queue.append(y)
                visited.add(y)
                path.append(y)
                cost += graph[x][y]
        return  path, cost

if __name__ == "__main__":
    graph = {
        "A": {"B": 22, "C": 48, "D": 28},
        "B": {"A": 22, "C": 20, "D": 18},
        "C": {"A": 48, "B": 20, "D": 32},
        "D": {"A": 28, "B": 18, "C": 32},
    }

    start = input("Enter the starting node: ")
    end = input("Enter the ending node: ")

    path, cost = bfs(start, end, graph)

    print("Path:", path)
    print("Cost:", cost)
