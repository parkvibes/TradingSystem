import io
from unittest import TestCase
from unittest.mock import Mock, patch

from stock_broker_application import StockBrokerApplication
from stock_driver import StockDriver


class TestStockBrokerApp(TestCase):
    def setUp(self):
        super().setUp()
        self.__broker = StockBrokerApplication()

    def test_select_stock_broker(self):
        pass

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_login(self, mock_stdout):
        def print_login(id, pw):
            print(f"{id} login success")

        driver: StockDriver = Mock()
        driver.login.side_effect = print_login

        self.__broker.select_stock_broker(driver)
        self.__broker.login("no name", "no password")
        self.assertEqual(mock_stdout.getvalue(), "no name login success\n")

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
