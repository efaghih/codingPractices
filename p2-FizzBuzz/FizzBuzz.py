# Description:
# Write a program that prints numbers from 1 to n. But for 
# multiples of 3 print "Fizz", for multiples of 5 print "Buzz", 
# and for numbers which are multiples of both 3 and 5 print "FizzBuzz".

# Twist: Instead of just printing, return the sequence as a 
# list so it can be used later in other programs or tests.


# Requirements:

# Write a function fizzbuzz(n) that returns a list of length n.

# For each number:

# Multiple of 3 → "Fizz"

# Multiple of 5 → "Buzz"

# Multiple of 3 and 5 → "FizzBuzz"

# Otherwise → the number itself.



# Example Input/Output:

# Input: n = 15

# Output: [
#   1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
#   11, "Fizz", 13, 14, "FizzBuzz"
# ]



######   Start of Code   ######

n = int(input("Enter a number: "))

def fizzbuzz(n):
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
            print("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
            print("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
            print("Buzz")
        else:
            list.append(i)
            print(i)

    return list


output = fizzbuzz(n)
print(output)







