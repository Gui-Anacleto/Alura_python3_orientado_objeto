def cria_conta(numero,titular,saldo, limite):
    conta = { "numero":numero,"titular":titular, "limite":limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))