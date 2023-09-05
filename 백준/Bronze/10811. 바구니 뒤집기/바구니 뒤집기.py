n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]

for i in range(m):
    i, j = map(int, input().split())
    trade = []
    for u in range(j - 1, i - 2, -1):
        trade.append(basket[u])
    basket = basket[: i - 1] + trade + basket[j:]
print(*basket)