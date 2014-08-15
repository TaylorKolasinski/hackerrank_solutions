# Difficulty - Easy
# Comparison Sorting
# Quicksort usually has a running time of n*log(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e., they sort a list just by comparing the elements with one another. A comparison sort algorithm cannot beat n log(n) (worst-case) running time, since n log(n) represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

# Alternative Sorting
# However, for certain types of input, it is more efficient to use a non-comparison sorting algorithm. This will make it possible to sort lists even in linear time. These challenges will cover Counting Sort, a fast way to sort lists where the elements have a small number of possible values, such as integers within a certain range. We will start with an easy task - counting.

# Challenge
# Given a list of integers, can you count and output the number of times each value appears?

# Hint: There is no need to sort the data, you just need to count it.

# Input Format
# There will be two lines of input:

# n - the size of the list
# ar - n space separated numbers that makes up the list
# Output Format
# Output the number of times every number from 0 to 99 (inclusive) appears in the list.

# Constraints
# 100 <= n <= 106
# 0 <= x < 100 , x ∈ ar

def counting_sort(ar):
  nums = list(range(100))
  counts = []

  for num in nums:
    counts.append(ar.count(num))

  print ' '.join(str(i) for i in counts)

n = input()
ar = [int(i) for i in raw_input().strip().split()]
counting_sort(ar)