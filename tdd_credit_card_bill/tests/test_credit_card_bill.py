import unittest

from credit_card_bill.bill import Bill
from credit_card_bill.money import Money
from credit_card_bill.purchase import Purchase


class TestBill(unittest.TestCase):

    def setUp(self) -> None:
        self.bill = Bill()

    def test_report_with_no_purchase(self):
        report = self.call_print()
        self.assertEqual('NENHUMA COMPRA REALIZADA\n_\nVALOR TOTAL|0 BRL', report)

    def test_report_with_one_local_purchase(self):
        self.bill.add_purchase(Purchase(name='LOJAS AMERICANAS', price=Money(amount=250)))
        report = self.call_print()
        self.assertEqual('COMPRA|VALOR\nLOJAS AMERICANAS|250 BRL\n_\nVALOR TOTAL|250 BRL', report)

    def test_add_purchase(self):
        self.bill.add_purchase(Purchase(name='LOJAS AMERICANAS', price=Money(amount=25)))
        self.assertEqual(1, len(self.bill.purchases))

    def test_add_purchases(self):
        self.bill.add_purchase(Purchase(name='LOJAS AMERICANAS', price=Money(amount=250)))
        self.bill.add_purchase(Purchase(name='A', price=Money(amount=250)))
        self.assertEqual(2, len(self.bill.purchases))

    def test_report_with_more_than_one_local_purchase(self):
        self.bill.add_purchase(Purchase(name='LOJAS AMERICANAS', price=Money(amount=250)))
        self.bill.add_purchase(Purchase(name='LOJAS RENNER', price=Money(amount=100)))
        report = self.call_print()
        self.assertEqual('COMPRA|VALOR\nLOJAS AMERICANAS|250 BRL\nLOJAS RENNER|100 BRL\n_\nVALOR TOTAL|350 BRL', report)

    def test_report_with_one_international_purchase(self):
        self.bill.add_purchase(Purchase(name='ROSS', price=Money(amount=100, currency='USD')))
        report = self.call_print()
        self.assertEqual('COMPRA|VALOR\nROSS|100 USD\n_\nCOTACAO USD|4 BRL\n_\nVALOR TOTAL|400 BRL', report)

    def call_print(self):
        report = self.bill.print(dollar_quote=Money(4))
        return report


if __name__ == '__main__':
    unittest.main()
