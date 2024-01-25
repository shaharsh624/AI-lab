from collections import deque


def water_jug_BFS(x, y, z):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (jug_a, jug_b), actions = queue.popleft()

        if jug_a == z or jug_b == z or jug_a + jug_b == z:
            return actions + ["Success"], True

        if (jug_a, jug_b) in visited:
            continue

        visited.add((jug_a, jug_b))

        # Fill jug A
        if jug_a < x:
            queue.append(((x, jug_b), actions + ["Fill A"]))

        # Fill jug B
        if jug_b < y:
            queue.append(((jug_a, y), actions + ["Fill B"]))

        # Empty jug A
        if jug_a > 0:
            queue.append(((0, jug_b), actions + ["Empty A"]))

        # Empty jug B
        if jug_b > 0:
            queue.append(((jug_a, 0), actions + ["Empty B"]))

        # Pour from A to B
        if jug_a + jug_b >= y:
            queue.append(((jug_a - (y - jug_b), y), actions + ["Pour A to B"]))
        else:
            queue.append(((0, jug_a + jug_b), actions + ["Pour A to B"]))

        # Pour from B to A
        if jug_a + jug_b >= x:
            queue.append(((x, jug_b - (x - jug_a)), actions + ["Pour B to A"]))
        else:
            queue.append(((jug_a + jug_b, 0), actions + ["Pour B to A"]))

    return [], False

if __name__ == "__main__":
    n = int(input("Enter jug A's capacity (n): "))
    m = int(input("Enter jug B's capacity (m): "))
    d = int(input("Enter capacity to measure (d): "))

    actions, result = water_jug_BFS(n, m, d)

    if result:
        print("The sequence of actions is:")
        for action in actions:
            print(action)
    else:
        print("No solution found.")
