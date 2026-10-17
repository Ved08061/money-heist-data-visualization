import matplotlib.pyplot as plt

class MoneyHeist:
    def __init__(self, bank_name, amount_stolen):
        self.bank_name = bank_name
        self.amount_stolen = amount_stolen
    
    def __str__(self):
        return f"A heist was pulled off at {self.bank_name} and {self.amount_stolen} dollars were stolen!"

heists = [
    MoneyHeist("National Bank", 1000000),
    MoneyHeist("City Bank", 500000),
    MoneyHeist("First Bank", 750000),
]

bank_names = [heist.bank_name for heist in heists]
amounts_stolen = [heist.amount_stolen for heist in heists]

plt.bar(bank_names, amounts_stolen)
plt.xlabel("Bank Name")
plt.ylabel("Amount Stolen")
plt.title("Money Heists")
plt.show()