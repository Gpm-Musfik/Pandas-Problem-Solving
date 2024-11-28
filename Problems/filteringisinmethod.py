# -*- coding: utf-8 -*-
"""FilteringIsinMethod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Filtering with isin Method
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Filtering with isin
filtered_df = df[df['City'].isin(['NY', 'SF'])]

print('Filtered DataFrame with isin Method:\n', filtered_df)