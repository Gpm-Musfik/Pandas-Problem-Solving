# -*- coding: utf-8 -*-
"""QueryMethodForConditionalFiltering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Query Method for Conditional Filtering
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 60]}
df = pd.DataFrame(data)

# Using query for filtering
filtered_df = df.query('Score > 80')

print('Filtered DataFrame using query:\n', filtered_df)