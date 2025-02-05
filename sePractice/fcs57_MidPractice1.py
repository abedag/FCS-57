# # Given an unsorted array of size N use selection sort to sort arr[] in a decreasing order______


def selecionSort(list):

    for unSort in range(0, len(list)):
        max = unSort

        for num in range(unSort, len(list)):
            if list[num] > list[max]:
                max = num

        list[unSort], list[max] = list[max], list[unSort]
        print(list)
    print(f"Here is the list {list} in descending order.")

selecionSort([4, 6, 1, 7, 9, 10 , 14, 54, 32, 67, 43])


# # Give a recursive binary search________________________________________________________________


def recursiveBinarySearch(list, num, start, end):

    if start > end:
        return False
    
    mid = (start + end)//2

    if list[mid] == num:
        return True
    
    elif list[mid] < num:
        return recursiveBinarySearch(list, num, start + 1, end)
    
    else:
        return recursiveBinarySearch(list, num, start, end - 1)
    
list = [1,2,3,4,5,6,7,8,9,10]    

print(recursiveBinarySearch(list, 1, 0, len(list)-1))


# # Give a fibonacci recursive function (generate sentence)_________________________________________________


def generateSentence(list, num, str):
    if num == 0:
        print(str)
        return
    for element in list:
        generateSentence(list, num-1, str+element)

generateSentence(["a","b"],2,"c")


# # Give a factorial recursive function___________________________________________________________


def fac(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fac(num-1)

print(fac(5))


# # Give an iterative binary search_______________________________________________________________


def iterBinarySearch(list, num):
    start = 0
    end = len(list) - 1
    mid = (start + end)//2

    while start <= end:
        mid = (start + end)//2

        if list[mid] == num:
            return True

        elif list[mid] > num:
            end = mid - 1

        else:
            start = mid + 1

    return False

print(iterBinarySearch([2,3,12,15,17,21,24,31,34,45,78,688], 34))





def recursiveBinarySearch(list, num, start, end):

    if start > end:
        return False
    
    mid = (start + end)//2

    if list[mid] == num:
        return True
    
    elif list[mid] < num:
        return recursiveBinarySearch(list, num, start + 1, end)
    
    else:
        return recursiveBinarySearch(list, num, start, end - 1)
    
list = [1,2,3,4,5,6,7,8,9,10]    

print(recursiveBinarySearch(list, 1, 0, len(list)-1))

def iterBinarySearch(list, num):
    start = 0
    end = len(list) - 1
    mid = (start + end)//2

    while start <= end:
        mid = (start + end)//2

        if list[mid] == num:
            return True

        elif list[mid] > num:
            end = mid - 1

        else:
            start = mid + 1

    return False

print(iterBinarySearch([2,3,12,15,17,21,24,31,34,45,78,688], 34))

def linearSearch(list, target):
    for i in list:
        if i == target:
            return target
    return -1

print(linearSearch([1,2,3,4,5,6,7,8,9,10], 4))
print(linearSearch([1,2,3,4,5,6,7,8,9,10], 32))
print(linearSearch([1,12,4,34,55,34,674,32,14,16], 1))

