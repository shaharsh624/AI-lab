from collections import deque

graph = {
    "A": {"B": 22, "C": 48, "D": 28},
    "B": {"A": 22, "C": 20, "D": 18},
    "C": {"A": 48, "B": 20, "D": 32},
    "D": {"A": 28, "B": 18, "C": 32},
}
start = "A"
end = "D"
count = len(graph)

global path
path = start


# BFS
def tsp_dfs(graph, start, end, visited, cost, count):
    global path

    if (start == end) and (count == len(path)):
        print(path)
        return

    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        print(vertex, end=", \n")

        neighbours = list(graph[vertex].keys())

        for adj in neighbours:
            if adj not in visited:
                queue.append(adj)
                print(adj)
                path += adj
                if (adj == end) and len(visited) != count:
                    return

                tsp_dfs(
                    graph=graph,
                    start=adj,
                    end=end,
                    visited=visited,
                    cost=cost,
                    count=count,
                )

    # print(path)
    return


tsp_dfs(graph, start, end, set(), 0, count)
