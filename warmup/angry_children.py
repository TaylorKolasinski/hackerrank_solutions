#Difficulty - Moderate
#Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to distribute one packet to each of the K children in the village (each packet may contain different number of candies). To avoid any fighting among the children, he would like to pick K out of N packets, such that unfairness is minimized.

# Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi denotes the number of candies in the ith packet, then we define unfairness as

# max(x1,x2,...xk) - min(x1,x2,...xk)

# where max denotes the highest value amongst the elements, and min denotes the least value amongst the elements. Can you figure out the minimum unfairness and print it?

# Input Format
# The first line contains an integer N.
# The second line contains an integer K. N lines follow. Each line contains an integer that denotes the candy in the ith packet.

# Output Format
# A single integer which will be the minimum unfairness.

# Constraints
# 1<=N<=10^5
# 1<=K<=N
# 0<= number of candies in any packet <=10^9


def unfairness(candies, k, n):
    start = 0
    end = k-1
    for i in range(n-k):
        unfairness = candies[end] - candies[start]
        if i > 0:
            if unfairness < min_unfairness:
                min_unfairness = unfairness
        else:
            min_unfairness = unfairness
        start = start + 1
        end = end + 1
    print int(min_unfairness)

n = input()
k = input()
candies = sorted([input() for _ in range(0,n)])
candies
unfairness(candies, k, n)
