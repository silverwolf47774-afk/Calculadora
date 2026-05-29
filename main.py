import os
import time


def calculadora(num1: float, num2: float, operador: str) -> float:
    result = float("nan")

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '**':
        result = num1 ** num2
    elif operador == '%':
        result = num1 % num2

    return result


def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '**': lambda a, b: a ** b,
        '%': lambda a, b: a % b
    }

    return ops.get(operador, lambda a, b: float("nan"))(num1, num2)


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            print('Calculadora')
            print('----------------------------------\n')

            num1 = float(input("Introduza o primeiro número: "))
            num2 = float(input("Introduza o segundo número: "))

            print("\nOperações disponíveis: +  -  *  /  **  %")
            operador = input("Escolha a operação: ")

            resultado = calculadora(num1, num2, operador)

            print(f"\nResultado: {resultado:g}")

            continuar = input("\nDeseja continuar? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
