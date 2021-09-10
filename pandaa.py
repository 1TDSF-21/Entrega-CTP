# primeira coisa, instalar openpyxl e o pandas se não tiver
import pandas as pd

sheet = pd.read_excel(
    r"notas_planilha_modelo.xlsx", skiprows=(0, 1)
)  # pegar o caminho do seu pc

aprovado = False
reprovado = False

# teste de func
def calcular_nota(x, showPrint=True):

    n1 = sheet["checkpoint1"][x]
    n2 = sheet["checkpoint2"][x]
    n3 = sheet["checkpoint3"][x]
    n4 = sheet["Challenge Sprint 3"][x]
    n5 = sheet["Challenge Sprint 4"][x]
    s1 = sheet["Semestre_1"][x]

    reprovado = False
    aprovado = False  # Identifica se o aluno foi aprovado na disciplina mesmo sem a nota da Global Solution

    media_s1 = s1 * 0.4  # O primeiro semestre equivale a 40 % da nota anual
    # calcula média cps + gs
    cps = [n1, n2, n3]
    menor = min(cps)
    index_menor = cps.index(menor)
    cps.pop(index_menor)  # Exclui a menor nota de CP
    notas = cps[0] + cps[1] + n4 + n5

    media_cp = round((cps[0] + cps[1]) / 2)
    media_ch = round((n4 + n5) / 2)
    media_cp_ch = round(
        ((notas / 4) * 0.4), 2
    )  # Média dos cps + sprints do 2o semestre
    media_s2 = round(((6 - media_s1) / 0.6), 2)  # Nota necessária para o 2o semestre
    nota_necessaria_GS = round(
        ((media_s2 - media_cp_ch) / 0.6), 2
    )  # Nota necessária na GS para ser aprovado no 2o semestre

    if nota_necessaria_GS > 10:
        reprovado = True

    if media_s2 <= 4 and media_cp_ch == 4:
        aprovado = True
        nota_necessaria_GS = 0

    elif media_s2 < 4:
        nota_necessaria_GS = 4 - media_cp_ch

    if showPrint:
        print(
            "\n\n",
            sheet["RM"][x],
            sheet["Nome"][x],
            "\nDisciplina: Computacional Thinking Using Python\nSemestre 1: ",
            sheet["Semestre_1"][x],
            "\n\t\tSemestre 2\nCheckpoints (média): ",
            media_cp,
            "\nChallenge: ",
            media_ch,
            "\n\nNota mínima na Global Solution para aprovação: ",
            nota_necessaria_GS,
            "\n\n",
        )

    return reprovado


x = int(input("Digite o índice das notas (0 por exemplo): "))

calcular_nota(x)
