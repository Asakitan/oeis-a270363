from fractions import Fraction
from math import comb
import sympy as sp

t,N=sp.symbols("t N")
x=t/(1+t)**2
E=lambda f: sp.factor(x*sp.diff(f,t)/sp.diff(x,t))
F=sp.factor(sp.diff(x*x*(1+t),t)/sp.diff(x,t)/(1-x*x*(1+t)))
p=N*(7*N**2-17*N-2)
q=-35*N**3+99*N**2+20*N-120
r=2*(2*N-5)*(7*N**2-3*N-12)
cs=[p,q,r,p,-r]
res=0
for j,c in enumerate(cs):
    v=x**j*F
    for h in range(4):
        res+=sp.expand(c).coeff(N,h)*v
        if h<3:
            v=E(v)
assert sp.factor(res)==sp.factor(-24*x+24*x*x+126*x**3)
a=[0]+[(n+1)*sum(Fraction(comb(2*n-3*k-2,n-k-1),n-k) for k in range((n-1)//2+1))
       for n in range(1,24)]
assert a[:5]==[0,2,3,10,30]
for n in range(4,24):
    assert sum(c.subs(N,n)*a[n-j] for j,c in enumerate(cs))==0
print("Exact rational differential identity passed; defining sums verified at n=0..23.")
