import nn
import pandas

model = nn.DNN(columnSize = 2000, outputSize = 5)
df = pandas.read_csv("disease_diagnosis.csv")
