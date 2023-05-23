import pandas as opcoesPandas



vendas_DF = opcoesPandas.read_excel(
    "D:\\curso\\pandas\\pandas\\2 - Data Frame\\DataFrame\\Vendas_Jan.xlsx")

print(vendas_DF.columns)
print("\n")

print(vendas_DF)

'''vendas = tabula.read_pdf("D:\\curso\\Histórico Alunos.pdf", pages="1")
print(vendas)'''