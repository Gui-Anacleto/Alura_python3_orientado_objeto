#criar objeto
class Conta:

    #função construtora.
    def __init__(self, numero, titular, saldo, limite): 
        #self é a referencia que sabe o endereço do objeto na memória.
        print("Construindo objeto...{}".format(self))
        #self sabe o endereço, então "." = vamos para lá.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
