import matplotlib.pyplot as plt
import numpy as np
import math
import time

now = time.time()

#import Testing
from dataProcessing import *

# Es gilt für die Daten: data[x][y]
# x gibt Zahl an: 0 - Nummer | 1 - Frequenz [Hz] | 2 - T/R [dB] | 3 - PHASE [deg]
# y gibt nummer der Mesung an (0-400)

# Farben in matplotlib: b ; g ; r ; c ; y ; m
# Linien in matplotlib: - ; -- ; -. ; :
# Marker in matplotlib: o ; s ; D ; ^ ; x ; * ; +
#-----------------------------------------------------------------------------------------------------------------------
# VARIABLEN ZUR SCHNELLEN AUSWERTUNG:
titelName = "Variation Proben C=1pF, N=8 Range 0-500"
messdaten = [
#(r"30.04.2020\backgroundKrokparalell.txt", "r-."),
#(r"30.04.2020\backgroundKrokauseinander.txt", "g-."),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange0-500.txt", "r-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange0-500S13440.txt", "g-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange0-500S13504.txt", "b-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange0-500S13489.txt", "c-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange0-500S13498.txt", "y-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange190-220.txt", "r-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange190-220S13440.txt", "g-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange190-220S13504.txt", "b-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange190-220S13489.txt", "c-"),
(r"15.05.2020\0.8isoSil4C4.7KeramikRange190-220S13498.txt", "y-"),
# (r"15.05.2020\0.8isoSil8C1KeramikRange0-500.txt", "r-"),
# (r"15.05.2020\0.8isoSil8C1KeramikRange0-500S13440.txt", "g-"),
# (r"15.05.2020\0.8isoSil8C1KeramikRange0-500S13504.txt", "b-"),
# (r"15.05.2020\0.8isoSil8C1KeramikRange0-500S13489.txt", "c-"),
# (r"15.05.2020\0.8isoSil8C1KeramikRange0-500S13498.txt", "y-"),
#(r"15.05.2020\0.8isoSil8C1KeramikRange0-500S13495.txt", "m-"),
#(r"15.05.2020\0.8isoSil8C1KeramikRange0-500S13461.txt", "r-."),
]

willPrint = False
#-----------------------------------------------------------------------------------------------------------------------
setTitle(titelName)

# for textData in messdaten:
#    plotData(textData[0], textData[1], fit=True)

#plotCombineData(messdaten[0][0], messdaten[1][0], messdaten[0][1], fit=True)

for i in range(0,5):
    plotCombineData(messdaten[i][0], messdaten[i+5][0], messdaten[i][1], fit=True)

#data = readData(textData[0])
#fitData(data)



#plt.legend(loc="best")
fig.legend(loc="center right",        # Position of the legend
           borderaxespad=3,           # Add little spacing around the legend box
           title="Legende:")

plt.subplots_adjust(right=0.7, left=0.04)

if willPrint:
    print("Speichere Daten als PNG")
    #plt.savefig(r'data\{}.eps'.format(titelName), format='eps')     # Um es später in LaTeX einzuarbeiten
    plt.savefig(r'data\{}.png'.format(titelName))

print('Time: ', round(time.time() - now, 3), 's')
plt.show()