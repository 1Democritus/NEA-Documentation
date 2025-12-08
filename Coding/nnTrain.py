import nn
import numpy as np
import pandas


df = pandas.read_csv("disease_diagnosis.csv")

#convert label from qualitative to one-hot-encoding
def OHElabel(value):
    conversionDict = {"Healthy": [1,0,0,0,0], "Bronchitis": [0,1,0,0,0], "Flu":[0,0,1,0,0], "Cold": [0,0,0,1,0], "Pneumonia": [0,0,0,0,1]}
    return conversionDict[value]

def convertGender(value):
    return 0 if value == "Male" else 1

df[["Systolic_Pressure", "Diastolic_Pressure"]] = df["Blood_Pressure_mmHg"].str.split('/', n = 1, expand = True)
df["Gender"] = df["Gender"].apply(convertGender)
#combine symptom columns into 1 then separate into list
df["Symptoms"] = df[["Symptom_1", "Symptom_2", "Symptom_3"]].apply(lambda val: ",".join(val.values.astype(str)), axis = 1)
df["Symptoms"] = df["Symptoms"].apply(lambda val: val.split(","))
symptomList = ["Body ache", "Cough", "Shortness of breath", "Fatigue", "Fever", "Headache", "Runny nose", "Sore throat"]
for symptom in symptomList:
    df[symptom] = [[symptom]] * len(df)
    df[symptom] = df.apply(lambda row: int(row[symptom] in row["Symptoms"]), axis = 1)


df = df.drop(columns = ["Symptoms","Symptom_1", "Symptom_2", "Symptom_3", "Treatment_Plan", "Severity", "Blood_Pressure_mmHg"])
labels = np.stack(df["Diagnosis"].apply(OHElabel).values).T
features = df.drop(columns = ["Diagnosis"]).to_numpy(dtype = float).T
model = nn.DNN(learningRate = 0.01, columnSize = features.shape[0], outputSize = labels.shape[0])
predictorModel = nn.trainModel(model = model, epochCount = 200, label = labels, trainset = features)
