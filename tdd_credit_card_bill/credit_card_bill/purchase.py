from credit_card_bill.money import Money


class Purchase:
    def __init__(self, name, price: Money):
        self.name = name
        self.price = price