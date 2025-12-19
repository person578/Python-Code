import pandas as pd
import numpy as np

data = {"Name": ["Ethan", "Ash", "John", "Tom"],
        "Age": [21, 27, 34, 40]}
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"])

# Add a new column
df["Job"] = ["Data Analyst", "Data Engineer", "Data Manager", "Software Engineer"]

print(df)