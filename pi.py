from sympy import symbols, N,Rational,integrate, init_printing, latex, pprint, sqrt
from sympy.abc import x
from fractions import Fraction
import math
init_printing(use_latex="mathjax")
# para imprimir de la potencia mas pequena a la mas grande
#x = symbols('x',commutative=False)
def fact(n):
    f = 1.0
    for i in range(1,n+1):
        f*=i
    return f
def pi(n):
    exp = 0
    for i in range(n+1):
        dividendo = Fraction(1,1)
        for j in range(i):
            dividendo *= Fraction(1,2) - j
        exp += (dividendo * x**i)/Rational(fact(i))
    exp = exp.subs(x,-x**2)
    exp = integrate(exp,(x,0,Fraction(1,2)))
    exp += -sqrt(3)/8
    exp *= 12
    return exp
#***Menor complejidad al calcular el dividendo***
def pi_mc(n):
    dividendo = Fraction(1,1)
    exp = dividendo
    for i in range(n):
        dividendo *= Fraction(1,2) - i
        exp = exp + ((dividendo * x**(i+1))/Rational(fact(i+1)))
    exp = exp.subs(x,-x**2)
    exp = integrate(exp,(x,0,Fraction(1,2)))
    #print(latex(integrate(exp,(x,0,Fraction(1,2)))))
    exp += -sqrt(3)/8
    exp *= 12
    return exp
#hasta 46
#print(N(pi_menor_complejidad(100),160))
print(N(pi(46),160))
#pprint(integrate(exp,(x,0,Fraction(1,2))))
