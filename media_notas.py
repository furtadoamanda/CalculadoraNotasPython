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
