# -*- coding: utf-8 -*-
"""TimebasedIndexingAndResampling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Time-based Indexing and Resampling
import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=date_range)

# Resampling to find weekly sales
weekly_sales = df.resample('W').sum()

print('Weekly Sales:\n', weekly_sales)