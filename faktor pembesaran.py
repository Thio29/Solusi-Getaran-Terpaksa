import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rasio(data, w):
    X = data.F0 / np.sqrt((data.k-data.m*data.ω**2)**2 + (data.c*data.ω)**2)
    A = X / data.δ
    f = data.ω / data.ωn
    ω = np.arange(0, w, 0.1) / data.ωn
    r = 1 / np.sqrt((1-(ω)**2)**2 + (2*data.ζ*(ω)))
    return f, A, ω, r

# data
data = pd.read_csv(r'C:\Users\thiof\Python\Learning\getaranterpaksa.csv')
data1 = data.iloc[0,:]
data2 = data.iloc[1,:]
data3 = data.iloc[2,:]
data4 = data.iloc[3,:]

# waktu
t = np.arange(0, 0.2, 0.0001)

# data 1
x1, y1, ω1, r1 = rasio(data1, 200)
plt.plot(ω1, r1, color="C0")
# data 2
x2, y2, ω2, r2 = rasio(data2, 100)
plt.plot(ω2, r2, color="C1" )
# data 3
x3, y3, ω3, r3 = rasio(data3, 200)
plt.plot(ω3[r3<6], r3[r3<6], color="C2")
# data 4
x4, y4, ω4, r4 = rasio(data4, 400)
plt.plot(ω4[r4<6], r4[r4<6], color="C3")
plt.plot(x1, y1, "o", label = "Kasus 1 (ζ=%.2f)" %(data1.ζ), color="C0")
plt.plot(x2, y2, "o", label = "Kasus 2 (ζ=%.2f)" %(data2.ζ), color="C1")
plt.plot(x3, y3, "o", label = "Kasus 3 (ζ=%.2f)" %(data3.ζ), color="C2")
plt.plot(x4, y4, "o", label = "Kasus 4 (ζ=%.2f)" %(data4.ζ), color="C3")
plt.text(x1, y1, '(%.2f, %.2f)' %(x1, y1))
plt.text(x2, y2, '(%.2f, %.2f)' %(x2, y2))
plt.text(x3, y3, '(%.2f, %.2f)' %(x3, y3))
plt.text(x4, y4, '(%.2f, %.2f)' %(x4, y4))
plt.axvline(1, linestyle=":",color="black")
plt.ylim(top=2.5)
plt.title("Grafik Rasio Perpindahan Terhadap Rasio Frekuensi")
plt.xlabel("ω / ωn")
plt.ylabel("X / δst")
plt.legend()
plt.tight_layout()
plt.show()
