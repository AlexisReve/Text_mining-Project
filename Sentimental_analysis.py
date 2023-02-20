import pandas as pd

df_asterix = pd.read_csv("Tweet_Asterix.csv", sep = ";")

print(df_asterix["text"])
print(df_asterix.shape)
