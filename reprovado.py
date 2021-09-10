import pandaa

def aluno_reprovado():
    print("\033[31m ------ Lista de reprovação ------ \033[0;0m")
    for index in range(len(pandaa.sheet)):
        if pandaa.calcular_nota(index, False):
            print(
                f"\033[31m RM: {pandaa.sheet['RM'][index]}, Nome: {pandaa.sheet['Nome'][index]} \033[0;0m"
            )

aluno_reprovado()