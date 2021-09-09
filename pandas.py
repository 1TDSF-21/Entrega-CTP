#primeira coisa, instalar openpyxl e o pandas se não tiver
import pandas as pd


sheet = pd.read_excel(r"C:\Users\joaom\Desktop\notas_planilha_modelo (1).xlsx")#pegar o caminho do seu pc
#teste de func
def mediaCp(x):
    n1 = sheet['checkpoint1'][x]
    n2 = sheet['checkpoint2'][x]
    n3 = sheet['checkpoint3'][x]
    media = (n1 + n2+ n3) /3
    print(sheet['Nome'][x] , '\nMedia do checkpoint:', media)
x = int(input("Digite o Indice das notas: (0 por exemplo)"))
mediaCp(x)





print("\n\n\n\n\n",sheet)#printa a tabela toda
