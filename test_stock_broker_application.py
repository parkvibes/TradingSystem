from unittest import TestCase
from unittest.mock import Mock
from stock_driver import KiwerDriver
from stock_broker_application import StockBrokerApplication

class TestStockBrokerApp(TestCase):

    def setUp(self):
        self.app = StockBrokerApplication()

    def test_select_stock_broker(self):
        pass

    def test_login(self):
        pass

    def test_buy(self):
        pass

    def test_sell(self):
        pass

    def test_get_price(self):
        pass

    def test_buy_nice_timing_ok(self):      
        self.mk = Mock(repr=KiwerDriver)
        self.app.select_stock_broker(self.mk)
        self.mk.get_price.side_effect = [100, 100]

        ret = self.app.buy_nice_timing(1, 1000)

        self.assertEqual(self.mk.get_price.call_count, 2)
        self.assertEqual(ret, 1000 // 100)

    def test_buy_nice_timing_not_ok(self):    
        self.mk = Mock(repr=KiwerDriver)
        self.app.select_stock_broker(self.mk)
        self.mk.get_price.side_effect = [100, 99]

        ret = self.app.buy_nice_timing(1, 1000)

        self.assertEqual(self.mk.get_price.call_count, 2)
        self.assertEqual(ret, 0)




    def test_sell_nice_timing(self):
        pass