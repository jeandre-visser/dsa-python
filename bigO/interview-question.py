# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];
# const array2 = ['z', 'y', 'x'];
# should return true.

# 2 parameters - arrays - no size limit
# return true or false

def containsCommonItem(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False

# O(a*b)
# O(1) - Space Complexity


array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'a']


def containsCommonItem2(arr1, arr2):
    # loop through first array and create object where properties === items in the array
    # can we assume always 2 params?

    map = {}
    for i in range(len(arr1)):
        if arr1[i] not in map:
            item = arr1[i]
            map[item] = True
    # loop through second array and check if item in second array exists on created object.
    for j in range(len(arr2)):
        if arr2[j] in map:
            return True
    return False

# O(a + b) Time Complexity
# O(a) Space Complexity

# containsCommonItem2(array1, array2)


def containsCommonItem3(arr1, arr2):
    # This function checks if there is any common item in two input arrays.
    # It uses Python's built-in function 'any' which returns True if at least one item in the iterable is true.
    # The iterable in this case is a generator expression that checks for each item in arr1 if it is in arr2.
    # If it finds any item in arr1 that is also in arr2, it immediately returns True and stops execution.
    # If no common item is found after checking all items, it returns False.
    return any(item in arr2 for item in arr1)


containsCommonItem(array1, array2)
containsCommonItem2(array1, array2)
containsCommonItem3(array1, array2)
