import math
from lista1.questao1 import metodos

#
#



def funcao(x):
    return x*x*x - (2*x) + 2


def derivada_funcao(x):
    return 3*x*x - 2


def visualizar_metodo(metodo, resultado):
    aproximacao = resultado[0]
    zero_aproximado = resultado[1]
    iteracoes = resultado[2]
    erro = resultado[3]

    print(metodo, aproximacao, "\N{TAB}", zero_aproximado, "\N{TAB}\N{TAB}", iteracoes, "  \N{TAB} \N{TAB}", erro)


tolerancia = 1e-7

print("\N{TAB}   Metodo\N{TAB}\N{TAB}  ", "Aproximacao\N{TAB}\N{TAB}\N{TAB}", "F(Aproximacao)\N{TAB}\N{TAB}", "Iteracoes\N{TAB}\N{TAB}", "\N{TAB}Erro")
print("---------------------------------------------------------------------------------------------------------")

visualizar_metodo("\N{TAB}MNR:           ", metodos.newton(funcao, derivada_funcao, tolerancia, 1))
