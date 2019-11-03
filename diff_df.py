'''
Find the differences between two dataframes using Pandas

Pitfalls :
   1. check if there are any duplicates on keys.
   2. check if keys have the types
'''
import pandas as pd

leftDf = pd.DataFrame({'City': ['New York', 'Chicago', 'Tokyo', 'Paris', 'New Delhi'],
                    'Temp': [59, 29, 73, 56, 48]})

rightDf = pd.DataFrame({'City': ['London', 'New York', 'Tokyo', 'New Delhi', 'Paris'],
                    'Temp': [55, 55, 73, 85, 56]})

print leftDf
print rightDf

print pd.merge(leftDf, rightDf, left_on='City', right_on='City',how = 'outer',indicator=True)
result = pd.merge(leftDf, rightDf, left_on='City', right_on='City',how = 'outer',indicator=True).loc[lambda x : x['_merge']=='right_only']
result = pd.merge(leftDf, rightDf, left_on='City', right_on='City',how = 'outer',indicator=True).loc[lambda x : x['_merge']!='both']
print '\nresult:'
print result

