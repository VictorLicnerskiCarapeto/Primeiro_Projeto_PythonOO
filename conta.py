class Conta:

    #Construtor
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Métodos
    def extrato(self):
        print(f'Saldo {self.__saldo} do Titular {self.__titular}')
    def deposita(self,  valor):
        self.__saldo += valor
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O {valor} passou o limite")
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    #Getters e Setters
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

'''
Lembrete:
conta = none zera uma referencia
garbage collector do python exclui objetos sem referencia
from conta import Conta
Para criar um novo objeto dentro do console: conta = Conta(123, "Nico", 55.5, 1000.0)
Para ver um atributo específico: exempl = conta.saldo(o "." serve como referencia para onde ir)
Para utilizar um método: exemplo = conta.deposita(50.0)
o self sabe onde o está o endereço do objeto e seus atributos
"__" antes dos atributos significa que s mesmos são privados
A refatoração de um código é muito importante pois sempre á algo a melhorar no que já foi feito
Os getters servem para leitura dos atributos e os Setters para modificá-los
metodos estaticos são aqueles que independem do objeto, são usados pela própia classe, normalmente utilizados
quando os objetos conpartlham de algo comum
Conta.codigos_objeto()
'''