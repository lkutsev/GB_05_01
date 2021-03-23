import functools
def i():
    return str(input('Input:'))

s = (lambda x:x.split(' '))('( 1 + 2 ) * 4 + 3')
#s = (lambda x:x.split(' '))(i())
print(s)
s1 = list(filter(lambda x:x in ('('),(s)))
print(s1)

def num_compare(x,y):
    return y - x

print(sorted([4, 43, 1, 22], key=functools.cmp_to_key(num_compare)))
