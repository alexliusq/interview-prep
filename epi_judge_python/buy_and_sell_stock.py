from typing import List

from test_framework import generic_test

## should be correct, passes everything but crashes at test 400
# def brute_force_stock(prices: List[float]) -> float:
#     # print(len(prices))
#     differences = [prices[j] - prices[i]
#                    for i in range(len(prices)) for j in range(i, len(prices))]
#     print(len(differences))
#     max_profit = max(differences)
#     return max_profit if max_profit > 0 else 0

def buy_and_sell_stock_once(prices: List[float]) -> float:
    lowest_price = float('inf')
    max_profit = 0.0
    for i in range(len(prices)):
        if (prices[i] < lowest_price):
            lowest_price = prices[i]
        profit = prices[i] - lowest_price
        if (profit > max_profit):
            max_profit = profit
    return max_profit

if __name__ == '__main__':
    # print('buy sell brute force')
    # generic_test.generic_test_main('buy_and_sell_stock.py',
    #                                 'buy_and_sell_stock.tsv',
    #                                 brute_force_stock)
    generic_test.generic_test_main('buy_and_sell_stock.py',
                                    'buy_and_sell_stock.tsv',
                                    buy_and_sell_stock_once)
