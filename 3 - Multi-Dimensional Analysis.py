import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyhere import here


titanic_df = pd.read_csv(r"C:\Users\MR ASIS\OneDrive\Documents\titanic_test.csv")
"""
Analyzes Titanic DataFrame data.

Args:
    titanic_df(pd.DataFrame): DataFrame contains Titanic passenger data.

Returns:
        First few rows.
        Data types of different columns and column names.
        Checking of missing data.
"""
print(titanic_df.head())
print(titanic_df.info())
print(titanic_df.columns)

# Checking of missing values
print(titanic_df.isna().any())
print(titanic_df.isna().sum())

def pivot_age_by_class_and_embarkation(titanic_df):
    """
    Creates a pivot table showing the average and median age of passengers grouped by 'Sex', 'Pclass', and 'Embarked'.

    Args:
        titanic_df(pd.DataFrame): DataFrame contains Titanic passenger data.

    Returns:
        pd.DataFrame: The pivot table with average and median grouped by "Sex", "Pclass", and "Embarked".
    """

pivot_table = titanic_df.pivot_table(index=["Sex", "Pclass", "Embarked"],
                                     values=["Age"],
                                     aggfunc=["mean", "median"],
                                     fill_value=0)
                     

print(pivot_table)

# Highlight anomalies
pivot_table["Age_Anomaly"] = ""
for index, row in pivot_table.iterrows():
    age_mean = row[("mean", "Age")]
    age_median = row[("median", "Age")]
    if age_mean > age_median:
        pivot_table.at[index, "Age_Anomaly"] = "High"
    else:
        pivot_table.at[index, "Age_Anomaly"] = "Low"
print(pivot_table)



