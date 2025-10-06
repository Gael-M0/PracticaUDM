#Hacer un xlsx en un csv
import pandas as pd
df = pd.read_excel(r"C:\Users\Usuario\Documents\GitHub\PracticaUDM\udemy\Python_DataScience\Prueba Santander.xlsx")
df.to_csv("Prueba Santander.csv", index=False)
