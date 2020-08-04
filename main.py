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
titelName = "Probenmessreihe C=4.7pF, N=8 Range 0-500 kombiniert 110-150 (25.06.2020) 280"
messdaten = [
#(r"30.04.2020\backgroundKrokparalell.txt", "r-."),
#(r"30.04.2020\backgroundKrokauseinander.txt", "g-."),
(r"25.06.2020\0.8isoSil8C4.7Range0-500.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13440.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13946.txt", "b-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500RundS14827.txt", "c-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S14260.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S12368.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13504.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500langS14541.txt", "b-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13911.txt", "c-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500langS12306.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13994.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13382.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500langS13372.txt", "b-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13406.txt", "c-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500kleinRundS14010.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13069.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500viertelS14675.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S12859.txt", "b-"),

(r"25.06.2020\0.8isoSil8C4.7Range0-500S13495.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13461.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13489.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range0-500S13498.txt", "b-"),

#(r"30.04.2020\nurkabel10cm.txt", "r-."),

(r"25.06.2020\0.8isoSil8C4.7Range110-150.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13440.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13946.txt", "b-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150RundS14827.txt", "c-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S14260.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S12368.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13504.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150langS14541.txt", "b-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13911.txt", "c-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150langS12306.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13994.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13382.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150langS13372.txt", "b-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13406.txt", "c-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150kleinRundS14010.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13069.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150viertelS14675.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S12859.txt", "b-"),

(r"25.06.2020\0.8isoSil8C4.7Range110-150S13495.txt", "y-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13461.txt", "r-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13489.txt", "g-"),
(r"25.06.2020\0.8isoSil8C4.7Range110-150S13498.txt", "b-"),
]

willPrint = False
#-----------------------------------------------------------------------------------------------------------------------
setTitle(titelName)

#for textData in messdaten:
#     plotData(textData[0], textData[1], fit=True)

#plotData(*(r"30.04.2020\nurkabel10cm.txt", "r-."))
#plotCombineData(messdaten[0][0], messdaten[1][0], messdaten[0][1], fit=True)

for i in range(0,22):
  plotCombineData(messdaten[i][0], messdaten[i+22][0], messdaten[i][1], fit=True)

#for i in range(0,5):
#  plotCombineData(messdaten[i+10][0], messdaten[i+15][0], messdaten[i+10][1], fit=False)

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
    plt.savefig(r'data\{}.pdf'.format(titelName))

print('Time: ', round(time.time() - now, 3), 's')
closeCSV()
plt.show()