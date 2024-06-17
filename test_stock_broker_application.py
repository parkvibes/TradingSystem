from unittest import TestCase
from unittest.mock import Mock

from stock_broker_application import StockBrokerApplication
from stock_driver import StockDriver


class TestStockBrokerApp(TestCase):
    def test_select_stock_broker(self):
        pass

    def test_login(self):
        pass

    def test_buy(self):
        pass

    def test_sell(self):
        driver: StockDriver = Mock()
        app = StockBrokerApplication()
        app.select_stock_broker(driver)
        stock_code = '12341234'
        price = 10000
        amount = 100
        self.assertTrue(app.sell(stock_code, price, amount))

    def test_get_price(self):
        pass

    def test_buy_nice_timing(self):
        pass
    def test_sell_nice_timing(self):
        pass