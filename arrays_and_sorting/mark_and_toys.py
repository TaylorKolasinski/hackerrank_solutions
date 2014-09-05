# Difficulty - Easy

# Mark and Jane are very happy after having their first kid. Their son is very fond of toys, so Mark wants to buy some. There are N different toys lying in front of him, tagged with their prices, but he has only $K. He wants to maximize the number of toys he buys with this money.

# Now, you are Mark's best friend and have to help him buy as many toys as possible.

# Input Format
# The first line contains two integers, N and K, followed by a line containing N space separated integers indicating the products' prices.

# Output Format
# An integer that denotes maximum number of toys Mark can buy for his son.

# Constraints
# 1<=N<=105
# 1<=K<=109
# 1<=price of any toy<=109
# A toy can't be bought multiple times.

def max_toys(prices, k):
    cost = 0
    for i, p in enumerate(prices):
        cost += p
        if cost > k:
          print i
          return

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  max_toys(sorted(prices), k)