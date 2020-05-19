import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

def fitFunction(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./(r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs(50./(Z + 50.)))

def fitData(data):
    data = [np.array(i[1:]) for i in data]

    x = np.linspace(1.e6, 500.e6, 10000)
    y = fitFunction(x, 1., 50.e-9, 100.e-9, 4.7e-12)
    plt.plot(x, y)                          # Plotte mit geschätzte Werte
    plt.plot(data[1], data[2])              # Plotte originale Daten

    indices = data[1] < 300.e6
    popt, pcov = curve_fit(fitFunction, data[1][indices], data[2][indices], p0=(1., 50.e-9, 100.e-9, 4.7e-12))
    print(popt)
    print(np.sqrt(np.diag(pcov)))

    plt.plot(data[1], fitFunction(data[1], *popt))   # Plotte Fitfunktion