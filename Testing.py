import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pathlib

dateiname = r"15.05.2020\0.8isoSil8C1KeramikRange0-500.txt"

def read_file(path):
    # path = pathlib.Path(path)
    # if not path.is_file():
    #     print("Der Pfad ist ungültig.")
    #     return

    data = [[], [], [], []]                                           # Liste für die Datenauswertung erstellen
    with open(path) as f:                          # Datei öffnen als f
        for i,line in enumerate(f):                     # Jede Linie der Datei durchgehen
            if i >= 6 and i <=406:                      # Unbrauchbarer Teil oben und unten weglassen
                line = list(line[:-1])                  # \n am Ende der Strings entfernen
                line[4] = ';'                           # Trennungen der Zahlen hinzufügen
                line[21] = ';'
                line[38] = ';'
                line = ''.join(line)
                #print(line)
                dataline = line.strip().split(";")      # Zeile in Liste mit einzelnen Zahlen umwandeln
                newDataline = ""
                for i,x in enumerate(dataline):         # Strings einer Zeile durchgehen und verarbeiten
                    newDataline = ""
                    for c in x:
                        if c != " " and c != "m" and c != "u":       # Leerzeichen aus den Strings entfernen
                            newDataline += c
                        if c == "m":                    # m als "*0.001" umwandeln zum verrechnen
                            newDataline += "*0.001"
                        if c == "u":
                            newDataline += "*0.000001"
                    data[i].append(eval(newDataline))     # String in Zahl umwandeln, sowie milli verrechnen und an die Daten anhängen
    return data


def fit_function(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./(r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs(50./(Z + 50.)))


data = [np.array(i[1:]) for i in read_file(r"C:\Users\maxkr_000\Desktop\Bachelorarbeit Stuffs\Messdaten\Originaldaten\{}".format(dateiname))]


x = np.linspace(1.e6, 500.e6, 10000)
y = fit_function(x, 1., 50.e-9, 100.e-9, 4.7e-12)
plt.plot(x, y)                          # Plotte mit geschätzte Werte
plt.plot(data[1], data[2])              # Plotte originale Daten

indices = data[1] < 300.e6
popt, pcov = curve_fit(fit_function, data[1][indices], data[2][indices], p0=(1., 50.e-9, 100.e-9, 4.7e-12))
print(popt)
print(np.sqrt(np.diag(pcov)))

plt.plot(data[1], fit_function(data[1], *popt))   # Plotte Fitfunktion

plt.show()