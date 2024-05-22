import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/Users/nikhilnaveen/Desktop/Learning/Assignments/LendingClubCaseStudy/loan.csv')

df_filtered = df[~df['loan_status'].str.contains('Current')]
print(df_filtered.head())
print(df_filtered.shape[0]-1)

null_value_mean = 100*df_filtered.isnull().mean()
columns_to_discard = null_value_mean[null_value_mean >50].index

df_new = df_filtered.drop(columns=columns_to_discard, axis=1)
print(df_new.head())
print(df_new.shape[0]-1)

df_new.to_excel('/Users/nikhilnaveen/Desktop/Learning/Assignments/LendingClubCaseStudy/loan_cleansed.xlsx', sheet_name='Sheet1', index=False)
