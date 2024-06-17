from random import seed
from unittest import TestCase
from unittest.mock import Mock
from stock_broker_application import StockBrokerApplication
from stock_driver import *
class TestStockBrokerApp(TestCase):
    def test_select_stock_broker(self):
        pass

    def test_login(self):
        pass

    def test_buy(self):
        pass

    def test_sell(self):
        pass

    def test_get_price_for_Kiwier(self):
        mk = Mock()
        st = StockBrokerApplication()
        st.select_stock_broker(mk) # KiwerDriver()
        mk.get_price.return_value = 8888
        #seed(99)
        self.assertEqual(8888, st.get_price(1))


    def test_get_price_for_Nemo(self):
        mk = Mock()
        st = StockBrokerApplication()
        st.select_stock_broker(mk)  # NemoDriver()
        mk.get_price.return_value = 8888
        #seed(99)
        self.assertEqual(8888, st.get_price(1))

    def test_buy_nice_timing(self):
        pass
    def test_sell_nice_timing(self):
        pass