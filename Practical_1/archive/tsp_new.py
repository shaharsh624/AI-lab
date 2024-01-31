from collections import deque


# BFS
def tsp_dfs(graph, start, end, visited, cost):
    visited.add(start)
    stack = deque([start])
    neighbours = list(graph[start].keys())
    print(start, ":", neighbours)
    
    x = list(set(neighbours) - (visited))
    print("neighbours-visited", ":", x)
    
    for adj in x:
        print(start, ":", adj)
        tsp_dfs(graph, adj, end, visited, cost)

    # while queue:
    #     vertex = queue.popleft()
    #     visited.add(vertex)
    #     neighbours = list(graph[vertex].keys())

    #     for adj in neighbours:
    #         if adj not in visited:
    #             queue.append(adj)
    #             if (adj == end) and len(visited) != count:
    #                 return

    #             tsp_dfs(
    #                 graph=graph,
    #                 start=adj,
    #                 end=end,
    #                 visited=visited,
    #                 cost=cost,
    #             )

    return


if __name__ == "__main__":
    graph = {
        "A": {"B": 22, "C": 48, "D": 28},
        "B": {"A": 22, "C": 20, "D": 18},
        "C": {"A": 48, "B": 20, "D": 32},
        "D": {"A": 28, "B": 18, "C": 32},
    }
    start = "A"
    end = "D"
    count = len(graph)

    tsp_dfs(graph, start, end, set(), 0)
