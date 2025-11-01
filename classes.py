
class Classes:
    def __init__(self):
        self.balance = 0
        self.historical_transactions = []

    def deposit(self, amount: float):
        self.balance += amount
        self.historical_transactions.append(f"Depósito: +R${amount:.2f}")
        return {"balance": self.balance, "historical_transactions": self.historical_transactions}

    def withdraw(self, amount: float):
        if amount > self.balance:
            return {"error": "Saldo insuficiente", "balance": self.balance}
        self.balance -= amount
        self.historical_transactions.append(f"Saque: -R${amount:.2f}")
        return {"balance": self.balance, "historical_transactions": self.historical_transactions}

    def get_balance(self):
        return {"balance": self.balance, "historical_transactions": self.historical_transactions}

    def bank_data(self):
        while True:
            insert_data = input("Digite (s) para saque, (d) para depósito ou (q) para sair: ").strip().lower()

            if insert_data == 's':
                if self.balance == 0:
                    print("Não há dinheiro para saque.")
                    continue
                proposed_value = float(input("Qual o valor do seu saque: "))
                if proposed_value > self.balance:
                    print("Saldo insuficiente.")
                else:
                    self.withdraw(proposed_value)
                    print(f"Saque de R${proposed_value:.2f} realizado com sucesso!")
                    print(f"Saldo atual: R${self.balance:.2f}")

            elif insert_data == 'd':
                valor_deposito = float(input("Qual o valor do seu depósito: "))
                self.deposit(valor_deposito)
                print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
                print(f"Saldo atual: R${self.balance:.2f}")

            elif insert_data == 'q':
                print("Encerrando operações. Obrigado por usar nosso banco!")
                break

            else:
                print("Opção inválida. Digite 's', 'd' ou 'q'.")
