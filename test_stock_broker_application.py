from unittest import TestCase
from unittest.mock import Mock

import stock_driver
from stock_broker_application import StockBrokerApplication


class TestStockBrokerApp(TestCase):
    def test_select_stock_broker(self):
        mk = Mock(spec=stock_driver)
        app = StockBrokerApplication()
        app.select_stock_broker(mk)
        self.assertIs(app.get_broker(), mk)

        kiwer_driver = stock_driver.KiwerDriver()
        app.select_stock_broker(kiwer_driver)
        self.assertIs(app.get_broker(), kiwer_driver)

        nemo_driver = stock_driver.NemoDriver()
        app.select_stock_broker(nemo_driver)
        self.assertIs(app.get_broker(), nemo_driver)

    def test_login(self):
        pass

    def test_buy(self):
        pass

    def test_sell(self):
        pass

    def test_get_price(self):
        pass

    def test_buy_nice_timing(self):
        pass

    def test_sell_nice_timing(self):
        pass
