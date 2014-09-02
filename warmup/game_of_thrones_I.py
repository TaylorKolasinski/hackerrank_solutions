#Difficulty - Easy
# King Robert has 7 kingdoms under his rule. He finds out from a raven that the Dothraki are soon going to wage a war against him. But, he knows the Dothraki need to cross the narrow river to enter his dynasty. There is only one bridge that connects both sides of the river which is sealed by a huge door.

# The king wants to lock the door so that the Dothraki can't enter. But, to lock the door he needs a key that is an anagram of a certain palindrome string.

# The king has a string composed of lowercase English letters. Help him figure out if any anagram of the string can be a palindrome or not.

# Input Format
# A single line which contains the input string

# Constraints
# 1<=length of string <= 10^5
# Each character of the string is a lowercase English letter.

def is_pal(string):
    uni_vals = list(set(string))
    odd_count = 0

    if len(string) % 2 == 0:
        for char in uni_vals:
            if string.count(char) % 2 != 0:
                found = False
                return
        found = True
    else:
        for char in uni_vals:
            if string.count(char) % 2 != 0:
                odd_count += 1
        if odd_count > 1:
            found = False
        else:
            found = True
    return found

string = raw_input()
found = is_pal(string)

if not found:
    print("NO")
else:
    print("YES")