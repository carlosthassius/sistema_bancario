#SISTEMA BANCARIO
#deposito, saque e extrato

saldo=0
extrato_cliente = ''

def saque():
    global saldo, extrato_cliente
    valor = float(input("Digite o valor que deseja sacar: "))
    if valor <= 500 and saldo >= valor:
        saldo-=valor
        print("Saque realizado com sucesso!\
\nSaldo restante: {:.2f}".format(saldo))
    elif valor <= 500 and saldo < valor:
        print("Saldo insuficiente")
    elif valor > 500:
        print("Só é possível realizar saque de até R$500.00")
    extrato_cliente+='Saque R$'
    extrato_cliente+=str(valor)
    extrato_cliente+='\n'
    menu()

def deposito():
    global saldo, extrato_cliente
    valor = float(input("Digite o valor que deseja depositar: "))
    saldo+=valor
    print("Depósito realizado com sucesso!\
\nSaldo: {:.2f}".format(saldo))
    extrato_cliente+='Depósito R$'
    extrato_cliente+=str(valor)
    extrato_cliente+='\n'
    menu()

def extrato():
    print(extrato_cliente)
    menu()

def menu():
    print("Bem-vindo ao Banco da DIO\n \
1) Sacar\n 2) Depositar\n 3) Ver extrato\n 4) Sair\n")
    opcao = input("Digite o código da ação desejada: ")
    if opcao == '1':
            saque()
    elif opcao == '2':
            deposito()
    elif opcao == '3':
            extrato()
    else: print("Operação encerrada")
    
menu()