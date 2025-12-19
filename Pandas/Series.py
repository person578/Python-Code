import pandas as pd

# A series is like a single column in excel

data = [100, 102, 104, 200, 202, 204]
# data = [100.1, 102.2, 104.3]
# data = ["A", "B", "C"]
# data = [True, False, True]

series = pd.Series(data, index=["A", "B", "C", "D", "E", "F"])

print(series[series >= 200])