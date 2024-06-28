# Calculadora de Notas Python 📊🐍

Programa criado para praticar os conhecimentos em Python.  
Trata-se de uma aplicação que possibilita ao usuário calcular sua nota final em uma disciplina, de acordo com os sistemas de média ou de soma, sendo informado se foi aprovado ou reprovado.  
O programa é dividido em 3 arquivos, `calc_nota.py`, `media_notas.py`, `soma_notas.py`.

## Arquivo principal (calc_nota.py):

```python
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
```
No presente arquivo, é definido o core de funcionamento da aplicação. De início, são importados os conteúdos integrais dos demais arquivos.  
Após, é impressa uma mensagem introdutória, seguida pelo bloco try.  
O bloco try é definido para que o programa não quebre caso ocorra uma das exceções definidas, explicadas mais a frente.  
De início, é exibido o menu principal ao usuário, para que ele selecione se deseja utilizar o sistema de soma ou o sistema de média. De acordo com a seleção feita pelo usuário, o programa chama a função `soma()` ou a função `media()`, definidas nos arquivos apartados. Se o usuário inserir um número diferente dos exibidos no menu, é exibida uma mensação de selação inválida, encerrando o programa.  
_**Exceções:**_ O programa definide duas exceções, a 'ValueError' e a 'ZeroDivisionError'. Se, no curso da execução do programa, algum dos dois erros for encontrado, o programa se encerra exibindo as mensagens definidas em cada exceção, não gerando um encerramento bruto e desagradável visualmente.  

## media_notas.py:
No escopo do arquivo `media_notas.py`, é definida a função `media()`, executada caso o usuário deseje utilizar o sistema de médias para cálculo de sua nota.
```python
def media():
    disciplina = input("Nome da disciplina: ")
    atividades = int(input("Número de atividades da disciplina: "))
    total_notas = 0
    total_pesos = 0

    for i in range(atividades):
        nota = float(input("Nota da atividade: "))
        peso = float(input("Peso da atividade: "))
        total_atividade = nota * peso
        total_notas += total_atividade
        total_pesos += peso

    media = total_notas / total_pesos
    
    if media >= 60:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
    
    print(f"Sua média final na disciplina {disciplina.title()} é: {media} \nVocê foi {situacao}")

```
Inicialmente, é solicitado ao usuário que indique o nome da disciplina e o número de atividades (provas, trabalhos, seminários, etc). As variáveis 'total_notas' e 'total_pesos' são inicialmente definidas como 0.  
É feita uma iteração pelo número de atividades indicadas pelo usuário, sendo, a cada iteração, solicitada a nota da atividade e seu peso na média geral.  
OBS: se a disciplina não utiliza pesos diversos para cada uma de suas atividades, os pesos são sempre 1.  
Em um sistema de média ponderada, cada atividade tem sua nota final baseada na nota obtida multiplicada pelo seu peso. Essas notas são somadas e divididas pela soma dos pesos para que se tenha a média geral.  
Calculada a média, tendo como base um sistema em que a nota necessária para aprovação é 60 pontos, se a média for maior ou igual a 60, a variável 'situacao' é definida como "APROVADO", ao passo que se for menor do que 60 será "REPROVADO".  
Por fim, é exibida uma mensagem final ao usuário informando sua média final na disciplina, bem como se está aprovado ou reprovado.

## soma_notas.py:
O sistema de somas tem seu funcionamento muito semelhante ao de média, porém mais simples.
```python
def soma():
    disciplina = input("Nome da disciplina: ")
    atividades = int(input("Número de atividades da disciplina: "))
    soma_notas = 0

    for i in range(atividades):
        nota = float(input("Nota da atividade: "))
        soma_notas += nota

    if soma_notas >= 60:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    print(f"Sua nota final na disciplina {disciplina.title()} é: {soma_notas} \nVocê foi {situacao}")

```
A função `soma()`, assim como a função `media()`, pede ao usuário o nome da disciplina e o número de atividades, fazendo uma iteração para cada atividade, em que é informada pelo usuário a nota para cada atividade.  
As notas são somadas e agrupadas na variável 'soma_notas'.  
Se a soma for maior do que 60, o aluno está aprovado, se for menor, reprovado.  
Da mesma forma que na função `media()`, é exibida uma mensagem final ao usuário informando sua nota final e sua situação.