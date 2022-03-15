import pandas as pd

df = pd.read_csv("data/allData.csv")
df["new_column"] = df["year"] + "- hello"
df.to_csv("allDataWDate.csv", index=False)
# import csv

# v = open('data/allData.csv')
# r = csv.reader(v)
# row0 = r.next()
# row0.append('calcualted air date')
# for item in r:
#     item.append(str(item[25]) + "-" + item[24])
    