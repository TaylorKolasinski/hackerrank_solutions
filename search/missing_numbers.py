# Difficulty - Moderate

# Numeros, The Artist, had two lists A and B, such that, B was a permutation of A. Numeros was very proud of these lists. Unfortunately, while transporting them from one exhibition to another, some numbers from List A got left out. Can you find out the numbers missing from A?

# Notes

# If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both the lists is the same. If that is not the case, then it is also a missing number.
# You have to print all the missing numbers in ascending order.
# Print each missing number once, even if it is missing multiple times.
# The difference between maximum and minimum number in the list B is less than or equal to 100.
# Input Format
# There will be four lines of input:

# n - the size of the first list
# This is followed by n space separated integers that make up the first list.
# m - the size of the second list
# This is followed by m space separated integers that make up the second list.

# Output Format
# Output the missing numbers in ascending order

# Constraints
# 1<= n,m <= 1000001
# -10000 <= x <= 10000 , x ∈ B
# Xmax - Xmin < 101

def find_missing_numbers(a, b):
    missing_numbers = []
    for n in a:
        if a[n] != b[n]:
            print n,

def get_counts(nums, nums_counts):
    for n in nums:
        if n in nums_counts:
            nums_counts[n] = nums_counts[n] + 1
        else:
            nums_counts[n] = 1
     return nums_counts


if __name__ == '__main__':
    # Hanlde inputs
    n = raw_input()
    N = map(int, raw_input().strip().split(' '))
    m = raw_input()
    M = map(int, raw_input().strip().split(' '))

    # Get counts of numbers in each array (N, M)
    n_counts = {}
    m_counts = {}
    n_counts = get_counts(N, n_counts)
    m_counts = get_counts(M, m_counts)

    find_missing_numbers(n_counts, m_counts)