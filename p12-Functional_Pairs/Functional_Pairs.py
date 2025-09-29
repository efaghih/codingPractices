# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element 
# of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.



### Start of Code ###

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car (pair):
    return pair(lambda a,b: a)

def cdr (pair):
    return pair(lambda a,b: b)  


# instead of lambda, we could use def and define new functions for doing the same job.


# # Test:
# pair = cons(3,4)
# print(f"{pair}")
# car_test = car(pair)
# cdr_test = cdr(pair)
# print(f"car: {car_test}")
# print(f"cdr: {cdr(pair)}")

       