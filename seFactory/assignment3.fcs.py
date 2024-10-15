print("Assignment 3")
print("")

print("Exercise 1:")
print("")


def recursive_binarySearch(grades, num1, start, end):
    
    if start > end:
        return False
    
    mid = (start + end)//2

    if grades[mid] == num1:
        return True
    
    elif grades[mid] > num1:
        return recursive_binarySearch(grades, num1, start, mid - 1)

    else:
        return recursive_binarySearch(grades, num1, mid + 1, end)

grades = [5 ,25 ,39 ,56 ,67 ,75 ,90]

print(recursive_binarySearch(grades, 100, 0, len(grades) - 1))
print(recursive_binarySearch(grades, 75, 0, len(grades) - 1)) 

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

def add_to_sort(integers, int1_4):

    for min in range(0, len(integers)):
        if int1_4 <= integers[min]:

            integers.insert(min, int1_4)
            return integers

    integers.appeend(int1_4)
    return integers

print(add_to_sort([1,2,4,6,32,45,76,99,110] , 55))    


print("")
print("Exercise 3:")
print("")

