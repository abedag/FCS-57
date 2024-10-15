# print("Assignment 3")

# print("Exercise 1:")
# print("")


# def recursive_binarySearch(grades, num1, start, end):
   
#     start = 0
#     end = len(grades) - 1 

#     if start > end:
#         return False
    
#     mid = (start + end)//2

#     if grades[mid] == num1:
#         return True
    
#     elif grades[mid] > num1:
#         return recursive_binarySearch(grades, num1, start, mid - 1)

#     else:
#         return recursive_binarySearch(grades, num1, mid + 1, end)

# grades = [5 ,25 ,39 ,56 ,67 ,75 ,90]

# print(recursive_binarySearch(grades, 100, 5, 90))
# print(recursive_binarySearch(grades, 75, 5, 90))

print("")
print("Exercise 2:")
print("")


def findCharcters(charcters, num2 ,reCharcters):
    if num2 == 0:
        print(reCharcters)
        return
    
    for i in charcters:
       findCharcters(charcters, num2 - 1, reCharcters + i)

charcters = ["a","b","c"]

findCharcters(charcters, 2 , "")

print("")
print("Exercise 4:")
print("")

