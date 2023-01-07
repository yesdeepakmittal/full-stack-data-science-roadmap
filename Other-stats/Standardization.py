'''
    If the data is normally distributed, we can standardize it(mean=0,std=1)
'''

import numpy as np
mean = 10
std = 10

arr = np.random.normal(loc=mean,scale=std,size=100)
# print(arr)

def z(n):
    '''
    returns z-score for every value
    '''
    return (n - mean)/std

ans = np.vectorize(z)(arr)

'''
Mean should be approximately equal to 0
Std. should be approximately equal to 1
'''
print('mean:',ans.mean())
print('std:',ans.std())