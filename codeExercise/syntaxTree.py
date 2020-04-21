Num = lambda env,n : n
Val = lambda env,x : env[x]
Add = lambda env,a,b : _eval(env,a)+_eval(env,b)
Mul = lambda env,a,b : _eval(env,a)*_eval(env,b)

_eval = lambda env,expr : expr[0](env,*expr[1:])

env = {'a':3,'b':6}
tree = (Add,(Val,'a'),
        (Mul,(Num,5),(Val,'b'))
        )
print(_eval(env,(Val,'a')))
print(_eval(env,(Num,5)))
print(Num(env,5))
print(_eval(env,tree))