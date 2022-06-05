def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'Seu saldo é: {conta["saldo"]}')

'''no método procedural você pode manipular e alterar os valores através de outras formas
enquanto no orientado a objetos você restringe a mudança apenas aos métodos que você quer
exemplo: conta = criar_conta(123, "Victor", 1000.0, 2000.0)
podemos modificar o saldo por exmplo com conta["saldo"] = 20000.0
sem precisar utilizar o metodo de deposito, além de ter que saber o nome da chave "saldo"'''