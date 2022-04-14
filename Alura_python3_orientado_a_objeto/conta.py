""" 
from conta import Conta
conta = Conta(1, "Gui", 30.0, 1000.0)
""" 

#criar OBJETO
class Conta:

    #função construtora.
    def __init__(self, numero, titular, saldo, limite): 
        #self é a referencia, ele sabe o endereço do objeto na memória.
        print("Construindo objeto...{}".format(self))
        #self sabe o endereço, então "." = vamos para lá.

        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        self.limite = limite
    
    #funções usadas m teste_procedure.py irão virar METODOS
    def extrato(self):
        print("Titular: {} \nSaldo: {} \nNumero: {} \nLimite: {}".format(self.titular, self.saldo, self.numero, self.limite))
        # conta.extrato()
        # conta2.extrato()

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


