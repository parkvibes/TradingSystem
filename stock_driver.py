from abc import abstractmethod, ABC

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class StockDriver(ABC):
    @abstractmethod
    def select_stock_brocker(self):
        pass

    @abstractmethod
    def login(self, id, password):
        pass

    @abstractmethod
    def buy(self, code, price, count):
        pass

    @abstractmethod
    def sell(self, code, price, count):
        pass

    @abstractmethod
    def get_price(self, code):
        pass


class KiwerDriver(StockDriver):
    def __init__(self):
        super().__init__()
        self.__api = KiwerAPI()

    def login(self, id, pw):
        self.__api.login(id, pw)

    def buy(self, code, price, cnt):
        self.__api.buy(code, price, cnt)

    def sell(self, code, price, cnt):
        self.__api.sell(code, price, cnt)

    def get_price(self, code):
        self.__api.current_price(code)


class NemoDriver(StockDriver):
    def __init__(self):
        super().__init__()
        self.__api = NemoAPI()

    def login(self, id, pw):
        self.__api.cerification(id, pw)

    def buy(self, code, price, cnt):
        self.__api.purchasing_stock(code, price, cnt)

    def sell(self, code, price, cnt):
        self.__api.selling_stock(code, price, cnt)

    def get_price(self, code):
        self.__api.get_market_price(code, 1)
