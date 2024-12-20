# -*- coding: utf-8 -*-
"""CreatingDummyVariables.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QtIsG_hUyQVIxCYot93A3DHS_wCilAat
"""

# Creating Dummy Variables
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Creating dummy variables
dummies = pd.get_dummies(df['City'], prefix='City')

print('Dummy Variables DataFrame:\n', dummies)