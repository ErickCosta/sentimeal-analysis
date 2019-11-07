# IEMOCA
import numpy as np
import pandas as pd
import csv
import os
import glob
import fileinput

local_path = "meld\\*"

data = []
i=0
for file in glob.glob(local_path):
    df = pd.read_csv(file, encoding='windows-1252')
    for index, line in df.iterrows():
        i += 1
        row = ['Sess' + str(line['Season']) + '_E' + str(line['Episode']) + '_ID' + str(i),
               '[' + str(line['StartTime']) + '-' + str(line['EndTime']) + ']:', line['Utterance'],
               line['Emotion'], line['Sentiment']]
        data.append(row)

df = pd.DataFrame(data, columns=['Session_ID', 'Time_Record', 'Transcription', 'Emotion', 'Sentiment'])

print(df.head())

print(df.tail())

print(df)

df.to_csv("data", index=False, encoding='windows-1252')
