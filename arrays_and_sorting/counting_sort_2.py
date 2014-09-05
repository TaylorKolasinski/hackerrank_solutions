# Difficulty - Easy

# Often, when a list is sorted, the elements being sorted are just keys to other values. For example, if you are sorting files by their size, the sizes need to stay connected to their respective files. You cannot just take the size numbers and output them in order, you need to output all the required file information.

# However, if you are not concerned about any other information, then you can simply sort those numbers alone. This makes counting sort very simple. If you already counted the values in the list, you don't need to access the original list again. This challenge involves a simple counting sort where the elements being sorted are all that matter.

# Challenge
# Given an unsorted list of integers, output the integers in order.

# Hint: You can use your previous code that counted the items to print out the actual values in-order.

# Input Format
# There will be two lines of input:

# n - the size of the list
# ar - n space separated numbers that belong to the list
# Output Format
# Output all the numbers of the list in-order.

# Constraints
# 1 <= n <= 1000000
# 0 <= x < 100 , x ∈ ar

def counting_sort(ar, n):
  nums = set(ar)
  sort = []

  for num in nums:
    for i,val in enumerate(ar):
        if val == num:
            sort.append(val)

  print ' '.join(str(i) for i in sort)

n = input()
ar = [int(i) for i in raw_input().strip().split()]
counting_sort(ar, n)