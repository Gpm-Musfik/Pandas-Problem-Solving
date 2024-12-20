# -*- coding: utf-8 -*-
"""PivotingDataFrames.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Pivoting DataFrames
import pandas as pd

# Creating a DataFrame
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'City': ['NY', 'NY', 'LA', 'LA'],
        'Sales': [200, 250, 300, 400]}
df = pd.DataFrame(data)

# Pivoting the DataFrame
pivot_df = df.pivot(index='Date', columns='City', values='Sales')

print('Pivoted DataFrame:\n', pivot_df)

