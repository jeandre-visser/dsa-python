def printAllNumbersThenAllPairSums(numbers):
    print('these are the numbers:')
    # O(n) b/c it depends on the size of the input (numbers) - Linear Time
    for number in numbers:
        print(number)

    print('and these are their sums:')
    # O(n^2) b/c it it has a nested loop and depends on the size of the input (numbers) - Quadratic Time
    for firstNumber in numbers:
        for secondNumber in numbers:
            print(firstNumber + secondNumber)


printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])
# O(n + n^2) --> O(n^2) --> Quadratic Time

# Big O Cheat Sheet Rules:
# - Worst Case (Usually)
# - Remove Constants (O(2n) --> O(n))
# - Different Terms for Inputs (O(n + m))
# - Drop Non-Dominant Terms (O(n + n^2) --> O(n^2))

# 0(x^2 + 3x + 100 + x/2) - Remove the constants and non-dominant terms
# 0(x^2)  - Worst case
