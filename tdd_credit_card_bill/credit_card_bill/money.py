class Money(object):
    def __init__(self, amount, currency='BRL'):
        self.amount = amount
        self.currency = currency

    def print(self):
        return f"{self.amount} {self.currency}"