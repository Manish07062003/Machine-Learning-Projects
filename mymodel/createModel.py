import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

dataset = pd.read_csv("dataset.csv")
df = dataset.copy()

y = dataset['Profit']
x = dataset[['R&D Spend','Administration', 'Marketing Spend']]

state = dataset['State']
final_state = pd.get_dummies(state,drop_first=True)
x[["Florida","New York"]] = final_state

print(x)


model = LinearRegression()
model.fit(x,y)
joblib.dump(model,"Predict_Profit.model")