from collections import deque


# BFS
def tsp_dfs(graph, start, end, visited, cost):
    visited.add(start)
    stack = deque([start])
    neighbours = list(graph[start].keys())
    print(start, ":", neighbours)
    
    x = list(set(neighbours) - (visited))
    # print("neighbours-visited", ":", x)
    
    for adj in x:
        # print(start, ":", adj)
        tsp_dfs(graph, adj, end, visited, cost)
        visited.remove(adj)

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
        "A": {"B": 2, "G": 6},
        "B": {"A": 2, "C": 7, "E": 2},
        "C": {"B": 7, "D": 3, "F": 3},
        "D": {"C": 3, "H": 2},
        "E": {"B": 2, "F": 2, "G": 1},
        "F": {"C": 3, "E": 2, "H": 2},
        "G": {"A": 6, "E": 1, "H": 4},
        "H": {"D": 2, "F": 2, "G": 4},
    }
    start = "A"
    end = "H"
    count = len(graph)

    tsp_dfs(graph, start, end, set(), 0)
