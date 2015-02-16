# Difficulty - Moderate
# Problem Statement

# You are given an integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.

# The first few elements of fibonacci sequence are 0,1,1,2,3,5,8,13,⋯ A fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are 0 and 1.

# Formally: 
# fib0fib1⋮fibn=0=1=fibn−1+fibn−2∀n>1
# Input Format 
# The first line contains T, number of test cases. 
# T lines follows. Each line contains an integer N.

# Output Format 
# Display IsFibo if N is a fibonacci number and IsNotFibo if it is not a fibonacci number. The output for each test case should be displayed in a new line.

# Constraints 
# 1≤T≤105 
# 1≤N≤1010

def isFib(ars)
  ars.each do |num|
    if isPerfSqr(5*num*num + 4) || isPerfSqr(5*num*num - 4)
      puts "IsFibo"
    else 
      puts "IsNotFibo"
    end
  end
end

def isPerfSqr(num)
  sqr = Math.sqrt(num)
  sqr.floor**2 == num
end

n = gets.to_i
k_inputs = []

for i in 0...n do
  ent = gets.split("\n").each do |j|
    k_inputs << j.to_i
  end 
end

isFib(k_inputs)