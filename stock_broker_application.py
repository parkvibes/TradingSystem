from stock_driver import StockDriver
import time


class StockBrokerApplication:
    def __init__(self):
        self.__stock_broker = None
        self.__sleep_ms_between_tries = 100
        
    def select_stock_broker(self,
                            stock_broker: StockDriver):
        self.__stock_broker = stock_broker

    def get_broker(self):
        return self.__stock_broker

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
        return self.__stock_broker.get_price(stock_code)

    def buy_nice_timing(self, stock_code: int, money: int):

        cur_price = self.__stock_broker.get_price(stock_code)

        time.sleep(self.__sleep_ms_between_tries / 1000)
        if cur_price > self.__stock_broker.get_price(stock_code):
            return 0
  
        self.__stock_broker.buy(stock_code, cur_price, money // cur_price)

        return money // cur_price

        

    def sell_nice_timing(self):
        pass
