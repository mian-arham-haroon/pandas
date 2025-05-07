import numpy as np
import pandas as pd

dis1={
    "name":['arham','haroon','ali','akhram'],
    "marks":[90,34,66,97],
    "city":['FSD','LHR','THO','GRO']
}
df=pd.DataFrame(dis1)
# df.to_csv('data.csv',index=False)
# print(df.tail(1))
# print(df.head(1))
# print(df.describe())
x=pd.read_csv('data.csv')
v=x['name'][0]=50
print(v)
x.to_csv('data.csv',index=False)
# x.index=['001','002','003','004'] 
print(x)

