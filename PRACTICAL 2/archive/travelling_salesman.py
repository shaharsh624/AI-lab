from collections import deque

graph = {
    "A": {"D": 28, "C": 48, "B": 22},
    "B": {"A": 22, "C": 20, "D": 18},
    "C": {"A": 48, "B": 20, "D": 32},
    "D": {"A": 28, "B": 18, "C": 32},
}


def tsp(graph, start, min_cost):
    visited = set()
    stack = deque([start])
    path = ""
    prev = ""

    while stack:
        vertex = stack.pop()
        if prev != "":
            min_cost += graph[vertex][prev]
            # print("\nCost: ", min_cost)
        if vertex not in visited:
            visited.add(vertex)
            prev = vertex
            neighbours = graph[vertex]

            path += vertex
            # print("Vertex: ", vertex)
            # print("Neighbours: ", neighbours)
            for i in neighbours:
                if i not in visited and i not in stack:
                    stack.extend(i)

                # print("Stack: ", stack)

    print("Final cost: ", min_cost + graph[vertex][start])
    print("Path: ", path)

    return


tsp(graph, "A", 0)


"""
ABCD = 102
ABDC = 120
ACBD = 118
ACDB = 120
ADBC = 114
ADCB = 102
"""
