def a_star(initial_state, goal_state, h, path):
    OPEN = {initial_state}
    CLOSED = set()
    g = {initial_state: 0}
    f = {state: 9999 for state in path.keys()}

    f[initial_state] = h[initial_state] + g[initial_state]
    parents = {state: "" for state in path.keys()}

    while OPEN:
        min_f = 9999999
        for state in OPEN:
            if f[state] <= min_f:
                BEST_NODE = state
                min_f = f[state]
        OPEN.remove(BEST_NODE)
        print(BEST_NODE)
        if BEST_NODE == goal_state:
            return

        for neighbour in path[BEST_NODE]:
            if neighbour in CLOSED:
                continue
            g_neighbour = g[BEST_NODE] + path[BEST_NODE][neighbour]
            if neighbour not in OPEN or g_neighbour < g[BEST_NODE]:
                OPEN.add(neighbour)
                parents[neighbour] = BEST_NODE
                g[neighbour] = g[BEST_NODE] + path[BEST_NODE][neighbour]
                f[neighbour] = g[neighbour] + h[neighbour]
        # print(parents)


if __name__ == "__main__":
    h = {"S": 5, "A": 3, "B": 4, "C": 2, "D": 6, "G": 0}

    path = {
        "S": {"A": 1, "G": 10},
        "A": {"B": 2, "C": 1},
        "B": {"D": 5},
        "C": {"D": 3},
        "D": {"G": 2},
        "G": {},
    }

    a_star("S", "G", h, path)

"""
    while OPEN:
        min_f = min(f.values())
        for state in OPEN:
            if f[state] <= min_f:
                BEST_NODE = state
                break
        OPEN.remove(BEST_NODE)
        CLOSED.add(BEST_NODE)

        if BEST_NODE == goal_state:
            return

        # Backward Links
        SUCCESSORS = {state: BEST_NODE for state in (path[BEST_NODE].keys())}

        for SUCCESSOR in SUCCESSORS:
            g[SUCCESSOR] = g[BEST_NODE] + path[BEST_NODE][SUCCESSOR]

            if SUCCESSOR in OPEN:
                OLD = SUCCESSOR
            elif SUCCESSOR not in OPEN and SUCCESSOR in CLOSED:
                CLOSED_OLD = SUCCESSOR
            else:
                OPEN.add(SUCCESSOR)
                SUCCESSORS[SUCCESSOR] = BEST_NODE

        print(SUCCESSORS)
"""
