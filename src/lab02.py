import numpy as np

# region TYPES


class Obstacle:
    def __init__(self, amount, damping) -> None:
        self.amount = amount
        self.damping = damping

    def totalDamping(self):
        return self.amount * self.damping

# endregion

# region MODELS


def freeSpace(f: int, d: float) -> float:
    return -27.55 + 20 * np.log10(f) + 20 * np.log10(d)


def itu(f: int, d: float, floorsAmount: int) -> float:
    return 20 * np.log10(f) + ituDistanceDamping(f) * np.log10(d) + ituRoofDamping(floorsAmount, f) - 28


def oneSlope(f: int, d: float) -> float:
    y = 4.5
    l0 = freeSpace(f, d)
    return l0 + 10 * y * np.log10(d)


def motleyKeenan(f: int, d: float, roofsAmount: int, wallsAmount: int, wallType="inside-wall") -> float:
    lfs = freeSpace(f, d)
    return lfs + wallsAmount * damping(wallType) + roofsAmount * damping("roof")


def multiWall(f, d, walls: list[Obstacle], roofs: list[Obstacle]) -> float:
    l0 = freeSpace(f, d)
    y = 4.5

    # Wall damping
    totalWallDamping = 0
    for wall in walls:
        totalWallDamping += wall.totalDamping()

    # Roof damping
    totalRoofDamping = 0
    for roof in roofs:
        totalRoofDamping += roof.totalDamping()

    return l0 + 10 * y * np.log10(d) + totalWallDamping + totalRoofDamping


# endregion

# region MODEL_HELPERS


def ituDistanceDamping(f: int):
    return 28
    # if f < 3000 and f > 1500:
    #     return 30
    # if f == 5000:
    #     return 31
    # pass


def ituRoofDamping(n: int, f: int):
    if f < 3000 and f > 1500:
        return 15+4*(n-1)
    if f == 5000:
        return 16


def damping(type: str):
    match type:
        case "wall-inside":
            return 7
        case "wall-outside":
            return 9
        case "roof":
            return 11
        case "window":
            return 4.5
        case _:
            return 0


# endregion

def energeticBalance(L: float):
    Pn = 20
    Go = 20
    Gn = 20
    A = 20
    return Pn + Gn + Go - L - A


def printResults(resultArray):
    print('Rzeczywiste: ', resultArray[0], 'dBm')
    print('Tłumienie w swobodnej przestrzeni: ', resultArray[1], 'dBm')
    print('ITU-R P.1238: ', resultArray[2], 'dBm')
    print('Model One-Slope: ', resultArray[3], 'dBm')
    print('Model Motleya-Keenana: ', resultArray[4], 'dBm')
    print('Model Multi-Wall: ', resultArray[5], 'dBm')


# Ex
# Inside
# printResults([-30, energeticBalance(freeSpace(2412, 1.5)), energeticBalance(itu(2412, 1.5, 0)), energeticBalance(
#     oneSlope(2412, 1.5)), energeticBalance(motleyKeenan(2412, 1.5, 0, 0)), energeticBalance(multiWall(2412, 1.5, [], []))])
# printResults([-46, energeticBalance(freeSpace(2412, 3)), energeticBalance(itu(2412, 3, 0)), energeticBalance(
#     oneSlope(2412, 3)), energeticBalance(motleyKeenan(2412, 3, 0, 0)), energeticBalance(multiWall(2412, 3, [], []))])
# printResults([-46, energeticBalance(freeSpace(2412, 4.5)), energeticBalance(itu(2412, 4.5, 0)), energeticBalance(
#     oneSlope(2412, 4.5)), energeticBalance(motleyKeenan(2412, 4.5, 0, 0)), energeticBalance(multiWall(2412, 4.5, [], []))])

# Walls
# printResults([-45, energeticBalance(freeSpace(2412, 2)), energeticBalance(itu(2412, 2, 0)), energeticBalance(
#     oneSlope(2412, 2)), energeticBalance(motleyKeenan(2412, 2, 1, 0)), energeticBalance(multiWall(2412, 2, [Obstacle(1, 2)], []))])
# printResults([-65, energeticBalance(freeSpace(2412, 4)), energeticBalance(itu(2412, 4, 0)), energeticBalance(
#     oneSlope(2412, 4)), energeticBalance(motleyKeenan(2412, 4, 1, 0)), energeticBalance(multiWall(2412, 4, [Obstacle(1, 2)], []))])
# printResults([-67, energeticBalance(freeSpace(2412, 7)), energeticBalance(itu(2412, 7, 0)), energeticBalance(
#     oneSlope(2412, 7)), energeticBalance(motleyKeenan(2412, 7, 2, 0)), energeticBalance(multiWall(2412, 7, [Obstacle(1, 2), Obstacle(1, 7)], []))])

# Roofs
printResults([-69, energeticBalance(freeSpace(2412, 4.5)), energeticBalance(itu(2412, 4.5, 1)), energeticBalance(
    oneSlope(2412, 4.5)), energeticBalance(motleyKeenan(2412, 4.5, 1, 1)), energeticBalance(multiWall(2412, 4.5, [Obstacle(1, 7)], [Obstacle(1, 11)]))])
printResults([-78, energeticBalance(freeSpace(2412, 5)), energeticBalance(itu(2412, 5, 1)), energeticBalance(
    oneSlope(2412, 5)), energeticBalance(motleyKeenan(2412, 5, 1, 1)), energeticBalance(multiWall(2412, 5, [Obstacle(1, 7)], [Obstacle(1, 11)]))])
printResults([-86, energeticBalance(freeSpace(2412, 6.5)), energeticBalance(itu(2412, 6.5, 2)), energeticBalance(
    oneSlope(2412, 6.5)), energeticBalance(motleyKeenan(2412, 6.5, 1, 2)), energeticBalance(multiWall(2412, 7, [Obstacle(1, 7), Obstacle(2, 11)], []))])

