from unittest import TestCase
from unittest.mock import Mock

from stock_driver import KiwerDriver, NemoDriver, StockDriver


class TesdtStock(TestCase):
    def setUp(self):
        super().setUp()
        self.__driver = KiwerDriver()
        self.__driver = NemoDriver()

    def test_login(self):
        driver: StockDriver = Mock()
