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

def clean_and_analyze_embarkation(titanic_df):
    """
    Cleans and analyzes the embarkation data of titanic_df.

    Args:
    titanic_df contains titanic passengers' information.

    Returns:
    A DataFrame contains the survival rate, avarage fare for passenger
    embarking from each port, including count of passengers.
    """

# Remove unnecessary columns
clean_titanic_df = titanic_df.drop(columns=["Cabin", "Ticket"])

# Fill missing Embarked values with the most common port
clean_titanic_df["Embarked"].fillna(clean_titanic_df["Embarked"].mode()[0], inplace=True)

print(clean_titanic_df.head())
print(clean_titanic_df.columns)

# Group by Embarked and analyze survival rate and average fare
grouped_titanic_clean_df = clean_titanic_df.groupby("Embarked")[["Survived", "Fare"]].agg(
    count=("Survived", "count"),
    survival_rate=("Survived", "mean"),
    average_fare=("Fare", "mean"),
    )
print(grouped_titanic_clean_df)
