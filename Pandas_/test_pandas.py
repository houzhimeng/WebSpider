import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
#

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]), 'F' : 'foo' })
dates = pd.date_range('20130101', periods=6)
print(df2.head(1))
print(df2.tail(2))


