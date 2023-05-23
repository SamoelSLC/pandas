import pandas as pd

dataFrameDados = pd.read_excel(
    "D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Deletar_Linhas_Colunas.xlsx")

print(dataFrameDados)
print('\n')
print(type(dataFrameDados))
print('\n')


print('Somente linhas com dados')
deletandoLinhasEmBranco = dataFrameDados.dropna()
print(deletandoLinhasEmBranco)
print('\n')
