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
# # x=pd.read_csv('data.csv')
# v=x['name'][0]=50
# print(v)
# x.to_csv('data.csv',index=False)
# # x.index=['001','002','003','004'] 
# print(x)


# ser=pd.Series(np.random.rand(34))
# print(ser)

# print(type(ser))
new_df=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# x=new_df.head()
# print(x)
# print(new_df)
# v=type(new_df)
# print(v)
# z=new_df[0][0]=0.1
# print(z)
# u=new_df.dtypes
# print(u)

# print()
# # c=new_df.head()
# print(c)
# print(new_df.index)
# print(new_df.columns)
# print(new_df.to_numpy())

# print(new_df.sort_index(axis=0,ascending=False))

# print(type(new_df[0]))

# new_df2=new_df
# new_df2[0][0]=6767
# print(new_df2)
# new_df2=new_df.copy()
# new_df2[0][0]=676733
# new_df.loc[0,0]=0.22222
new_df.columns=list("ABCDE")
X=new_df.loc[[1,2],['B','C']]
# new_df.head(2)
print(X)