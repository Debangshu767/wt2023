import numpy as np
import papnda as pd 
import matplotlib.pyplot as pyplot

#read csv file

df = pd.read_csv("dataset.csv")
print(df.head(10))

#find total number of runs kholi has scored
total_runs = df["Runs"].sum()
print(f"total runs by kholi in {no_of_matches} matches",total_runs)

#average runs
avg_runs = df["Runs"].mean()
print(f"average runs in {no_of_matches} is",avg_runs)

#number of mathces played at different positiosn
positiosns = df["pos"].unique()
print(positiosns.unique())

df["pos"] = df["pos"].map({
    3.0 : "Batting at 3",
    4.0 : "Batting  at 4",
    2.0 : "Batting at 2",
    1.0 : "Batting at 1",
    7.0 : "Batting at 7",
    5.0 : "Batting at 8",
    6.0 : "Batting at 6"

})

def show_pie_plot(df,key) :
    counts = df[key].value_counts()
    count_values = counts.value_counts
    count_labels = count.index

    fig = plt.figure(figsize=(10,7))
    plt.pie(count_values, labels = count_labels)
    plt.show()
    
