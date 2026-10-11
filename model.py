import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Dataset load
data = {
    'Temperature': [28, 32, 18, 22, 30, 25, 20, 35, 28, 32],
    'Humidity': [80, 65, 75, 90, 85, 70, 95, 60, 75, 50],
    'Wind_Speed': [5, 8, 2, 4, 6, 7, 3, 9, 4, 1],
    'Weather': ['Rainy', 'Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Sunny', 'Cloudy']
}
df = pd.DataFrame(data)
print(df.columns.tolist())

X = df[["Temperature", "Humidity", "Wind_Speed"]]
y = df["Weather"]


dtc_model = DecisionTreeClassifier()
dtc_model.fit(X, y)

pickle.dump(dtc_model, open('dtc_model.pkl', 'wb'))
print("Model dumped and  Trained into pkl file")