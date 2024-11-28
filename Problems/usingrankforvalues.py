# -*- coding: utf-8 -*-
"""UsingRankForValues.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Using Rank to Rank Values
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 90, 78, 92]}
df = pd.DataFrame(data)

# Ranking scores in descending order
df['Rank'] = df['Score'].rank(ascending=False)

print('DataFrame with Ranked Scores:\n', df)