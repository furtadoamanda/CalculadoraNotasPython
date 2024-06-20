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
