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

"""
Grouping Titanic DataFrame and creating new column.

Args:
    titanic_df(pd.DataFrame): DataFrame contains Titanic passenger data.

Returns:
        Groups the Titanic dataframe by "Pclass".
        New column "Age_Range" categorizing ages into custom bins (e.g., "Child", "Teen", "Adult", "Senior").
        Checking of new dataset.
"""
# Grouping by "Pclass"
titanic_df_pclass = titanic_df.groupby("Pclass")[["Age", "Fare"]].mean()
print(titanic_df_pclass)

print(titanic_df["Age"].max())

# Creating a new column "Age_Range"
dict_age_range = {
    "Child":[0, 12],
    "Teen":[13, 18],
    "Adult":[19, 45],
    "Senior":[46, 76]
    }

# Define a function to assign age ranges
def assign_age_range(age):
    for category, (lower, upper) in dict_age_range.items():
        if lower<= age <= upper:
            return category
        
# Apply the function to create "Age_Range" column

titanic_df["Age_Range"] = titanic_df["Age"].apply(assign_age_range)
titanic_df.to_csv("titanic_df_with_age_range.csv", index=False)
titanic_df_with_age_range = pd.read_csv("titanic_df_with_age_range.csv")
print(titanic_df_with_age_range.info())

def categorize_age_and_analyze_fare(titanic_df_with_age_range):
    """
    Analyzes Titanic passenger fares based on age ranges and passenger classes.

    Args:
        titanic_df_with_age_range (pd.DataFrame): DataFrame contains Titanic passenger data.

    Returns:
        pd.DataFrame: Summary table with count, average, and median fare for each
        age range within each passenger class.
    """

# Checking correct column names
if "Fare" not in titanic_df_with_age_range.columns:
    raise ValueError("Column Fare not found in the DataFrame.")

# Create a pivot table with descriptive statistics
summary_table = titanic_df_with_age_range.pivot_table(index=["Pclass", "Age_Range"],
                                                      values=["Fare"],
                                                      aggfunc=["count", "mean", "median"],
                                                      fill_value=0,
                                                      margins=True).reset_index()
summary_table.columns = ["Pclass",
                         "Age_Range",
                         "Passenger_count",
                         "Average_Fare",
                         "Median_Fare"]
                      
print(summary_table)

