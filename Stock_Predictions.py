from __future__ import division
from math import sqrt
from heapq import heappush, heappop

def printTransactions(money, k, d, name, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        avg = mean(nums)
        variance = sum((x - avg) ** 2 for x in nums) / len(nums)
        return sqrt(variance)

    def info(price):
        price_change_count = sum(1 for i in range(1, 5) if price[i] > price[i - 1])
        price_sd = sd(price)
        price_mean = mean(price)
        avg_segments = [mean(price[start:start + 3]) for start in range(3)]
        price_change_rate = (price[-1] - price[-2]) / price[-2]
        return price_change_rate
    
    transaction_list = []
    potential_buys = []

    for i in range(k):
        current_info = info(prices[i])
        if current_info > 0 and owned[i] > 0:
            transaction_list.append((name[i], 'SELL', str(owned[i])))
        elif current_info < 0:
            heappush(potential_buys, (current_info, i, name[i]))

    while money > 0.0 and potential_buys:
        rate, idx, item_name = heappop(potential_buys)
        buy_amount = int(money / prices[idx][-1])
        if buy_amount > 0:
            transaction_list.append((item_name, 'BUY', str(buy_amount)))
            money -= buy_amount * prices[idx][-1]

    print(len(transaction_list))
    for transaction in transaction_list:
        print(' '.join(transaction))

if __name__ == '__main__':
    m, k, d = map(float, input().strip().split())
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for _ in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append(list(map(float, temp[2:7])))

    printTransactions(m, k, d, names, owned, prices)
