# MIGHT NOT WORK PROPERLY

h = {
    "A": 40,
    "B": 32,
    "C": 25,
    "D": 35,
    "E": 19,
    "F": 17,
    "G": 0,
    "H": 10,
}

graph = {
    "A": {"B": 11, "C": 14, "D": 7},
    "B": {"A": 11, "E": 15},
    "C": {"A": 14, "E": 8, "F": 10},
    "D": {"A": 7, "F": 25},
    "E": {"B": 15, "C": 8, "H": 9},
    "F": {"C": 10, "G": 20},
    "G": {"F": 20, "H": 10},
    "H": {"E": 9, "G": 10},
}


def hill_climb(start, goal):
    path = []

    path.append(start)
    current = start

    while current != goal:
        for node in graph.keys():
            if node == current:
                minCost = 99999
                minNode = current

                for y in graph[node].keys():
                    if h[y] < minCost:
                        minCost = h[y]
                        minNode = y

                path.append(minNode)
        current = path[-1]

    print(f"The Hill Climbing Algorithm:")
    print(f"\nThe path is as per below: \nStart State -> ", end="")
    for pathNode in path:
        print(f"{pathNode} -> ", end="")
    print(f"Goal State")


Start_State = "A"
Goal_State = "D"

hill_climb(Start_State, Goal_State)
