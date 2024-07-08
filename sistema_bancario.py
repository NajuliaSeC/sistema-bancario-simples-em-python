menu = """

(1) Depositar
(2) Sacar
(3) Consultar Extrato
(4) Sair 

"""
saldo = 0
limite = 500
extrato = ""
saques_feitos = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    
    try:
        opcao = int(input("Digite a operação que deseja realizar:"))

        if opcao == 1:
            deposito = float(input("Digite o valor que deseja depositar:"))
            if deposito <= 0 :
                print ("Não é possível depositar este valor, tente novamente")
            else:
                saldo = saldo + deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                print (f"Seu depósito de ${deposito:.2f} foi realizado com sucesso")
        elif opcao ==2:
            saque = float (input("Digite o valor que deseja sacar:"))
            if saque > saldo:
                print ("Saldo insuficiente")
            elif saque <= 0 or saque > limite:
                print ("Não é possível sacar este valor, tente novamente")
            elif saques_feitos >= LIMITE_SAQUES:
                print ("Seu limite diário de saques foi atingido, tente novemente depois de 24 horas")
            else:
                saldo = saldo - saque
                extrato += f"Saque: R${saque:.2f}\n"
                print (f"Seu saque de ${saque:.2f} foi efetuado com sucesso")
                saques_feitos +=1
        elif opcao ==3:
            print("\n =====EXTRATO=====")
            print ("Não foram realizadas movimentações" if not extrato else extrato)
            print (f"\nSaldo: R$ {saldo:.2f}")
            print("==========")
        elif opcao == 4:
            break
        else:
            print ("Opção inválida tente novamente")
    except ValueError:
         print ("Por favor, digite um número")