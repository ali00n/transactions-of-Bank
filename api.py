
from fastapi import FastAPI
from classes import Classes

app = FastAPI()
my_bank = Classes()

@app.get("/")
def home():
    return {"message": "Bem-vindo ao seu banco!"}

@app.get("/balance")
def balance():
    return my_bank.get_balance()

@app.post("/deposit/{amount}")
def deposit(amount: float):
    return my_bank.deposit(amount)

@app.post("/withdraw/{amount}")
def withdraw(amount: float):
    return my_bank.withdraw(amount)
