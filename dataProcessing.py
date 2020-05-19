import matplotlib.pyplot as plt
import numpy as np
import ast
from scipy.optimize import curve_fit
import math

#import fitting
print("DATAPROCESSING BEGINNT AB HIER")
#LOADING SAMPLE DICTIONARY
with open('sampleDictionary.txt', 'r') as f:
    samples = ast.literal_eval(f.read())

# Plotsettings
#-----------------------------------------------------------------------------------------------------------------------
#plt.figure(figsize=(13,7), facecolor="white")
fig, ax = plt.subplots(1, 1, figsize=(18,7))

showPhase = False
titelName = ""


def setTitle(tl):
    global titelName
    titelName = tl
    plt.title(titelName)
# Allgemein
#plt.title(titelName)
plt.xlim(1, 500)
plt.xlabel(r'$f\, \, [MHz]$')
# Für T/R
plt.ylabel(r'$\frac{T}{R} \,\, [dB]$')
plt.ylim(-60, 5)

if showPhase:
    ax2 = ax.twinx()
    plt.ylabel(r'$\phi \,\, [^\circ]$')
    plt.ylim(-90, 90)
    if True:  # True adds a zero line
        ax2.plot(np.linspace(1, 500, 400), np.zeros(400), 'b:')

#-----------------------------------------------------------------------------------------------------------------------
def readData(dateiname):
    data = [[], [], [], []]  # Liste für die Datenauswertung erstellen
    dateipfad = r"C:\Users\maxkr_000\Desktop\Bachelorarbeit Stuffs\Messdaten\Originaldaten\{}".format(dateiname)
    with open(dateipfad) as f:  # Datei öffnen als f
        for i, line in enumerate(f):  # Jede Linie der Datei durchgehen
            if i >= 7 and i <= 406:  # Unbrauchbarer Teil oben und unten weglassen # ERSTER WERT WEGGELASSEN, DA SINNLOS
                line = list(line[:-1])  # \n am Ende der Strings entfernen
                line[4] = ';'  # Trennungen der Zahlen hinzufügen
                line[21] = ';'
                line[38] = ';'
                line = ''.join(line)
                # print(line)
                dataline = line.strip().split(";")  # Zeile in Liste mit einzelnen Zahlen umwandeln
                for i, x in enumerate(dataline):  # Strings einer Zeile durchgehen und verarbeiten
                    newDataline = ""
                    for c in x:
                        if c != " " and c != "m" and c != "u":  # Leerzeichen aus den Strings entfernen
                            newDataline += c
                        if c == "m":  # m als "*0.001" umwandeln zum verrechnen
                            newDataline += "*0.001"
                        if c == "u":
                            newDataline += "*0.000001"
                    data[i].append(
                        eval(newDataline))  # String in Zahl umwandeln, sowie milli verrechnen und an die Daten anhängen
    return data


# Es gilt für die Daten: data[x][y]
# x gibt Zahl an: 0 - Nummer | 1 - Frequenz [Hz] | 2 - T/R [dB] | 3 - PHASE [deg]
# y gibt nummer der Mesung an (0-400)
def plotData(dateiname, linestyle, fit=False):
    data = readData(dateiname)
    minimumfreq = data[1][np.array(data[2]).argmin()]/10**6
    minimumTrans = data[2][np.array(data[2]).argmin()]
    if dateiname[-10:-9] == "S":
        # Show Sample data in legend
        ax.plot(np.array(data[1])/10**6, data[2], linestyle,
                label= r"{} {}$f_R = {} \, MHz$ ; $T_m = {} \,dB${}{}".format(dateiname[11:-4:],"\n",round(minimumfreq,2),
                                                                          round(minimumTrans,2), "\n", samples[dateiname[-9:-4]]))
    else:
        # No Sample found
        ax.plot(np.array(data[1]) / 10 ** 6, data[2], linestyle,
                label=r"{} {}$f_R = {} \, MHz$ ; $T_m = {} \,dB$".format(dateiname[11:-4:], "\n", round(minimumfreq, 2),
                                                                         round(minimumTrans, 2)))
    if showPhase:
        ax2.plot(np.array(data[1]) / 10 ** 6, data[3], linestyle+'.',
                label=r"{} {}Phase".format(dateiname[11:-4:],"\n"))

    if fit:
        fitData(data, linestyle=linestyle, dateiname=dateiname)

print("DATAPROCESSING ENDET HIER")

def fitFunction(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./(r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs(50./(Z + 50.)))

def fitData(data, linestyle="b-", dateiname="Fitfunktion"):
    data = [np.array(i[1:]) for i in data]

    x = np.linspace(1.e6, 500.e6, 10000)
    y = fitFunction(x, 1., 50.e-9, 100.e-9, 4.7e-12)
    plt.plot(x/10**6, y)                          # Plotte mit Startwerten
    #plt.plot(data[1], data[2])              # Plotte originale Daten

    indices = data[1] < 350.e6
    popt, pcov = curve_fit(fitFunction, data[1][indices], data[2][indices], p0=(1., 50.e-9, 100.e-9, 4.7e-12))
    print(popt)
    print(np.sqrt(np.diag(pcov)))
    err = np.sqrt(np.diag(pcov))

    ax.plot(np.array(np.linspace(1.e6, 500.e6, 1000)) / 10**6, np.array(fitFunction(np.linspace(1.e6, 500.e6, 1000), *popt)), linestyle+".",
            label= r"Fit zu {} {}$R_W = {}({}) \, \Omega$ ; $L_p = {}({}) \,nH$ {}$L = {}({}) nH$ ; $C = {}({})pF$".format(dateiname[11:-4:],"\n",round(popt[0],3),
                                                                                        round(err[0],3),round(popt[1]*10**9,2),round(err[1]*10**9,2),"\n",round(popt[2]*10**9,2),round(err[2]*10**9,2),round(popt[3]*10**12,2),round(err[3]*10**12,2)))
                                                                              # Plotte Fitfunktion

ax.plot(np.zeros(100)+300, np.linspace(-60,10, 100), "b:")