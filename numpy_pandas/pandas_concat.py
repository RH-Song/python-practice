import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

print df1
print df2
print df3

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print res

# join, ['inner','outer']
df4 = pd.DataFrame(np.ones((3,4))*1,index=[1,2,3],columns=['a','b','c','d'])
df5 = pd.DataFrame(np.ones((3,4))*2,index=[2,3,4],columns=['b','c','d','e'])

res = pd.concat([df4,df5],join='outer')
print res

res = pd.concat([df4,df5],axis=1,join_axes=[df4.index])
print res
res = pd.concat([df4,df5],join='inner',ignore_index=True)
print res

# append
res_app = df1.append(df2,ignore_index=True)
print res_app
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res_app_series = df1.append(s1,ignore_index=True)
print res_app_series
