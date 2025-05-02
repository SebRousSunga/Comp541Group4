import pandas as pd

print("Hello, world!")
allergyData = pd.read_csv("data/food-allergy-analysis-Zenodo.csv")
print(allergyData.describe())

