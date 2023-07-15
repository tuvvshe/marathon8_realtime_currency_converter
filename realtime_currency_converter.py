from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("ENTER THE AMOUNT: "))
from_currency = input("FROM CURRENCY: ").upper()
to_currency = input("TO CURRENCY: ").upper()
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)