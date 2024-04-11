def secant_solver(func, x0, x1, tol=1e-6, max_iter=100):
    """
    Soluciona raízes de funções utilizando o método da secante.

    Args:
    func (callable): Função para a qual se deseja encontrar a raiz.
    x0 (float): Estimativa inicial da raiz.
    x1 (float): Segunda estimativa inicial da raiz.
    tol (float): Tolerância para a convergência.
    max_iter (int): Número máximo de iterações.

    Returns:
    float: Aproximação da raiz da função.

    Raises:
    ValueError: Se a função não cruzar o eixo x no intervalo [x0, x1].
    """

    # Iteração inicial
    f0, f1 = func(x0), func(x1)
    if f0 * f1 >= 0:
        raise ValueError("A função não cruza o eixo x no intervalo [x0, x1].")

    for i in range(max_iter):
        # Próxima estimativa da raiz
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        # Verificar convergência
        if abs(x2 - x1) < tol:
            return x2

        # Atualizar valores para próxima iteração
        x0, x1 = x1, x2
        f0, f1 = f1, func(x2)

    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# Exemplo de uso:
def f(x):
    return x**2 - 2

raiz_aproximada = secant_solver(f, 1, 2)
print("Raiz aproximada:", raiz_aproximada)
