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
trans = "\\transcriptions\\*"
eval = "\\eval\\*"

data = []

for session in range(1,sessions+1):
    local_path = path+str(session)+trans
    for name in glob.glob(local_path):
        for line in fileinput.input(name):
            d = line.split(" ", 2)
            d[len(d)-1] = d[len(d)-1].replace("\n", "")
            row = d[:]
            data.append(row)

df = pd.DataFrame(data, columns = ['Session_ID', 'Time_Record', 'Transcription'])

print(df.head())

print(df.tail())

print(df)

df.to_csv("data",index=True)