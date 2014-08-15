# Difficulty - Easy
# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle of the tree occurs during the monsoon, when it doubles in height. The second growth cycle of the tree occurs during the summer, when its height increases by 1 meter.
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

# Input Format
# The first line contains an integer, T, the number of test cases.
# T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.

# Constraints
# 1 <= T <= 10
# 0 <= N <= 60

def tree(n):
  h = 1
  if n != 0:
    for x in range(1,n+1):
      if x%2 != 0:
        h = h*2
      else:
        h = h + 1
  print h

for _ in range(input()):
  tree(input())