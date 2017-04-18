import numpy as np
import pandas as pd

dates = pd.date_range('20170418',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print df

# comment or uncomment to see the output
# print df['A']
# print df.A

# slice
# print df[0:3]
# print df['20170418':'20170420']

# select by label:loc
# print df.loc['20170421']
# print df.loc[:,['A','B']]
# print df.loc['20170420',['A','B']

#select by position:iloc
# print df.iloc[3,1]
# print df.iloc[2:3,1:3]

# mixed selection:ix
# print df.ix[:3,['A','C']]

# Boolean indexing
# print df[df.A > 8]
# df.B[df.A > 8] = 200
# print df
df['F'] = np.nan
print df
# df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20170418',periods=6))
# print df

# drop or fill nan
df.isnull()
# print df.dropna(axis=1,how='any') # how = 'any' or 'all'
print df.fillna(value=0)
