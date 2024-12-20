# -*- coding: utf-8 -*-
"""MapForValueReplacement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Using map() for Value Replacement
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Department': ['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)

# Mapping departments to codes
department_map = {'HR': 1, 'IT': 2, 'Finance': 3}
df['Dept Code'] = df['Department'].map(department_map)

print('DataFrame with Mapped Values:\n', df)