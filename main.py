'''
Create coin alert for specified coin
'''
import time
from crypto_data import get_coins, Coin


def alert(symbol: str, bottom_price: float, top_price: float, coins_list: list[Coin]):
    '''
    Displays the coin alert
    '''
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top_price or coin.current_price < bottom_price:
                print(coin, 'Triggered!')
            else:
                print(coin)


if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    # Refresh data every 5 sec
    while True:
        alert('btc', bottom_price=30_000, top_price=33_000, coins_list=coins)
        alert('eth', bottom_price=20_000, top_price=22_000, coins_list=coins)
        time.sleep(5)
