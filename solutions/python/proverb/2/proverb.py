def proverb(*args,**kwargs):
    res = []
    for i in range(len(args)-1):
        res += [f'For want of a {args[i]} the {args[i+1]} was lost.']
    if args and bool(*kwargs.values()): 
        res += [f'And all for the want of a {kwargs.popitem()[1]} {args[0]}.']
    elif args: res += [f'And all for the want of a {args[0]}.']
    return res
