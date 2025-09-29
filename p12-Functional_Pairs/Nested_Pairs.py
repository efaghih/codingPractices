
# Nested Pairs

# Extend cons so it can store not just values but other pairs.

# Ask the user to implement deep_car and deep_cdr that can traverse nested pairs 
# to extract values at arbitrary depths.

# Scenario:

# p = cons(cons(1, 2), cons(3, 4))
# # deep_car(p, [0,1]) should return 2
# # deep_cdr(p, [1,0]) should return 3


from Functional_Pairs import cons, cdr, car



# ------------------------------
# Only support 2-Levels 
# ------------------------------

def deep_car2l(pair, item):
    if item[0] == 0:
        next_pair =  car(pair)
        if item[1] == 0:
            return car(next_pair)
        elif item[1] == 1:
            return  cdr(next_pair)
    
    if item[0] == 1:
        next_pair =  cdr(pair)
        if item[1] == 0:
            return car(next_pair)
        elif item[1] == 1:
            return cdr(next_pair) 


# Assume cons, car, cdr, and deep_car are already defined

# ------------------------------
# 2-Level Nested Pair Test
# ------------------------------
p2 = cons(cons(1, 2), cons(3, 4))

print("2-Level Tests")
print(deep_car2l(p2, [0, 0]))  # Expected: 1
print(deep_car2l(p2, [0, 1]))  # Expected: 2
print(deep_car2l(p2, [1, 0]))  # Expected: 3
print(deep_car2l(p2, [1, 1]))  # Expected: 4




# ------------------------------
# Support multi-Level Pairs
# ------------------------------

def deep_car(pair, path):
    """
    Traverse a nested pair along the path.
    path: list of 0s and 1s
        0 -> car (left)
        1 -> cdr (right)
    """
    if not path:
        # Base case: path is empty, return the pair itself
        return pair
    
    # Take the first step in the path
    index = path[0]
    next_pair = car(pair) if index == 0 else cdr(pair)
    
    # Recurse on the remaining path
    return deep_car(next_pair, path[1:])



# ------------------------------
# Support multi-Level Nested Pairs
# ------------------------------
p2 = cons(cons(1, 2), cons(3, 4))

print("\nmultifunc: 2-Level Tests")
print(deep_car(p2, [0, 0]))  # Expected: 1
print(deep_car(p2, [0, 1]))  # Expected: 2
print(deep_car(p2, [1, 0]))  # Expected: 3
print(deep_car(p2, [1, 1]))  # Expected: 4


# # ------------------------------
# # 3-Level Nested Pair Test
# # ------------------------------
# p3 = cons(cons(cons(5, 6), 7), 8)

# print("\nmultifunc: 3-Level Tests")
# print(deep_car(p3, [0, 0, 0]))  # Expected: 5
# print(deep_car(p3, [0, 0, 1]))  # Expected: 6
# print(deep_car(p3, [0, 1]))     # Expected: 7
# print(deep_car(p3, [1]))        # Expected: 8

# # ------------------------------
# # 4-Level Nested Pair Test
# # ------------------------------
# p4 = cons(cons(cons(cons(9, 10), 11), 12), 13)

# print("\nmultifunc: 4-Level Tests")
# print(deep_car(p4, [0, 0, 0, 0]))  # Expected: 9
# print(deep_car(p4, [0, 0, 0, 1]))  # Expected: 10
# print(deep_car(p4, [0, 0, 1]))     # Expected: 11
# print(deep_car(p4, [0, 1]))        # Expected: 12
# print(deep_car(p4, [1]))           # Expected: 13