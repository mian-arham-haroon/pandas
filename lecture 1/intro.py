import numpy as np
import pandas as pd

dis1={
    "name":['arham','haroon','ali','akhram'],
    "marks":[90,34,66,97],
    "city":['FSD','LHR','THO','GRO']
}
df=pd.DataFrame(dis1)
# df.to_csv('data.csv',index=False)
df.tail(1)
df.head(1)
print(df)









