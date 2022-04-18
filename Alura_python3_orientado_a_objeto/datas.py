
class Data:

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))

#TESTE
# data = Data(21,7,2022)
# data.formatada()
# 21/7/2022               <- Resultado.