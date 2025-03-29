import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyhere import here


titanic_df = pd.read_csv(r"C:\Users\MR ASIS\OneDrive\Documents\titanic_train.csv")
"""
Analyzes Titanic train DataFrame.

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

def fare_range_analysis(titanic_df):
    """
    Fare Range analysis with Custom Bissing of titanic_df.

    Args:
    titanic_df contains titanic passengers' information.

    Returns:
    A DataFrame grouping by "FareRange" bins and "Sex" then
    calculation of mean, minimum, maximum, and standard deviation of "Age" as well survival rate.
    """

# Create custom fare bins using pd.qcut
titanic_df["FareRange"] = pd.qcut(titanic_df["Fare"], q=4)

# Group by FareRange bins and sex
grouped_titanic_df = titanic_df.groupby(["FareRange", "Sex"], observed=False)

# Calculate mean, min, max, std of Age and survival rate for each group
analysis_titanic_df = grouped_titanic_df.agg({
    "Age":["mean", "min", "max", "std"],
    "Survived":"mean"
    }).reset_index()
# 
analysis_titanic_df_cols = analysis_titanic_df.set_axis(["FareRange", "Sex", "Mean_Age", "Min_Age", "Max_Age", "Age_Std", "Mean_Survived"],
                                                        axis="columns"
                                                        )
                                                        

print(analysis_titanic_df_cols)

