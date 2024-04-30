def dfs(start, goal, graph):
    visited = set()
    path = []
    cost = 0

    stack = [start]
    visited.add(start)

    while stack:
        x = stack.pop()
        path.append(x)
        visited.add(x)

        if x == goal:
            return path, cost

        temp_stack = []
        for y in graph[x]:
            if y not in visited:
                temp_stack.append(y)
                cost += graph[x][y]
        stack.extend(temp_stack[::-1])
    return path, cost


if __name__ == "__main__":
    graph = {
        "A": {"B": 22, "C": 48, "D": 28},
        "B": {"A": 22, "C": 20, "D": 18},
        "C": {"A": 48, "B": 20, "D": 32},
        "D": {"A": 28, "B": 18, "C": 32},
    }

    start = input("Enter the starting node: ")
    end = input("Enter the ending node: ")

    path, cost = dfs(start, end, graph)

    print("Path:", path)
    print("Cost:", cost)
