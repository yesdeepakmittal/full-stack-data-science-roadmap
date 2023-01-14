def fn(*args, **kwargs):
    '''
        args: return tuple
        kwargs: return dictionary
    '''
    print('args: ', args)
    print('kwargs: ', kwargs)

print(fn(2,4,x=1,y=2))

''' Output:
    args:  (2, 4)
    kwargs:  {'x': 1, 'y': 2}
'''

def calculte_sum(*args):
    s = 0
    for ele in args:
        s += ele
    return s

print('Sum:',calculte_sum(1,2,3,4,5))

''' Output:
    Sum: 15
'''