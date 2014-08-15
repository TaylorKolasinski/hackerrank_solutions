# Difficulty - Easy
# There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs only once.

# Input Format

# The first line of the input contains an integer N indicating number of integers.
# The next line contains N space separated integers that form the array A.

# Constraints

# 1 <= N < 100
# N % 2 = 1 ( N is an odd number )
# 0 <= A[i] <= 100, ∀ i ∈ [1, N]


def lonelyinteger(a):
  for x in a:
    if a.count(x) == 1:
      print x

if __name__ == '__main__':
  a = input()
  b = map(int, raw_input().strip().split(" "))
  lonelyinteger(b)