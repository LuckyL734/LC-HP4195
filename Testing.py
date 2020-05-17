import os

dateiname = r"C:\Users\maxkr_000\Desktop\Bachelorarbeit Stuffs\Messdaten\24.04.2020\blankSil4C4.7Range0-500.txt"

print(dateiname)
print(os.getcwd())

open(dateiname)

se = "              0.1m"

se = list(se)

se.remove(" ")
newSe = ""
for x in se:
    print(x)
    if x != " " and x != "m":
        print("TRUE")
        newSe += x
    if x == "m":
        newSe += "*0.001"



print(se)
print(eval(newSe))

test = " 00000.01  "

print(test)
print(eval(test))