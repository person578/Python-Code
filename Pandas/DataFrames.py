import pandas as pd
import numpy as np

data = {"Name": ["Ethan", "Ash", "John", "Tom"],
        "Age": [21, 27, 34, 40]}
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"])

# Add a new column
df["Job"] = ["Data Analyst", "Data Engineer", "Data Manager", "Sr. Software Engineer"]

# Add a new row
new_rows = pd.DataFrame([{"Name": "Alan", "Age": 43, "Job": "Sr. Software Architect"},
                               {"Name": "Jacob", "Age": 45, "Job": "Sr. Software Engineer"}], index=["Employee 5", "Employee 6"])
df = pd.concat([df, new_rows])

print(df)