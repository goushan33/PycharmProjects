import itertools
def compute_pi(n):
    naturals=itertools.count(1)
    ns=itertools.takewhile(lambda x:x<n,naturals)
    term=[]
    pi=0
    for i in ns:
        if i<=(2*n-1) and i%2:
            term.append(4/i)

    for i in range(len(term)):
        if i%2:
            pi+=term[i]
        else:
            pi+=-term[i]
    return pi
print(compute_pi(10))
print(compute_pi(100))
print(compute_pi(1000))
print(compute_pi(10000))
print(compute_pi(100000))
