def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def canMeasureWater(j1: int, j2: int, cap: int) -> bool:
    if j1 + j2 < cap:
        return False
    if cap % gcd(j1, j2) == 0:
        return True
    return False


if __name__ == "__main__":
    print(canMeasureWater(4, 3, 2))
