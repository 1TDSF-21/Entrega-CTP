import pandaa

def aluno_aprovado():
    print("\033[32m ------ Lista de aprovação sem GS ------ \033[0;0m")
    for index in range(len(pandaa.sheet)):
        if pandaa.calcular_nota(index, False)=="aprovadoSemGS": 
            print(
                f"\033[32m RM: {pandaa.sheet['RM'][index]}, Nome: {pandaa.sheet['Nome'][index]} \033[0;0m"
            )

aluno_aprovado()