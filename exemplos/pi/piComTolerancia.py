def calcula_pi(tol):
    """
    Calcula o número pi com a serie de Gregory-Leibnitz
    :param tol: a tolerancia
    :return: o pi e o erro
    """

    tolerancia = 0.01  # margem de erro especificada pelo usuario como "aceitavel"
    erro = 10000

    pi_novo = 4.0
    pi_velho = 4.0

    # valores iniciais da primeira iteracao
    numerador = -4  # -4(-1)^n vira -4
    denominador = 3.0  # 2n+1 vira 3

    while erro > tol:
        pi_novo = pi_velho + numerador / float(denominador)
        erro = abs(pi_novo - pi_velho)

        numerador *= -1
        denominador += 2.0
        pi_velho = pi_novo

    return pi_novo, erro


pi, e = calcula_pi(1e-3)
print(pi, e)

print(calcula_pi(1e-6))
