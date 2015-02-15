# Difficulty - Easy
# Problem Statement

# Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

# Your task is to find the minimum number of required deletions.

# Input Format 
# The first line contains an integer T i.e. the number of test cases. 
# Next T lines contain a string each.

# Output Format 
# For each test case, print the minimum number of deletions required.

# Constraints

# 1≤T≤10 
# 1≤lengthofString≤105 

def alternatingChars (a)
  a.each do |str|
    count, prev_l = 0, ""
    str.split("").each do |l|
      count += (l == prev_l) ? 1 : 0
      prev_l = l
    end
    puts count
  end
end


# Get inputs
n = gets.to_i
k_inputs = []

for i in 0...n do
  ent = gets.split("\n").each do |j|
    k_inputs << j
  end 
end

alternatingChars(k_inputs)