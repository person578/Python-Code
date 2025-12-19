import pandas as pd
import numpy as np

data = {"Name": ["Ethan", "Ash", "John", "Tom"],
        "Age": [21, 27, 34, 40]}
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"])

print(df.iloc[1])