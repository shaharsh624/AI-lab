from collections import defaultdict

j1, j2, target = 4, 3, 2
visited = defaultdict(lambda: False)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def canMeasureWater(j1, j2, cap):
    if j1 + j2 < cap:
        return False
    if cap % gcd(j1, j2) == 0:
        return True
    return False


def waterJug(c1, c2):
    if (c1 == target and c2 == 0) or (c1 == 0 and c2 == target):
        print(c1, c2)
        return True
    if visited[(c1, c2)] == False:
        print(c1, c2)
        visited[(c1, c2)] = True

        return (
            waterJug(0, c2)
            or waterJug(c1, 0)
            or waterJug(j1, c2)
            or waterJug(c1, j2)
            or waterJug(c1 + min(c2, (j1 - c1)), c2 - min(c2, (j1 - c1)))
            or waterJug(c1 - min((j2 - c2), c1), c2 + min((j2 - c2), c1))
        )
    else:
        return False


if __name__ == "__main__":
    if canMeasureWater(j1, j2, target):
        waterJug(0, 0)
