# Example EDA steps on a CSV file (data.csv)
# Run: python task2_eda.py data.csv

import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def basic_report(df):
    print("Shape:", df.shape)
    print("\nColumns and dtypes:\n", df.dtypes)
    print("\nMissing values per column:\n", df.isnull().sum())
    print("\nNumeric description:\n", df.describe(include=[np.number]).T)
    print("\nTop value counts for object columns:")
    for col in df.select_dtypes(include=['object']).columns:
        print(f"\n{col}:\n", df[col].value_counts(dropna=False).head(10))

def correlation_analysis(df, figsize=(10,8)):
    numeric = df.select_dtypes(include=[np.number])
    corr = numeric.corr()
    print("\nCorrelation (top):\n", corr)
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation heatmap")
    plt.tight_layout()
    plt.show()

def detect_outliers_iqr(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr
    return df[(df[col] < low) | (df[col] > high)]

def main(path):
    df = pd.read_csv(path)
    basic_report(df)
    correlation_analysis(df)
    # Example visualizations:
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_cols:
        col = numeric_cols[0]
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

        plt.figure()
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
        plt.show()

    # Example grouping
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    if cat_cols and numeric_cols:
        cat = cat_cols[0]
        num = numeric_cols[0]
        print(f"\nGroup stats of {num} by {cat}:\n", df.groupby(cat)[num].describe().head())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task2_eda.py data.csv")
        sys.exit(1)
    main(sys.argv[1])