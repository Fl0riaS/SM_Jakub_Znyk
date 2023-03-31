
import numpy as np

# region CONSTANTS

LIGHTSPEED = 299792458
G_CH_7_MID_RANGE_FREQ = 2442000000
AC_CH_57_MID_RANGE_FREQ = 5285000000
DIRECTOR_AMOUNT = 8

# endregion

# region HELPER FUNCTIONS


def calculateLamb(f: int) -> float:
    return LIGHTSPEED/f

# endregion

# region ANTENNAS


def biQuad(f: int):
    lamb = calculateLamb(f)

    L1 = lamb/4
    H = lamb
    B = lamb/2
    D = lamb/8
    L2 = np.sqrt(np.power(L1, 2)*2)*2

    totalWireLength = L1 * 8 + B * 2 + H * 2

    print(f"{L1=}m\n{H=}m\n{B=}m\n{D=}m\n{L2=}m\n{totalWireLength=}m\n")
    pass


def yagiUda(f: int):
    lamb = calculateLamb(f)

    reflectorLength = lamb * 0.49
    radiatorLength = lamb * 0.47
    directorLength = lamb * 0.44

    betweenReflectorRadiator = lamb * 0.25
    betweenRadiatorDirector = lamb * 0.20

    print(f"{DIRECTOR_AMOUNT=}\n{reflectorLength=}m\n{radiatorLength=}m\n{directorLength=}m\n{betweenReflectorRadiator=}m\n{betweenRadiatorDirector=}m\n")
    pass


def logPer(f: int, elements: int, t: float):
    lamb = calculateLamb(f)

    # lenghts
    l = np.empty(elements)
    l[0] = lamb/2
    for i in range(elements-1):
        l[i+1] = t * l[i]

    # distances
    optimalSpacing = 0.243 * t - 0.051
    cota = 4 * optimalSpacing / (1-t)
    d = np.empty(elements - 1)
    for i in range(elements - 1):
        d[i] = ( l[i] - l[i+1] ) / 2 * cota

    # printing results
    for i in range(l.size):
        print("Length of element {} = {}m".format(i, l[i]))

    for i in range(d.size):
        print("Distance between element {} and {} = {}m".format(i, i+1, d[i]))


# endregion

# biQuad(G_CH_7_MID_RANGE_FREQ)
# biQuad(AC_CH_57_MID_RANGE_FREQ)
# yagiUda(G_CH_7_MID_RANGE_FREQ)
# yagiUda(AC_CH_57_MID_RANGE_FREQ)
logPer(G_CH_7_MID_RANGE_FREQ, 8, 0.88)
