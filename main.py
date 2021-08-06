import pandas as pd     # Serve para importar um código do pandas
from twilio.rest import Client #Serve para importar a função de SMS de uma das biblioteca do twilio
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
    # Your Account SID from twilio.com/console
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # Your Auth Token from twilio.com/console
    auth_token  = "your_auth_token"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="Hello from Python!")
    print(message.sid)

# 4 - Ca#so não houver valor maior que 55.000, não realizar nenhuma operação


# 5 - Bibliotecas a serem utilizadas para essa lógica:      pandas, openpyxl e twilio
