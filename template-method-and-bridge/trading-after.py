from typing import List
from abc import ABC, abstractmethod

class TradingBot(ABC):

    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

    def check_prices(self, coin: str):
        """Now we can actually add more tradingBot
        subclasess without change the check prices method"""
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")


"""Now we decouple the process which is checking prices returning
what we should buy or sell and the actual algorithms"""
class AverageTrader(TradingBot):
    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)

class MinMaxTrader(TradingBot):
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)

application = AverageTrader()
application.check_prices("BTC/USD")