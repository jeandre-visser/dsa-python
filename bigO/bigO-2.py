def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])  # O(1)

    middleIndex = len(items) // 2
    index = 0

    while index < middleIndex:  # O(n/2)
        print(items[index])
        index += 1

    for time in range(100):  # O(100)
        print('hi')


# O(1 + n/2 + 100) --> O(n/2 + 101) --> O(n + 1) --> O(n) --> Linear Time
printFirstItemThenFirstHalfThenSayHi100Times([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
