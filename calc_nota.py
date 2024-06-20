from media_notas import *
from soma_notas import *

print(f"{"*" * 10} CALCULADORA DE NOTAS {"*" * 10}")

try:
    print("""DESEJA UTILIZAR QUAL SISTEMA DE NOTAS:
        [1] - SOMA DE NOTAS
        [2] - MÉDIA DE NOTAS""")
    selecao = int(input("> "))

    if selecao == 1:
        soma()
    elif selecao == 2:
        media()
    else:
        print("Seleção inválida.")
except ValueError:
    print("Valor inválido. Programa encerrado.")
except ZeroDivisionError:
    print("A soma dos pesos não pode ser zero. Programa encerrado.")