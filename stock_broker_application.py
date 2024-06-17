from stock_driver import StockDriver


class StockBrokerApplication:
    def __init__(self):
        self.__stock_broker = None

    def select_stock_broker(self,
                            stock_broker: StockDriver):
        self.__stock_broker = stock_broker

    def login(self,
              _id: str,
              pw: str) -> None:
        self.__stock_broker.login(_id, pw)

    def purchase(self,
                 stock_code: int,
                 price: int,
                 amount: int) -> None:
        self.__stock_broker.purchase(stock_code, price, amount)

    def sell(self,
             stock_code: int,
             price: int,
             amount: int) -> None:
        self.__stock_broker.sell(stock_code, price, amount)

    def get_price(self,
                  stock_code: int) -> int:
        return self.__stock_broker.current_stock_price(stock_code)

    def buy_nice_timing(self):
        pass

    def sell_nice_timing(self):
        pass
