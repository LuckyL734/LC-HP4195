import matplotlib.pyplot as plt
import numpy as np
import math

R1 = 50
R2 = 50
C1 = 10**-10
L1 = 6.68*10**-6
param = {"R1": 50,
        "R2": 50,
        "C1": 10**-9,
        "L1":6.68*10**-6}

print(param["R1"], " Daten R1")

print("R1 = " , R1 , " , R2 = " , R2 , " , C1 = " , C1 , " , L1 = " , L1)

# t = np.arange(0, 5, 0.2)
# plt.plot(t, t, "r--", t, t**2, "bs", t, t*5, "g^")
# plt.axis([0,6,0,20])
# print(t)

# data = {"a": np.arange(50),
#         "c": np.random.randint(0,50,50),
#         "d": np.random.randn(50)}
# data["b"] = data["a"]+10* np.random.randn(50)
# data["d"] = np.abs(data["d"]) * 50
#
# plt.scatter("a", "b", c="c", s="d", data=data)
# plt.xlabel("entry a")
# plt.ylabel("entry b")

w = np.logspace(3.0, 9.0, num=1000)
# print("w = ", w)

#def Z(t):
#    return 1 / np.sqrt( R1**2 + 1/ (w**2*C1**2 + 1 / (R2**2 + w**2 * L1**2)) + 2*R1*R2 / (w**2 * C1**2 * (R2**2 + w**2 * L1**2) - 2 * w**2 * L1 * C1 + 1) )

def Z(t):
    return 1 / abs(R1 + 1/(1.j * w * C1 + 1 / (R2 + 1.j * w * L1) ) )

plt.figure(figsize=(13,7), facecolor="white")
plt.plot(w/(2*np.pi), Z(w), "r-")
plt.xscale("log")
plt.yscale("log")
plt.title('Simulation')


plt.show()
print("FERTIG")