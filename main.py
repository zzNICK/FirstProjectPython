import pandas as pd     # Serve para importar um código do pandas
from twilio.rest import Client #Serve para importar a função de SMS de uma das biblioteca do twilio
#Fazendo conexção com o Twilio
# Your Account SID from twilio.com/console
account_sid = "AC9203c3fa9024a2780e4bfb1883e0a72b"
# Your Auth Token from twilio.com/console
auth_token = "b4e7e3dbd071d53b4b197b1f95c852a1"
client = Client(account_sid, auth_token)

# Lógica do programa

# 1 - Abrir os 3 arquivos em excel
lista_meses = ["1-Janeiro", "2-Fevereiro", "3-Março"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    # 2 - Verificar se algum valor na coluna VENDAS daquele determinado arquivo é maior que 55.000
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000 , "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"]. values[0]
        print(f"No mes de {mes} encontramos vendas acima de 55 mil. O Vendedor {vendedor} fez {vendas} vendas")
        # 3 - Caso seja maior que 55.000 -> Enviar uma SMS com o nome do ganhador e o mês em que foi feito, junto com as vendas
        message = client.messages.create(
            to="+5511976565635",
            from_="+16466797363",
            body=f"No mes de {mes} encontramos vendas acima de 55 mil. O Vendedor {vendedor} fez {vendas} vendas")
        print(message.sid)

# 4 - Caso não houver valor maior que 55.000, não realizar nenhuma operação
# 5 - Bibliotecas que foram utilizadas para essa lógica:      pandas, openpyxl e twilio
