def a_star(start, goal, h, graph):
    OPEN = {start}
    CLOSED = set()
    g = {start: 0}
    f = {start: h[start] + g[start]}
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
            if y not in CLOSED:
                temp = h[y] + graph[x][y]
                if y not in OPEN or temp < g[y]:
                    OPEN.add(y)
                    g[y] = temp
                    f[y] = g[y] + h[y]
                    parent[y] = x

    return None


if __name__ == "__main__":
    h = {"S": 5, "A": 3, "B": 4, "C": 2, "D": 6, "G": 0}

    graph = {
        "S": {"A": 1, "G": 10},
        "A": {"B": 2, "C": 1},
        "B": {"G": 5},
        "C": {"D": 3, "G": 4},
        "D": {"G": 2},
        "G": {},
    }

    path = a_star("S", "D", h, graph)
    print(path)
