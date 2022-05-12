N = 100000  # numero de iteracoes para calcular pi
pi = 4.0

# valores iniciais da primeira iteracao
numerador = -4     # -4(-1)^n vira -4
denominador = 3.0  # 2n+1 vira 3

for i in range(1, N):
    pi += numerador / float(denominador)

    numerador *= -1
    denominador += 2.0

    print(i, pi)
