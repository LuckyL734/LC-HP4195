import matplotlib.pyplot as plt
import numpy as np
import math

#import fitting
print("DATAPROCESSING BEGINNT AB HIER")
# Plotsettings
#-----------------------------------------------------------------------------------------------------------------------
#plt.figure(figsize=(13,7), facecolor="white")
fig, ax = plt.subplots(1, 1, figsize=(18,7))

showPhase = True
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
plt.ylim(-50, -15)

if showPhase:
    ax2 = ax.twinx()
    plt.ylabel(r'$\phi \,\, [^\circ]$')
    plt.ylim(-90, 90)
    if True:  # True adds a zero line
        ax2.plot(np.linspace(1, 500, 400), np.zeros(400), 'b:')

#-----------------------------------------------------------------------------------------------------------------------

# Es gilt für die Daten: data[x][y]
# x gibt Zahl an: 0 - Nummer | 1 - Frequenz [Hz] | 2 - T/R [dB] | 3 - PHASE [deg]
# y gibt nummer der Mesung an (0-400)
def plotdata(dateiname, linestyle):
    data = [[], [], [], []]                                           # Liste für die Datenauswertung erstellen
    dateipfad = r"C:\Users\maxkr_000\Desktop\Bachelorarbeit Stuffs\Messdaten\Originaldaten\{}".format(dateiname)
    with open(dateipfad) as f:                          # Datei öffnen als f
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
    minimumfreq = data[1][np.array(data[2]).argmin()]/10**6
    minimumTrans = data[2][np.array(data[2]).argmin()]
    ax.plot(np.array(data[1])/10**6, data[2], linestyle, label= r"{} {}$f_R = {} \, MHz$ ; $T_m = {} \,dB$".format(dateiname[11:-4:],"\n",round(minimumfreq,2),round(minimumTrans,2)))
    if showPhase:
        ax2.plot(np.array(data[1]) / 10 ** 6, data[3], linestyle+'.',
                label=r"{} {}Phase".format(dateiname[11:-4:],"\n"))

print("DATAPROCESSING ENDET HIER")
