class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def soma(self):
        result = self.num1 + self.num2
        print("Soma do {} + {} = {}".format(self.num1,self.num2,result))

    def sub(self):
        result = self.num1 - self.num2
        print("Soma do {} - {} = {}".format(self.num1,self.num2,result))

    def mult(self):
        result = self.num1 * self.num2
        print("Soma do {} * {} = {}".format(self.num1,self.num2,result))
    
    def div(self):
        result = self.num1 / self.num2
        print("Soma do {} / {} = {}".format(self.num1,self.num2,result))