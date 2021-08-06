import pandas as pd     # Serve para importar um código do pandas
# Lógica do programa

# 1 - Abrir os 3 arquivos em excel
lista_meses = ["1-Janeiro", "2-Fevereiro", "3-Março"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    # 2 - Verificar se algum valor na coluna VENDAS daquele determinado arquivo é maior que 55.000
    if (tabela_vendas["Vendas"] > 55000).any():
        print(f"No mes de {mes} encontrou vendas acima de 55 mil")

# 3 - Caso seja maior que 55.000 -> Enviar uma SMS com o nome do ganhador e o mês em que foi feito, junto com as vendas
# 4 - Caso não houver valor maior que 55.000, não realizar nenhuma operação
# 5 - Bibliotecas a serem utilizadas para essa lógica:      pandas, openpyxl e twilio
