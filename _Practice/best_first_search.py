def best_first_search(start, goal, h, graph):
    OPEN = {start}
    CLOSED = set()
    f = {start: h[start]}
    parent = {start: None}

    while OPEN:
        x = min(OPEN, key=lambda z: f[z])
        OPEN.remove(x)
        CLOSED.add(x)

        if x == goal:
            path = []
            while x is not None:
                path.append(x)
                x = parent[x]
            path.reverse()
            return path

        for y in graph[x]:
            if y not in OPEN and y not in CLOSED:
                OPEN.add(y)
                f[y] = h[y]
                parent[y] = x

    return None


if __name__ == "__main__":
    h = {"S": 5, "A": 3, "B": 4, "C": 2, "D": 6, "G": 0}

    path = {
        "S": {"A": 1, "G": 10},
        "A": {"B": 2, "C": 1},
        "B": {"G": 5},
        "C": {"D": 3, "G": 4},
        "D": {"G": 2},
        "G": {},
    }

    path = best_first_search("S", "D", h, path)

    print(path)
