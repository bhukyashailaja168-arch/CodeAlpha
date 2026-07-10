# Examples: bar chart, scatter plot with regression, interactive plotly chart
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Example dataset: use seaborn's tips dataset
df = sns.load_dataset("tips")

def static_charts(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x="day", data=df, order=df['day'].value_counts().index)
    plt.title("Number of bills per day")
    plt.show()

    plt.figure(figsize=(8,6))
    sns.scatterplot(x="total_bill", y="tip", hue="time", data=df)
    sns.regplot(x="total_bill", y="tip", data=df, scatter=False, color="black", truncate=True)
    plt.title("Tip vs Total bill with regression line")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.boxplot(x="day", y="total_bill", data=df)
    plt.title("Total bill by day")
    plt.show()

def interactive_chart(df):
    fig = px.scatter(df, x="total_bill", y="tip", color="time",
                     size="size", hover_data=["day"], title="Interactive Tip vs Bill")
    fig.show()

if __name__ == "__main__":
    static_charts(df)
    interactive_chart(df)