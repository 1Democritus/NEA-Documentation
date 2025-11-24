import nn
import pandas

model = nn.DNN(columnSize = 2000, outputSize = 5)
df = pandas.read_csv("disease_diagnosis.csv")

#feature engineering
def OHElabel(value):
    conversionDict = {"Healthy": [1,0,0,0,0], "Bronchitis": [0,1,0,0,0], "Flu":[0,0,1,0,0], "Cold": [0,0,0,1,0], "Pneumonia": [0,0,0,0,1]}
    return np.array(conversionDict[value])
df["Diagnosis"] = df["Diagnosis"].apply(OHElabel)
