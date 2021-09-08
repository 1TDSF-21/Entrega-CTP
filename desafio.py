def calcular_nota(cp1, cp2, cp3, sprint3, sprint4, semestre1):
    reprovado = False # Identifica se o aluno não possui chance de aprovação na disciplina
    aprovado = False # Identifica se o aluno foi aprovado na disciplina mesmo sem a nota da Global Solution
    media_semestre1 = semestre1 * 0.4 # O primeiro semestre equivale a 40% da nota anual

    # Calcula a média dos CPs + GS
    cps = [cp1, cp2, cp3]
    menor = min(cps)    
    index_menor = cps.index(menor)     
    cps.pop(index_menor)      # Exclui a menor nota de CP
    notas_cps = cps[0] + cps[1] + sprint3 + sprint4

    media_cps = round(((notas_cps/4)*0.4), 2) # Média dos cps + sprints do 2o semestre
    media_semestre2 = round(((6 - media_semestre1) / 0.6 ), 2) # Nota necessária para o 2o semestre
    nota_necessaria_GS = round(((media_semestre2 - media_cps) / 0.6), 2) # Nota necessária na GS para ser aprovado no 2o semestre
    

    if nota_necessaria_GS > 10:
        reprovado = True
    
    if media_semestre2  <= 4 and media_cps == 4:
        aprovado = True
        nota_necessaria_GS = 0
        
    elif media_semestre2 < 4:
        nota_necessaria_GS = 4 - media_cps
        
    return [nota_necessaria_GS, reprovado, aprovado]

print(calcular_nota(10, 10, 10, 10, 10, 10))