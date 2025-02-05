# # 1. Recursion

# # Exercise 1: Factorial using Recursion
# # Write a recursive function that takes a number n and returns the factorial of n.
# #  The factorial of a number is the product of all positive integers less than or 
# # equal to n (e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120).


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fac(n-1)

print(fac(3))
print(fac(5))
print(fac(9))


# # Exercise 2: Fibonacci Sequence using Recursion
# # Write a recursive function that returns the nth Fibonacci number.
# #  The Fibonacci sequence is defined as:

# # Fibonacci(0) = 0
# # Fibonacci(1) = 1
# # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) for n > 1





# # Exercise 3: Sum of Digits using Recursion
# # Write a recursive function that computes the sum of the digits of a given number.
# #  For example, given n = 123, the function should return 6 (since 1 + 2 + 3 = 6).


def sum_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(12))


# # 2. Search Algorithms

# # Exercise 1: Sequential (Linear) Search
# # Write a function that implements linear search.
# # Given a list of integers and a target value,
# # the function should return the index of the target value in the list.
# # If the target is not found, return -1.


def linearSearch(list, target):
    for i in list:
        if i == target:
            return target
    return -1

print(linearSearch([1,2,3,4,5,6,7,8,9,10], 4))
print(linearSearch([1,2,3,4,5,6,7,8,9,10], 32))
print(linearSearch([1,2,3,4,5,6,7,8,9,10], 1))


# # Exercise 2: Binary Search (Iterative)
# # Write an iterative function that implements binary search. 
# # Given a sorted list of integers and a target value, 
# # the function should return the index of the target value. 
# # If the target is not found, return -1.


def iterBinarySearch(list, target):
    start = 0
    end = len(list)-1
    mid = (start+end)//2

    while start <= end:
        mid = (start+end)//2

        if mid == target:
            return target
        
        elif mid > target:
            end = mid - 1

        else:
            start = mid + 1

    return -1

        
print(iterBinarySearch([1,2,3,4,5,6,31,34,56,234], 32))
print(iterBinarySearch([1,2,3,4,5,6,31,34,56,234], 1))
print(iterBinarySearch([1,2,3,4,5,6,31,34,56,234], 321))


# # Exercise 3: Binary Search (Recursive)
# # Write a recursive function that implements binary search. 
# # Given a sorted list of integers, a target value, 
# # and the left and right indices of the list, return the index of the target value. 
# # If the target is not found, return -1.


def recBinarySearch(list, target, start, end):

    mid = (start+end)//2

    while start > end:
        mid = (start+end)//2

        if list[mid] == target:
            return target
        
        elif list[mid] > target:
            return recBinarySearch(list, target, start+1, mid)
        
        else:
            return recBinarySearch(list, target, mid+1, end)
    
    return -1

list = [1,2,3,4,5,6,7,8,9]
print(recBinarySearch(list, 1, 0, len(list)-1))








# # 3. Sorting Algorithms

# # Exercise 1: Bubble Sort
# # Write a function that implements the bubble sort algorithm. Given a list of integers, 
# # the function should sort the list in ascending order by repeatedly swapping adjacent 
# # elements if they are in the wrong order.

# # Exercise 2: Insertion Sort
# # Write a function that implements the insertion sort algorithm. Given a list of integers,
# #  the function should sort the list by inserting elements into their correct positions.

# # Exercise 3: Merge Sort (Recursive)
# # Write a function that implements the merge sort algorithm using recursion.
# # Given a list of integers, the function should divide the list into two halves, 
# # sort each half recursively, and then merge the sorted halves to produce a sorted list.

# # Imad's Exercise 💀
# # If we have this list [1,2,3,4,5,6,7,8,9,10]
# # And we want sort this list 
# # Even and odd


# # Assiggnments

# # ass2
# # ex1


# list = [21,35,25,32,3,6,87,65]

# int1 = int(input("Enter the first number:"))
# int2 = int(input("Enter the second number:"))
# lower = min(int1,int2)
# upper = max(int1,int2)
# for n in list:
#     if lower <= n <= upper:
#         print(n)


# # ex2

# names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

# while True:

#     letter = input("Enter any letter you want or (q) to quit:")
#     if letter.lower == "q":
#         break
#     if  len(letter) != 1 or not letter.isalpha():
#         print("Enter a sinngle letter:")
#         continue

#     for name in names:
#         if letter in name.lower():
#             print(name)
    

# # ex3


# numbers = [-12, 2, 4, 12, 25, 67]

# for i in numbers:
#     number = int(input("Enter the number to add to the list or -99 to stop: "))
#     if number == -99:
#         print(f"The updated list is {numbers}")
#         break
#     else:
#         numbers.append(number)
#         numbers.sort()
#         print(f"The updated list is {numbers}")

# # ex4

# words = """Is this the real life? Is this just fantasy? Caught in a landslide,
# no escape from reality Open your eyes, look up to the skies and see I'm just
# a poor boy, I need no sympathy Because I'm easy come, easy go, little high,
# little low Any way the wind blows doesn't really matter to me, to me Mama,
# just killed a man Put a gun against his head, pulled my trigger, now h's
# dead Mama, life had just begun But now I've gone and thrown it all away Mama,
# ooh, didn't mean to make you cry If I'm not back again this time tomorrow
# Carry on, carry on as if nothing really matters Too late, my time has come
# Sends shivers down my spine, body's aching all the time Goodbye, everybody,

# I've got to go Gotta leave you all behind and face the truth Mama, ooh (any
# way the wind blows) I don't wanna die I sometimes wish I'd never been born at
# all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do
# the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)
# Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poor"
# boy, nobody loves me He's just a poor boy from a poor family Spare him his
# life from this monstrosity."""


# int11 = int(input("Enter the first index:"))
# int22 = int(input("Enter the second index:"))
# lower = min(int11,int22)
# upper = max(int11,int22)

# if int11 == int22:
#     print("You can't Input the same index.")

# if 0 <= lower < len(words) and 0 <= upper <= len(words):
#     result = words[lower:upper]
#     print(result)
