import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data_transmission.csv", sep=",")

# The x axis are the same for the 3 experiments
x = data['lambda']
y_skim = data['T_skim_2ml']
y_half = data['T_half_full']
y_full = data['T_full']

plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission (%)")
plt.title("Absorption spectra")
plt.plot(x, y_full, label='whole milk (3.5 g/100 ml)')
plt.plot(x, y_half, label='half milk (1.5 g/100 ml)')
plt.plot(x, y_skim, label='skim milk (0.1 g/100 ml)')
plt.legend()
plt.axis([400, 900, 0, 200])
plt.show()

plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission (%)")
plt.title("Absorption spectra")
plt.plot(x, y_full, label='whole milk (3.5 g/100 ml)')
plt.plot(x, y_half, label='half milk (1.5 g/100 ml')
plt.legend()
plt.axis([400, 450, 0, 350])
plt.show()
