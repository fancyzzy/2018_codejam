def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0
    candies = [0] * n
    for i in range(n):
        if i == 0:
            candies[i] = 1
        else:
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            else:
                candies[i] = 1
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            continue
        else:
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            else:
                continue
    res = sum(candies)
    return res

str = input()
strlist = str.split()
intlist = list(map(float, strlist))
print(candy(intlist))

