def uniform_cost_search(start, goal, graph):
    visited = set()
    path = []
    total_cost = 0

    priority_queue = {start: 0}

    while priority_queue:
        x = min(priority_queue, key=priority_queue.get)
        cost_x = priority_queue[x]
        del priority_queue[x]

        if x not in visited:
            visited.add(x)
            path.append(x)
            total_cost += cost_x

            if x == goal:
                return path, total_cost

            for y in graph[x]:
                if y not in visited:
                    temp_new_cost = cost_x + graph[x][y]
                    if y not in priority_queue or temp_new_cost < priority_queue[y]:
                        priority_queue[y] = temp_new_cost

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

    path, cost = uniform_cost_search(start, end, graph)

    if path:
        print("Path:", path)
        print("Cost:", cost)
    else:
        print("No path found.")
