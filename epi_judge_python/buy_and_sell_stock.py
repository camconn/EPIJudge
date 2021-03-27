from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if len(prices) == 0: return 0

    lo = prices[0]
    profit = float(0)

    for p in prices:
        lo = min(lo, p)

        todays_profit = p - lo

        profit = max(profit, todays_profit)

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
