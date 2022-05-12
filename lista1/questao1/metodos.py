import math


def bissecao(funcao, tolerancia, inicio_intervalo, final_intervalo):
    aproximacao_nova = 0
    erro = 10 * tolerancia

    aproximacao_anterior = final_intervalo
    iteracoes=0
    while erro > tolerancia:
        ponto_medio = (final_intervalo + inicio_intervalo) / 2

        aproximacao_nova = ponto_medio

        if funcao(aproximacao_nova) == 0:
            return aproximacao_nova

        if funcao(aproximacao_nova) * funcao(inicio_intervalo) < 0:
            final_intervalo = aproximacao_nova
        else:
            inicio_intervalo = aproximacao_nova

        erro = abs(aproximacao_nova - aproximacao_anterior)
        aproximacao_anterior = aproximacao_nova
        iteracoes += 1

    return aproximacao_nova, math.fabs(funcao(aproximacao_nova)), iteracoes, erro


def falsa_posicao(funcao, tolerancia, inicio_intervalo, final_intervalo):
    aproximacao_nova = 0
    erro = 10 * tolerancia

    aproximacao_anterior = final_intervalo
    iteracoes = 0
    while erro > tolerancia:
        numerador = final_intervalo*funcao(final_intervalo) - inicio_intervalo*funcao(inicio_intervalo)
        denominador = funcao(final_intervalo) - funcao(inicio_intervalo)
        ponto_medio = float(numerador) / float(denominador)

        aproximacao_nova = ponto_medio

        if funcao(aproximacao_nova) == 0:
            return aproximacao_nova

        if funcao(aproximacao_nova) * funcao(inicio_intervalo) < 0:
            final_intervalo = aproximacao_nova
        else:
            inicio_intervalo = aproximacao_nova

        erro = abs(aproximacao_nova - aproximacao_anterior)
        aproximacao_anterior = aproximacao_nova
        iteracoes += 1

    return aproximacao_nova,  math.fabs(funcao(aproximacao_nova)), iteracoes, erro


def newton(funcao, derivada_funcao, tolerancia, chute):
    erro = 10 * tolerancia

    aproximacao_nova = chute
    aproximacao_anterior = chute
    iteracoes = 0
    while erro > tolerancia:
        aproximacao_nova = funcao_newton(funcao, derivada_funcao, aproximacao_anterior)
        erro = abs(aproximacao_nova - aproximacao_anterior)
        aproximacao_anterior = aproximacao_nova
        iteracoes += 1

    return aproximacao_nova,  math.fabs(funcao(aproximacao_nova)), iteracoes, erro


def funcao_newton(funcao, derivada_funcao, aproximacao_anterior):
    return aproximacao_anterior - funcao(aproximacao_anterior) / derivada_funcao(aproximacao_anterior)


def secante(funcao, aproximacao_anterior, aproximacao_nova, tolerancia):
    assert tolerancia > 0, "tol deve ser maior que zero"

    erro = math.fabs(aproximacao_nova - aproximacao_anterior)
    iteracoes = 0
    while erro > tolerancia:
        f0 = funcao(aproximacao_anterior)
        f1 = funcao(aproximacao_nova)
        p2 = aproximacao_nova - f1 * (aproximacao_nova - aproximacao_anterior) / (f1 - f0)

        aproximacao_anterior = aproximacao_nova
        aproximacao_nova = p2
        erro = math.fabs(aproximacao_nova - aproximacao_anterior)
        iteracoes += 1

    return aproximacao_nova,  math.fabs(funcao(aproximacao_nova)),  iteracoes, erro
