import io
from unittest import TestCase
from unittest.mock import Mock, patch
import stock_driver
from stock_broker_application import StockBrokerApplication
from stock_driver import StockDriver, KiwerDriver

from stock_broker_application import StockBrokerApplication
from stock_driver import StockDriver


class TestStockBrokerApp(TestCase):
    def setUp(self):
        super().setUp()
        self.app = StockBrokerApplication()

    def test_select_stock_broker(self):
        mk = Mock(spec=StockDriver)
        self.app.select_stock_broker(mk)
        self.assertIs(self.app.get_broker(), mk)

        kiwer_driver = KiwerDriver()
        self.app.select_stock_broker(kiwer_driver)
        self.assertIs(self.app.get_broker(), kiwer_driver)

        nemo_driver = NemoDriver()
        self.app.select_stock_broker(nemo_driver)
        self.assertIs(self.app.get_broker(), nemo_driver)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_login(self, mock_stdout):
        def print_login(id, pw):
            print(f"{id} login success")

        driver: StockDriver = Mock()
        driver.login.side_effect = print_login

        self.app.select_stock_broker(driver)
        self.app.login("no name", "no password")
        self.assertEqual(mock_stdout.getvalue(), "no name login success\n")

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

    def test_get_price_for_Kiwier(self):
        mk = Mock()
        self.app.select_stock_broker(mk) # KiwerDriver()
        mk.get_price.return_value = 8888
        #seed(99)
        self.assertEqual(8888, self.app.get_price(1))


    def test_get_price_for_Nemo(self):
        mk = Mock()
        self.app.select_stock_broker(mk)  # NemoDriver()
        mk.get_price.return_value = 8888
        #seed(99)
        self.assertEqual(8888, self.app.get_price(1))

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
