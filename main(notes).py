import os
import time


# ==================================================================================================================
# Criar um repositorio do GitHub clonado, realizando os seguintes passos:
# 1º Aceder o GitHub Desktop
#
# 2º Com o link enviado pelo formador, clonar o repositorio no GitHub Desktop e o respetivo fork.
#	2.1 - O programa é uma calculadora https://github.com/cbarata-formador/Calculadora.git
#
# 3º Abrir o repositório com o VSCode
#
# 4º Terminar a implementação da calculadora
#	4.1º Instruções: no bloco principal deverão implementar a solicitação de 2 numeros (float) ao utilizador
#  e o tipo de operação a realizar.
#
#		Para o calculo das operações deverão completar a função calculadora() já existente no repositório e 
# implementar uma segunda função com uma abordagem interna diferente mas com a mesma assinatura (mesmos 
# parâmetros e mesmo tipo de retorno).
#
#		As funções deverão devolver o mesmo resultado, quem utilizar o vosso repositório pode optar por que 
# função utilizar.
#
#		Após exibição do resultado deverão perguntar ao utilizador se deseja continuar a efetuar mais operações.
#
#		As operações a implementar serão a soma, subtração, divisão, multiplicação, exponenciação e o módulo 
# (resto da divisão inteira)
#
# 5º Efetuar as alterações necessárias fazendo vários commits e pushs.
#
# 6º Ir ao github verificar as alterações.
#
# 7º Partilhar com o formador o link do repositorio criado.
#
# ==================================================================================================================


# =========================================================
# FUNÇÃO 1: CALCULADORA (estrutura clássica com if/elif)
# =========================================================
def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Calculadora básica usando estrutura condicional.

    Parâmetros:
    - num1: primeiro número (float)
    - num2: segundo número (float)
    - operador: símbolo da operação (+, -, *, /, **, %)

    Retorno:
    - resultado da operação ou NaN se operador inválido
    """

    # Valor padrão caso o operador seja inválido
    result = float("nan")

    # Soma
    if operador == '+':
        result = num1 + num2

    # Subtração
    elif operador == '-':
        result = num1 - num2

    # Multiplicação
    elif operador == '*':
        result = num1 * num2

    # Divisão
    elif operador == '/':
        result = num1 / num2

    # Exponenciação
    elif operador == '**':
        result = num1 ** num2

    # Módulo (resto da divisão)
    elif operador == '%':
        result = num1 % num2

    return result


# =========================================================
# FUNÇÃO 2: CALCULADORA (versão alternativa com dicionário)
# =========================================================
def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    """
    Versão alternativa da calculadora usando dicionário de funções (mapa de operações).
    Mesma assinatura e mesmo resultado da função calculadora().
    """

    # Mapeamento de operadores para funções lambda
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '**': lambda a, b: a ** b,
        '%': lambda a, b: a % b
    }

    # get() evita erro caso operador não exista
    # retorna NaN se operação inválida
    return ops.get(operador, lambda a, b: float("nan"))(num1, num2)


# =========================================================
# BLOCO PRINCIPAL (EXECUÇÃO DO PROGRAMA)
# =========================================================
if __name__ == "__main__":

    # Loop principal da calculadora (continua até o utilizador sair)
    while True:

        # Limpa o terminal (Windows ou Linux/Mac)
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            print('Calculadora')
            print('----------------------------------\n')

            # Entrada de dados do utilizador
            num1 = float(input("Introduza o primeiro número: "))
            num2 = float(input("Introduza o segundo número: "))

            # Escolha da operação
            print("\nOperações disponíveis: +  -  *  /  **  %")
            operador = input("Escolha a operação: ")

            # Chamada da função principal
            resultado = calculadora(num1, num2, operador)

            # Resultado formatado (remove .0 quando possível)
            print(f"\nResultado: {resultado:g}")

            # Pergunta se quer continuar
            continuar = input("\nDeseja continuar? (s/n): ").lower()

            if continuar != 's':
                break

        # Erro de conversão (ex: letras em vez de números)
        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        # Erro de divisão por zero
        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    # Mensagem final ao sair do programa
    print('\nVolte sempre!\n')