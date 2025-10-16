# Container With Most Water (Two Pointers - Medium)

# Description:
# You are given an integer array height where each value represents height of a vertical line on the x-axis.
# Find two lines that together with the x-axis form a container that holds the most water.

# Requirements:
# Implement a function:

# def max_area(height: list[int]) -> int:

 
# Example:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: Max area between indices 1 and 8 (min height 7 × width 7)



### Start of Code ###

def max_area(height: list[int]) -> int:
    
    wth = 0
    lng = 0
    max_val = 0
    for i in range(len (height)):
        for j in range (len(height)):
            wth = abs(i-j)
            lng = min (height[i], height[j])
            max_val = max(max_val, lng * wth)
    
    return max_val

print("____________First Soln._____________")


height = [1,8,6,2,5,4,8,3,7]
print(f"max area for {height} = {max_area(height)}")

height = [4,3,2,1,4]
print(f"max area for {height} = {max_area(height)}")

height = [1,1]
print(f"max area for {height} = {max_area(height)}")


# O(n^2)



### Second Soln. ###


def max_area_sol2(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_val = 0
    while (left != right):
        max_val = max(max_val, min(height[left], height[right]) * abs(left - right))
        if (height[left] > height[right]):
            right -= 1
        elif (height[right] >= height[left]):  
            left += 1
        # print(f"left: {left} and height left {height[left]}")
        # print(f"left: {right} and height left {height[right]}")
    
    return max_val


print("____________Second Soln._____________")


height = [1,8,6,2,5,4,8,3,7]
print(f"max area for {height} = {max_area_sol2(height)}")

height = [4,3,2,1,4]
print(f"max area for {height} = {max_area_sol2(height)}")

height = [1,1]
print(f"max area for {height} = {max_area_sol2(height)}")


# O(n^2)
