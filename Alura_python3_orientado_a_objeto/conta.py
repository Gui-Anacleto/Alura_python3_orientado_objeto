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

        self.__titular = titular
        self.__saldo = saldo
        self.__numero = numero
        self.__limite = limite
    
    #funções usadas m teste_procedure.py irão virar METODOS
    def extrato(self):
        print("Titular: {} \nSaldo: {} \nNumero: {} \nLimite: {}".format(self.__titular, self.__saldo, self.__numero, self.__limite))
        # conta.extrato()
        # conta2.extrato()

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor


