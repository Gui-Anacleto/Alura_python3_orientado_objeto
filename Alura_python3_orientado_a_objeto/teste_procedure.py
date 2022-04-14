def cria_conta(numero,titular,saldo, limite):
    conta = { "numero":numero,"titular":titular, "saldo":saldo, "limite":limite}
    return conta
    #criar conta:
    #conta = Conta(1, "Gui", 30.0, 1000.0)
    
def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))