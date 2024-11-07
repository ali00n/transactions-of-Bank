print("Bem-vindo ao seu banco!")

saldo = 0
historico_transacoes = []

while True:
    opcao = input("Digite (s) para saque, (d) para depósito ou (q) para sair: ")

    if opcao == 's':
        valor_saque = float(input("Qual o valor do seu saque: "))

        if valor_saque > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldo -= valor_saque
            historico_transacoes.append(f"Saque: -R${valor_saque:.2f}")
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
            print(f"Seu saldo: R${saldo:.2f}")

    elif opcao == 'd':
        valor_deposito = float(input("Qual o valor do seu depósito: "))
        saldo += valor_deposito
        historico_transacoes.append(f"Depósito: +R${valor_deposito:.2f}")
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == 'q':
        print("Encerrando operações. Obrigado por usar nosso banco !")
        break

    else:
        print("Opção inválida. Por favor, digite 's' para saque, 'd' para depósito ou 'q' para sair.")

print("\nHistórico de transações:")
for transacao in historico_transacoes:
    print(transacao)
print(f"Saldo total: R${saldo:.2f}")
