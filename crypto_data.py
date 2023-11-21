'''
Get crypto data from Coingecko
'''
import requests
from dataclasses import dataclass
from typing import Final

# live data api url
BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'

@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name} ({self.symbol}): €{self.current_price:,}'
