# -*- coding: utf-8 -*-
from sympy import nsimplify,simplify, symbols, N,Rational,integrate, init_printing, latex, pprint, sqrt
from sympy.abc import y
from fractions import Fraction
import math
init_printing(use_latex="mathjax")
# para imprimir de la potencia más pequeña a la mas grande
#x = symbols('x',commutative=False)
def fact(n):
    f = 1.0
    for i in range(1,n+1):
        f*=i
    return f
s = "\\documentclass{article}\n"
s+= "\\usepackage{amsmath}"
s+= "\\usepackage{graphicx}"
s+= "\\usepackage[utf8]{inputenc}\n"
s+= "\\title{Aproximando $\\pi$}"
s+= "\\author{Fernando Gerardo Flores García}\n"
s+= "\\begin{document}\n"
s+= "\\maketitle\n"
s+= "\\section{Recordemos el teorema generalizado del binomio.}\n"
s+= "\\begin{align*}"
s+= "(y+x)^r = \\sum_{k=0}^{\\infty} \\binom{r}{k} y^{r-k}x^{k}\n"
s+= "\\end{align*}\n\\begin{center}\ndonde r es cualquier real y\n"
s+= "\\end{center}\n\\begin{align*}\n"
s+= "\\binom{r}{k}=\\frac{1}{k!}\\prod_{n=0}^{k-1}(r-n)\n"
s+= "\\end{align*}\n\\section{Ecuación de un circulo unitario}\n"
s+= "\\begin{align*}\nx^2+y^2=1\\\\\n"
s+= "\\end{align*}\n\\begin{center}\ndespejamos a y\n"
s+= "\\end{center}\n\\begin{align*}\ny=(1-x^2)^\\frac{1}{2}\n"
s+= "\\end{align*}\n"
s+= "Notamos que podemos usar el teorema, "
#***Menor complejidad al calcular el dividendo***
def pi_mc(n):
    global s
    s+= "apliquémoslo a los primeros 11 términos.\n"
    x = symbols('x',commutative=False)
    dividendo = Fraction(1,2)
    exp = Fraction(1,1)
    exp_l = Fraction(1,1)
    exp += Fraction(1,2)*y
    exp_l += Fraction(1,2)*x
    for i in range(n-1):
        print(i)
        pprint(str(dividendo)+"*"+str((Fraction(1,2) - Fraction(i+1,1))))
        pprint(Fraction(i+1,1))
        dividendo *= (Fraction(1,2) - (i+1))
        exp_l = exp_l + ((dividendo * x**(i+2))/Rational(fact(i+2)))
        exp = exp + ((dividendo * y**(i+2))/Rational(fact(i+2)))
    pprint(exp)
    s+= "\\section{Obetenemos los "+str(n+1)+" terminos de la expresión}\n"
    s+= "$(1+x)^{\\frac{1}{2}}=$ "
    s+= "$" +str(latex(exp_l)) +"$\n"
    #s+= str(latex(pow((1+x),Fraction(1,2)))) + "\n"
    exp = exp.subs(y,-y**2)
    exp_l = exp_l.subs(x,-x**2)
    s+= "\\section{Expresión substituyendo x por $-x^{2}$}\n"
    s+= "$(1-x^{2})^{\\frac{1}{2}}=$ "
    s+= "$"+str(latex(exp_l))+"$\n"
    s+= "\\section{Integrando de 0 a $\\frac{1}{2}$:}"
    s+= "Estámos integrando para calcular el área de 0 a $\\frac{1}{2}$ del circulo.\\\\ \n"
    s+= "$ \\int_{0}^{\\frac{1}{2}} (1-x^{2})^{\\frac{1}{2}} \\,dx = "
    s+= "\\int_{0}^{\\frac{1}{2}} "+str(latex(exp_l))+"\\,dx $\n"
    exp = integrate(exp,(y,0,Fraction(1,2)))
    #exp_l = integrate(simplify(exp_l),(x,0,Fraction(1,2)))
    s+= "\\subparagraph{Resultado}\n"
    s+= "\\includegraphics[width=0.5\\textwidth]{area_1.png}\n"
    s+= "\\begin{flushleft}\n"
    s+= "Sabemos que el área es $\\frac{\pi}{12} + \\frac{\\sqrt{3}}{8}$ entonces lo reemplazamos.\n"
    s+= "\\end{flushleft}\n\\begin{flushleft}\n"
    s+= "$\\frac{\\pi}{2}+\\frac{\\sqrt{3}}{8}= "+latex(exp)+"$\n"
    s+= "\\end{flushleft}\n"
    s+= "\\section{Despejando $\\pi$}\n"
    s+= "$\\pi="+"12["+str(latex(exp))+"-\\frac{\\sqrt{3}}{8}]$\n"
    print(exp_l)
    print(exp)
    exp += -sqrt(3)/8
    exp *= 12
    exp_l += -sqrt(3)/8
    exp_l *= 12
    s+= ", $\\pi="+str(latex(exp))+"$\n"
    s+= "\\section{Aproximación final con "+str(n+1)+" Términos: }\n"
    s+= str(N(exp,40))+"\n"
    return simplify(exp)
#hasta 46
#print(N(pi_menor_complejidad(100),160))
#print(s)
print(N(pi_mc(16),40))
s+= "\\end{document}"
print(s)
#pprint(integrate(exp,(x,0,Fraction(1,2))))
