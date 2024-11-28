# -*- coding: utf-8 -*-
"""FunctionsGroupedData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Applying Functions to Grouped Data
import pandas as pd

# Creating a DataFrame
data = {'Team': ['A', 'A', 'B', 'B', 'C'], 'Points': [10, 15, 20, 25, 30]}
df = pd.DataFrame(data)

# Applying a function to grouped data
grouped_df = df.groupby('Team')['Points'].transform(lambda x: x / x.max())

print('DataFrame with Applied Functions to Grouped Data:\n', df)