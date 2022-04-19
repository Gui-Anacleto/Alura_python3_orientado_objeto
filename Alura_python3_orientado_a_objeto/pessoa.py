# -*- coding: latin-1 -*-
class Pessoa:    
    def __init__(self,nome,cpf,idade,endereco):
        print("Cadastrando...no utilizando o objeto: {}".format(self))

        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__endereco = endereco

    def consulta_cad(self):
        print("Nome: {}\nCPF: {}\nIdade: {}\nEndereco: {}".format(self.__nome,self.__cpf,self.__idade,self.__endereco))
    



