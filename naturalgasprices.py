#necessary libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#sets 'seaborn' style presets
plt.style.use("seaborn")

#grabs data, can be found in this repository
data = pd.read_csv("monthly.csv")
date = data["Month"]
prices = data["Price"]

#labels and executes
plt.ylabel("Price (USD)")
plt.title("Natural Gas Prices")
plt.plot(date,prices)
plt.show()
