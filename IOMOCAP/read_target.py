#IEMOCA
import numpy as np
import pandas as pd
import csv
import os
import glob
import fileinput

sessions = 5
session_prefix = "session0"
path = "iemocap\\"+session_prefix
eval = "\\eval\\*"

data = []

for session in range(1,sessions+1):
    local_path = path+str(session)+eval
    for name in glob.glob(local_path):
        for line in fileinput.input(name):
            if line[0] == "[":
                d = line.split("\t")[1:]
                e = d[2].replace("[", "").replace("]", "").replace("\n", "").replace(",", "").split(" ")[:]
                row = [d[0], d[1], e[0], e[1], e[2]]
                data.append(row)

df = pd.DataFrame(data, columns = ['Session_ID', 'Sentiment', 'Valence', 'Activation', 'Dominance'])

print(df.head())

print(df.tail())

print(df)

df.to_csv("target",index=False)