def dou(param):
    return 2*param

def tri(param):
    return 3*param

fns = [dou,tri]

for f in fns:
    print f(10)
