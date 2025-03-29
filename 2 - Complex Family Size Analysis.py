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

"""
Grouping Titanic DataFrame and creating new column.

Args:
    titanic_df(pd.DataFrame): DataFrame contains Titanic passenger data.

Returns:
        Groups the Titanic dataframe by "Pclass".
        New column "FamilySize" categorizing families into custom bins (e.g., "Solo", "Small", "Medium", "Large").
        Checking of new dataset.
"""
# Define family categories
fam_cat = {
  "Solo":[1, 1],
    "Small":[2, 4],
    "Medium":[5, 7],
    "Large":[8, 11]
    }


# Define a function to assign family categories
def assign_family_category(family_size):
    for category, (lower, upper) in fam_cat.items():
        if lower<= family_size <= upper:
            return category
        

# Calculate family size (including passenger themselves)
titanic_df["FamilySize"] = titanic_df["SibSp"] + titanic_df["Parch"] + 1

        
# Apply the function to create "FamilySize" column

titanic_df["FamilyCategory"] = titanic_df["FamilySize"].apply(assign_family_category)
titanic_df.to_csv("titanic_df_with_family_size.csv", index=False)
titanic_df_with_family_size = pd.read_csv("titanic_df_with_family_size.csv")
print(titanic_df_with_family_size.info())

# Create pivot table
pivot_table = titanic_df_with_family_size.pivot_table(index=["Pclass", "FamilyCategory"],
                                                      values=["Survived", "Fare"],
                                                      aggfunc={"Survived":"mean", "Fare":"mean"},
                                                      fill_value=0,
                                                      margins=True).reset_index()
pivot_table.columns = ["Pclass",
                       "FamilySize",
                       "Average_Fare",
                       "Suvival rate"]
                   
print(pivot_table)
