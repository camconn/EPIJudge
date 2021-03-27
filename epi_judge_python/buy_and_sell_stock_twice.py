from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    if len(prices) <= 1: return 0

    mx_total_profit = 0
    mn_price_seen = prices[0]
    mx_price_seen = prices[-1]

    fst_profits = [0]*len(prices)

    # calculate first sale profits
    for i, p in enumerate(prices):
        mn_price_seen = min(mn_price_seen, p)
        mx_total_profit = max(mx_total_profit, p - mn_price_seen)
        fst_profits[i] = mx_total_profit

    # second sale profits
    # can't use enumerate here
    for i in range(len(prices)-1, 0, -1):
        p = prices[i]

        mx_price_seen = max(mx_price_seen, p)
        mx_total_profit = max(mx_total_profit, mx_price_seen - p + fst_profits[i-1])

    return mx_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
