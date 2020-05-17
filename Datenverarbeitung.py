import matplotlib.pyplot as plt
import numpy as np
import math

#import fitting

print("METHODE BEGINNT AB HIER:")
# Es gilt für die Daten: data[x][y]
# x gibt Zahl an: 0 - Nummer | 1 - Frequenz [Hz] | 2 - T/R [dB] | 3 - PHASE [deg]
# y gibt nummer der Mesung an (0-400)

# Farben in matplotlib: b ; g ; r ; c ; m ; y ; b
# Linien in matplotlib: - ; -- ; -. ; :
# Marker in matplotlib: o ; s ; D ; ^ ; x ; * ; +
#-----------------------------------------------------------------------------------------------------------------------
# VARIABLEN ZUR SCHNELLEN AUSWERTUNG:
messdaten = [
#(r"30.04.2020\backgroundKrokparalell.txt", "r-."),
#(r"30.04.2020\backgroundKrokauseinander.txt", "g-."),
#(r"07.05.2020\0.8isoSil2C47KerkoRange90-120.txt", "b-"),
#(r"07.05.2020\0.8isoSil2C47KerkoRange90-120S13495.txt", "c-"),
(r"07.05.2020\0.8isoSil4C4.7KeramikRange190-220.txt", "r-"),
(r"07.05.2020\0.8isoSil4C4.7KeramikRange190-220S13495.txt", "m-"),
(r"07.05.2020\0.8isoSil4C4.7KeramikRange190-220S13440.txt", "c-"),
(r"07.05.2020\0.8isoSil4C4.7KeramikRange190-220S13504.txt", "b-"),
#(r"07.05.2020\0.8isoSil4C4.7KeramikRange190-220S13498.txt", "y-"),
(r"07.05.2020\0.8isoSil8C1KeramikRange230-250.txt", "g-"),
(r"07.05.2020\0.8isoSil8C1KeramikRange230-250S13495.txt", "y-"),

    #(r"24.04.2020\rotCu5C10Range0-500.txt", "b-")
]

titelName = "Variation von C und N bei 0.8isoSil + Sample 13495 Range in f_R"

willPrint = False
#-----------------------------------------------------------------------------------------------------------------------
# Plotsettings
#-----------------------------------------------------------------------------------------------------------------------
#plt.figure(figsize=(13,7), facecolor="white")
fig, ax = plt.subplots(1, 1, figsize=(18,7))
# Allgemein
plt.title(titelName)
plt.xlim(1, 500)
plt.xlabel(r'$f\, \, [MHz]$')
# Für T/R
plt.ylabel(r'$\frac{T}{R} \,\, [dB]$')
plt.ylim(-50, -15)

# Für Phase
ax2 = ax.twinx()

plt.ylabel(r'$\phi \,\, [^\circ]$')
plt.ylim(-90, 90)
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------")

ax2.plot(np.linspace(1,500,400), np.zeros(400), 'b:')

print("-----------------------")


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
    ax.plot(np.array(data[1])/10**6, data[2], linestyle, label= r"{}  \n  $f_R = {} \, MHz$ ; $T_m = {} \,dB$".format(dateiname[11:-4:],round(minimumfreq,2),round(minimumTrans,2)))
    ax2.plot(np.array(data[1]) / 10 ** 6, data[3], linestyle+'.',
             label=r"{}  Phase".format(dateiname[11:-4:]))

for data in messdaten:
    plotdata(data[0], data[1])

#plt.legend(loc="best")
fig.legend(loc="center right",        # Position of the legend
           borderaxespad=0,         # Add little spacing around the legend box
           title="Legende:")

plt.subplots_adjust(right=0.7, left=0.04)

if willPrint:
    print("Speichere Daten als PNG")
    #plt.savefig(r'data\{}.eps'.format(titelName), format='eps')     # Um es später in LaTeX einzuarbeiten
    plt.savefig(r'data\{}.png'.format(titelName))

plt.show()

print("METHODE ENDET HIER")
