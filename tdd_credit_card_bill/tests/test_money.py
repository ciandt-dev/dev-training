import unittest

from credit_card_bill.money import Money


class TestMoney(unittest.TestCase):
    def test_print_money(self):
        money = Money(amount=25)
        self.assertEqual(money.print(), '25 BRL')

    def test_default_currency_on_money(self):
        money = Money(amount=25)
        self.assertEqual(money.currency, 'BRL')


if __name__ == '__main__':
    unittest.main()
