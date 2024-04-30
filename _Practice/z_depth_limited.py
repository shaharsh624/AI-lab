# MIGHT NOT WORK PROPERLY


def dfs_depth_limited(start, goal, depth_limit, graph):
    visited = set()
    path = []
    cost = 0
    depth = 0

    stack = [(start, depth)]
    visited.add(start)

    while stack:
        x, depth = stack.pop()
        path.append(x)
        visited.add(x)

        if x == goal or depth == depth_limit:
            return path, cost

        temp_stack = []
        for y in graph[x]:
            if y not in visited:
                temp_stack.append((y, depth + 1))
                cost += graph[x][y]
        stack.extend(temp_stack[::-1])

    return None, None


if __name__ == "__main__":
    graph = {
        "A": {"B": 22, "C": 48, "D": 28},
        "B": {"A": 22, "C": 20, "D": 18},
        "C": {"A": 48, "B": 20, "D": 32},
        "D": {"A": 28, "B": 18, "C": 32},
    }

    start = input("Enter the starting node: ")
    end = input("Enter the ending node: ")
    depth = int(input("Enter depth limit [0-START]: "))

    path, cost = dfs_depth_limited(start, end, depth, graph)

    print("Path:", path)
    print("Cost:", cost)
