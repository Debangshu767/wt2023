import pandas as pd
df=pd.read_csv("dataset.csv")
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.shape)
print(df.describe())
print(df["Opposition"].describe())
print(df)
print(df)
print(df["Runs"].value_counts())

# slicing ,selecting,extracting
# new_df=df[["Runs","4s","6s","Opposition"]]
# print(new_df)
#print(new_df.describe())
# print(new_df.iloc[2:13]["Runs"])

# print(df["Opposition"]=="v Australia")
vs_aussies=df[df["Opposition"]=="v Australia"]
# print(vs_aussies.head(10))

# print(vs_aussies["Runs"].sum())
# vs_aussies=df["Runs"]>100
runs=vs_aussies[vs_aussies["Runs"]>=100]
print(runs)

def find_centuries(x):
    if x>=100:
        return "OG"
    else :
        return "NOOB"
df["Centuries"]=df["Runs"].apply(find_centuries)
print(df)