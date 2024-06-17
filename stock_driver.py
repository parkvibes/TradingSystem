from abc import abstractmethod, ABC

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