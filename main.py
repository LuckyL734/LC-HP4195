import matplotlib.pyplot as plt
import numpy as np
import math

#import Testing
from dataProcessing import *

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

titelName = "Variation von C und N bei 0.8isoSil + Samples 07.05  Range in f_R + Phase"

willPrint = True
#-----------------------------------------------------------------------------------------------------------------------
setTitle(titelName)

for data in messdaten:
    plotdata(data[0], data[1])

#plt.legend(loc="best")
fig.legend(loc="center right",        # Position of the legend
           borderaxespad=5,         # Add little spacing around the legend box
           title="Legende:")

plt.subplots_adjust(right=0.7, left=0.04)

if willPrint:
    print("Speichere Daten als PNG")
    #plt.savefig(r'data\{}.eps'.format(titelName), format='eps')     # Um es später in LaTeX einzuarbeiten
    plt.savefig(r'data\{}.png'.format(titelName))

plt.show()