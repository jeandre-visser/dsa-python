boxes = ['a', 'b', 'c', 'd', 'e']


def logAllPairsOfArray(array):
    for i in range(len(array)):  # O(n)
        for j in range(len(array)):  # O(n)
            print(array[i], array[j])  # O(1)


print(logAllPairsOfArray(boxes))  # O(n * n) --> O(n^2) --> Quadratic Time

# Loops that occur nested (like the above) are multiplied together.
# Loops that occur one after another (not nested - like in bigO-3) are added together.
