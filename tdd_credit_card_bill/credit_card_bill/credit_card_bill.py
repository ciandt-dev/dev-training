from credit_card_bill.money import Money
from credit_card_bill.purchase import Purchase


class CreditCardBill:
    def __init__(self):
        self.purchases = []
        self.local_currency = 'BRL'

    def print(self, dollar_quote: Money):
        if len(self.purchases) == 0:
            return self.generate_bill_with_no_purchase(dollar_quote)
        else:
            report = self.append_purchase_header()
            report = self.append_purchase(report)
            report = self.append_international_purchase(dollar_quote, report)
            report = self.append_total_price(dollar_quote, report)
            return report

    def generate_bill_with_no_purchase(self, dollar_quote: Money) -> str:
        report = 'NENHUMA COMPRA REALIZADA\n'
        report = self.append_total_price(dollar_quote, report)
        return report

    def append_total_price(self, dollar_quote: Money, report: str) -> str:
        report += f"_\nVALOR TOTAL|{self.calculate_total_price(dollar_quote).print()}"
        return report

    def append_purchase(self, report: str) -> str:
        for purchase in self.purchases:
            report += f"{purchase.name}|{purchase.price.print()}\n"
        return report

    def append_international_purchase(self, dollar_quote: Money, report: str) -> str:
        has_international_purchase = self.has_international_purchase()
        if has_international_purchase:
            report += f"_\nCOTACAO USD|{dollar_quote.print()}\n"
        return report

    @staticmethod
    def append_purchase_header():
        return 'COMPRA|VALOR\n'

    def calculate_total_price(self, dollar_quote):
        total = 0
        for purchase in self.purchases:
            if purchase.price.currency == self.local_currency:
                total += purchase.price.amount
            else:
                total += purchase.price.amount * dollar_quote.amount
        return Money(total)

    def add_purchase(self, purchase: Purchase):
        self.purchases.append(purchase)

    def has_international_purchase(self) -> bool:
        has_international_purchase = False
        for purchase in self.purchases:
            if purchase.price.currency != self.local_currency:
                has_international_purchase = True
        return has_international_purchase
