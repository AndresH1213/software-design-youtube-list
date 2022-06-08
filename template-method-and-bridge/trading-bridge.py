from typing import List
from abc import ABC, abstractmethod

"""Bridge resolve for you is that if you have two
separate things that vary, in this case we have exchanges
and different tradingBot and what bridge solve for us is
add that capability to adding an extra exchange or adding
an extra bot without having to do anything on the other side
of the bridge."""

"""So the bridge is a kind of mechanism to have two separate class
hierarchies two variations that can change independently of each other"""

class Exchange(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass

class BinanceExchange(Exchange):
    def connect(self):
        print('Connecting to Binance...')

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

class CoinbaseExchange(Exchange):
    def connect(self):
        print('Connecting to Coinbase...')

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 32, 18, 1]

"""The bridge here is the connection between the trading bot object and the
exchange object, and the interesting thing here is that this happen in the
abstract level"""
class TradingBot(ABC):

    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

    def check_prices(self, coin: str):
        """Now we can actually add more tradingBot
        subclasess without change the check prices method"""
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
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

application = AverageTrader(CoinbaseExchange())
application.check_prices("BTC/USD")