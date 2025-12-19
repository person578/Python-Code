import pandas as pd
import numpy as np

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

print(series[series >= 2000])

# A series is like a single column in excel

#data = np.array([100, 102, 104, 200, 202, 204])
# data = [100.1, 102.2, 104.3]
# data = ["A", "B", "C"]
# data = [True, False, True]

#series = pd.Series(data, index=["A", "B", "C", "D", "E", "F"])

#print(series[series < 200])