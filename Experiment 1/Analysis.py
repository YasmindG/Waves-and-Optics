import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

whole = pd.read_csv("Whole.csv", sep=",")
half  = pd.read_csv("Half.csv", sep=",")
skim  = pd.read_csv("Skim.csv", sep=",")

data = [whole, half, skim]
# The x axis are the same for the 3 experiments
x  = whole['wavelength']
y_data = []

for dat in data:
    y1 = dat['intensity1']
    y2 = dat['intensity2']
    y3 = dat['intensity3']
    
    y_temp = np.array([y1,y2,y3])
    y  = np.average(y_temp,axis=0)
    y_data.append(y)

plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.title("Emission spectra")
plt.plot(x, y_data[0], label='whole milk') 
plt.plot(x, y_data[1], label='half milk') 
plt.plot(x, y_data[2], label='skim milk') 
plt.legend()
plt.show()

# Trim the data sets such that the first peak will not be taken into account
skim_above_500 = skim[skim["wavelength"] > 500]
half_above_500 = half[half["wavelength"] > 500]
whole_above_500 = whole[whole["wavelength"] > 500]

# The x axis are the same for the 3 experiments
x500  = whole_above_500['wavelength']

column = skim_above_500["intensity1"]
max_index = column.idxmax()
print("peak for skim milk = ", skim_above_500.loc[max_index, "wavelength"])

column = half_above_500["intensity1"]
max_index = column.idxmax()
print("peak for half milk = ", half_above_500.loc[max_index, "wavelength"])

column = whole_above_500["intensity1"]
max_index = column.idxmax()
print("peak for whole milk = ", whole_above_500.loc[max_index, "wavelength"])

