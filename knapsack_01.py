
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value




def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp

def constructList(dp, weights, values, capacity):
    n = len(weights)
    x = [0]*n
    profit = dp[n][capacity]

    for i in range(n,0,-1):
        if profit in dp[i] and profit not in dp[i-1]:
            x[i-1] = 1
            profit = profit-values[i-1]

    return x

def main():
    weights = [2, 3, 4, 5]
    values = [1, 2, 5, 6]
    items = [Item(5,6), Item(3,2), Item(4,5), Item(2, 1)]
    items.sort(key = lambda x: x.weight)
    for item in items:
        print(item.weight)
    capacity = 8
    dp = knapsack(weights, values, capacity)
    x = constructList(dp, weights, values, capacity)
    print(x)

if __name__=='__main__':
    main()
