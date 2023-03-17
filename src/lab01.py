import math
import numpy as np
import matplotlib.pyplot as plt

LIGHTSPEED = 299792458

#region CALCULATING FUNCTIONS
def convertToDecibel(value):
    return 10 * np.log10(value)

def calculatePowerDecrease(gt, gr, lamb, d, decibel = True):
    ratioLinear = gt * gr * pow((lamb / (4 * math.pi * d)),2)
    if(decibel):
        return convertToDecibel(ratioLinear)
    return ratioLinear

def calculateLamb(f) -> float:
    return LIGHTSPEED/f

def calculatePowerDecreaseTwoWay(gt, gr, f, d, h1, h2):
    lamb = calculateLamb(f)
    leftSide = calculatePowerDecrease(gr, gt, lamb, d, decibel=False)
    d1 = calculateDistance(h1, h2, d, 1)
    d2 = calculateDistance(h1, h2, d, 2)
    fi1 = calculateFi(f, d1)
    fi2 = calculateFi(f, d2)
    e1 = np.cos(fi1) + (np.sin(fi1) * 1j)
    e2 = np.cos(fi2) + (np.sin(fi2) * 1j)
    leftAbsFragment = 1/d1 * e1
    rightAbsFragment = 1/d2 * e2
    rightSide = np.abs(leftAbsFragment - rightAbsFragment)
    return convertToDecibel(leftSide * rightSide)

def calculateDistance(h1, h2, d, variant) -> float:
    if(variant == 1):
        return np.sqrt(np.power((h1-h2),2)+np.power(d,2))
    if(variant == 2):
        return np.sqrt(np.power((h1+h2),2)+np.power(d,2))
    pass

def calculateFi(f,d):
    c = LIGHTSPEED
    return -2 * math.pi * f * d / c
    
#endregion

#region EXERCISES
def ex1(variant: str):
    lamb1 = calculateLamb(900000000)
    lamb2 = calculateLamb(2400000000)

    if(variant == 'a'):
        d = np.linspace(1,100,399)
        res1 = calculatePowerDecrease(1.6, 1.6, lamb1, d)
        res2 = calculatePowerDecrease(1.6, 1.6, lamb2, d)
    else:
        d = np.linspace(1,10000,10000)
        res1 = calculatePowerDecrease(1.6, 1.6, lamb1, d)
        res2 = calculatePowerDecrease(1.6, 1.6, lamb2, d)
    
    plt.plot(d,res1, label='900Mhz')
    plt.plot(d,res2, label='2400Mhz')
    
    plt.title('Wzgledny spadek mocy sygnalu')
    plt.xlabel("d[m]")
    plt.ylabel("Pr/Pt[dB]")
    plt.legend()

    return plt.show()

def ex2():
    s = np.linspace(1,10000,10000)
    v = LIGHTSPEED
    t = s/v

    plt.plot(s,t)
    
    plt.title('Opoznienia sygnalu ze wzgledu na przebyta droga')
    plt.xlabel("s[m]")
    plt.ylabel("t[s]")

    return plt.show()

def ex3(variant: str):
    if(variant == 'a'):
        d = np.linspace(1,100,399)
        res1 = calculatePowerDecreaseTwoWay(1.6, 1.6, 900000000, d, 30, 3)
        res2 = calculatePowerDecreaseTwoWay(1.6, 1.6, 2400000000, d, 30, 3)
    else:
        d = np.linspace(1,10000,10000)
        res1 = calculatePowerDecreaseTwoWay(1.6, 1.6, 900000000, d, 30, 3)
        res2 = calculatePowerDecreaseTwoWay(1.6, 1.6, 2400000000, d, 30, 3)

    plt.plot(d, res1, label='900Mhz')
    plt.plot(d, res2, label='2400Mhz')

    plt.title('Wzgledny spadek mocy sygnalu')
    plt.xlabel("d[m]")
    plt.ylabel("Pr/Pt[dB]")
    plt.legend()

    return plt.show()

#endregion


if __name__ == '__main__':
  # func benchmark
  print(calculatePowerDecrease(1.6,1.6,0.3,1))

  ex1('a')
  ex1('b')
  ex2()
  ex3('a')
  ex3('b')

    