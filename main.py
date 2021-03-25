#Не читать - еще не готово!!!
#1 2 + 4 × 3 +
#def pipeline(e, *functions):
#    for f in functions:
#        e = bind(e, f)
#    return e
#Теперь вместо
#bind(bind(bind(bind(unit(x), f1), f2), f3), f4)
#мы можем использовать следующее сокращение:
#pipeline(unit(x), f1, f2, f3, f4)
def i():
    return str(input('Input:'))


f = lambda x,y:x+y
s = (lambda x:x.split(' '))('1 2 + 4 × 3 +')
from functools import reduce
#s = (lambda x:x.split(' '))(i())
print(s)
s1 = list(filter(lambda x:x.isdigit() ,(s)))
print(s1)
def oper(value):
    return \
        {
            '+': lambda i,j: i+j,
            '-': lambda i,j: i-j,
            '*': lambda i,j: i*j
        }.get(value)
def calc():
print (oper('-')(1,5))

def num_compare(x,y):
    return y - x

#print(sorted([4, 43, 1, 22], key=functools.cmp_to_key(num_compare)))
import functools
lst = range(10)
f = lambda x, y: (x[0] + y, x[1]+[x[0] + y])
from functools import reduce
b =  reduce(f, lst, (0, []))
print (b)
print (str(f))