import pandas as pd

misDatos = pd.read_csv("Pokemon2.csv")
misDatos.drop(["#","Type 1","Type 2","Generation","Legendary"],axis=1,inplace=True)
print(misDatos)