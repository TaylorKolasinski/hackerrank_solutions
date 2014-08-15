# Difficulty - Moderate
# Given N integers, count the number of pairs of integers whose difference is K.

# Input Format
# The 1st line contains N & K (integers).
# The 2nd line contains N numbers of the set. All the N numbers are distinct.

# Output Format
# An integer that tells the number of pairs of integers whose difference is K.

# Constraints:
# N <= 105
# 0 < K < 109
# Each integer will be greater than 0 and at least K smaller than 231-1

def pairs(al,a,k):
    count = 0

    for i, x in enumerate(a):
        while i < al and x + k > a[i]:
            i += 1
        if i == al:
            continue
        elif x + k == a[i]:
            count += 1

    print count

if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    b.sort()
    pairs(_a_size, b,_k)