import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def solusi(data, waktu, kasus):
    # amplitudo
    def X(F0, k, m, ω, c):
        X = F0 / np.sqrt((k-m*ω**2)**2 + (c*ω)**2)
        return X

    # fase
    def ϕ(c, ω, k, m):
        ϕ = np.arctan(c*ω / (k-m*ω**2))
        return ϕ

    # amplitudo awal
    def X0(ζ, ωn, x0, v0, X, ϕ, ω, ωd):
        X0 = np.sqrt(((ζ*ωn*x0 + v0 + ζ*ωn*X*np.sin(ϕ)-X*ω*np.cos(ϕ))/ωd)**2 + (x0 + X * np.sin(ϕ))**2 )
        return X0

    # fase awal
    def ϕ0(ωd, x0, X, ϕ, ζ, ωn, v0, ω):
        ϕ0 = np.arctan(ωd*(x0 + X*np.sin(ϕ))/(ζ*ωn*x0 + v0 + ζ*ωn*X*np.sin(ϕ)-X*ω*np.cos(ϕ)))
        return ϕ0

    # solusi transient
    def xc(X0, ζ, ωn, t, ωd, ϕ0):
        xc = X0*np.exp(-ζ*ωn*t)*np.sin(ωd*t + ϕ0)
        return xc

    # solusi steady-state
    def xp(X, ω, t, ϕ):
        xp = X*np.sin(ω*t - ϕ)
        return xp

    # kecepatan awal
    v0 = 0
    # solusi partikuler
    X = -X(data.F0, data.k, data.m, data.ω, data.c) 
    ϕ =  ϕ(data.c, data.ω, data.k, data.m)
    xp = xp(X, data.ω, t, ϕ)
    # solusi transient
    v0 = 0
    X0 = X0(data.ζ, data.ωn, data.x0, v0, X, ϕ, data.ω, data.ωd)
    ϕ0 = ϕ0(data.ωd, data.x0, X, ϕ , data.ζ, data.ωn, v0, data.ω)
    xc = xc(X0, data.ζ, data.ωn, t, data.ωd, ϕ0)
    # solusi total
    xt = xp + xc
    
    # mencetak hasil pengolahan data
    print("Pada %s didapat:"%kasus)
    print("X = ", X, "\nϕ = ", ϕ, "\nX0 = ", X0, "\nϕ0 = ", ϕ0)

    # plotting
    plt.plot(t, xt, color="red", label="x") 
    plt.plot(t, xp, color="green", label="xp")
    plt.plot(t, xc, color="blue", linestyle=":", label="xc")
    plt.title("Grafik Amplitudo terhadap Waktu " + kasus)
    plt.ylabel("Amplitudo (m)")
    plt.xlabel("waktu (s)")
    plt.grid()
    plt.legend()
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.tight_layout()
    plt.show()

# data
data = pd.read_csv(r'C:\Users\thiof\Python\Learning\getaranterpaksa.csv')
data1 = data.iloc[0,:]
data2 = data.iloc[1,:]
data3 = data.iloc[2,:]
data4 = data.iloc[3,:]

# waktu
t = np.arange(0, 0.2, 0.0001)

# data 1
solusi1 = solusi(data=data1, waktu=t, kasus="Kasus 1")
# data 2
solusi2 = solusi(data=data2, waktu=t, kasus="Kasus 2")
# data 3
solusi3 = solusi(data=data3, waktu=t, kasus="Kasus 3")
# data 4
solusi4 = solusi(data=data4, waktu=t, kasus="Kasus 4")