# Transactions‑of‑Bank

A simple bank transaction system in Python: supports deposit, withdrawal, viewing balance and transaction history.
It has both a console interface and a REST API using FastAPI.

#Project Structure:

transactions‑of‑Bank/
│
├── classes.py         # Contains the bank‑logic class
├── main.py            # Console interface for interacting with the bank
├── api.py             # REST API endpoints for the bank (FastAPI)
└── README.md          # This documentation

# Features
A Classes class (in classes.py) that maintains:

balance (initially 0)

historical_transactions (list of deposit/withdrawal entries)

Console interface (via main.py): lets a user interactively deposit, withdraw and view history.

REST API interface (via api.py): lets external clients query the balance/history, deposit and withdraw programmatically.

# Getting Started
Prerequisites:
- Python 3.7+

# Install dependencies (e.g., FastAPI and Uvicorn):
- pip install fastapi uvicorn

# Run the Console Interface:
- python main.py

# You will see prompts for:

- (s) → withdrawal (saque)

- (d) → deposit (depósito)

- (q) → quit (sair)

# Run the API Server:
vicorn api:app --reload

# Then you can access endpoints:

- GET / → returns a welcome message

- GET /balance → returns current balance and transaction history

- POST /deposit/{amount} → deposit the specified amount

- POST /withdraw/{amount} → withdraw the specified amount (if sufficient balance)


# Usage Example:
Bem‑vindo ao seu banco!
Digite (s) para saque, (d) para depósito ou (q) para sair: d  
Qual o valor do seu depósito: 100  
Depósito de R$100.00 realizado com sucesso!  
Saldo atual: R$100.00  
Histórico de transações:  
Depósito: +R$100.00  
Saldo total: R$100.00  
...

# API:
# Deposit 50
curl -X POST "http://127.0.0.1:8000/deposit/50"
# Response:
{"balance":50.0,"historical_transactions":["Depósito: +R$50.00"]}

# Check balance/history
curl "http://127.0.0.1:8000/balance"
# Response:
{"balance":50.0,"historical_transactions":["Depósito: +R$50.00"]}

# Withdraw 20
curl -X POST "http://127.0.0.1:8000/withdraw/20"
# Response:
{"balance":30.0,"historical_transactions":["Depósito: +R$50.00","Saque: -R$20.00"]}















