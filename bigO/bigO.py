import time


# -------- LINEAR TIME --------
# Best Case: O(n) --> Linear Time
# Reason 1: Linear time complexity is good as it scales directly with the size of the input.
# Reason 2: It is predictable and easy to understand.
# Reason 3: It is often the best possible time complexity for algorithms that need to process each element of the input at least once.
# However, it is not as efficient as constant time because:
# Reason 4: It can become inefficient for large inputs.
# Reason 5: It does not provide consistent performance regardless of the input size.
# Reason 6: It is not ideal for real-time systems where consistent performance is critical.
# nemo = ['nemo'] * 100

# large = ['nemo'] * 10000
# everyone = ["dory", "bruce", "marlin",
#             "gill", "bloat", "nigel", "nemo", "squirt", "darla"]


# def find_nemo(array):
#     t0 = time.time()
#     for i in range(len(array)):
#         if array[i] == 'nemo':
#             print('Found Nemo!')
#             break
#         else:
#             print('Not Nemo!')
#     t1 = time.time()
#     print(f'Time taken: {t1 - t0} seconds')


# find_nemo(everyone)  # O(n) --> Linear Time


# -------- CONSTANT TIME --------
# Best Case: O(1) --> Constant Time (Most Efficient)
# Reason 1: Constant time complexity is the most efficient as it does not depend on the size of the input.
# Reason 2: It allows for predictable performance, regardless of the input size.
# Reason 3: It is ideal for real-time systems where consistent performance is critical.

# boxes = [0, 1, 2, 3, 4, 5]


# def log_first_two_boxes(boxes):
#     print(boxes[0])  # O(1)
#     print(boxes[1])  # O(1)


# log_first_two_boxes(boxes)  # O(2) --> Constant Time


# What is the Big O of the below function? (Hint, you may want to go line by line)
def funChallenge(input):
    # O(1) --> Constant Time: This operation does not depend on the size of the input.
    a = 10
    # O(1) --> Constant Time: This operation also does not depend on the size of the input.
    a = 50 + 3

    # O(n) --> Linear Time: This loop runs as many times as the size of the input. Loops are always linear time.
    for i in range(len(input)):
        # O(n) --> Linear Time: This function is called inside the loop, so it's called as many times as the size of the input.
        anotherFunction()
        # O(n) --> Linear Time: This operation is performed inside the loop, so it's performed as many times as the size of the input.
        stranger = True
        # O(n) --> Linear Time: This operation is also performed inside the loop, so it's performed as many times as the size of the input.
        a += 1
    # O(1) --> Constant Time: This operation does not depend on the size of the input.
    return a

# Caclulate the Big O of the above function:
# O(3 + 4n) --> Simplified to O(n) --> Linear Time


# What is the Big O of the below function? (Hint, you may want to go line by line)
def anotherFunChallenge(input):
    a = 5                    # O(1) --> Constant Time
    b = 10                  # O(1) --> Constant Time
    c = 50                # O(1) --> Constant Time
    for i in range(input):  # O(n) --> Linear Time
        x = i + 1        # O(n) --> Linear Time
        y = i + 2      # O(n) --> Linear Time
        z = i + 3   # O(n) --> Linear Time

    for j in range(input):  # O(n) --> Linear Time
        p = j * 2     # O(n) --> Linear Time
        q = j * 2   # O(n) --> Linear Time

    whoAmI = "I don't know"  # O(1) --> Constant Time

# Caclulate the Big O of the above function:
# O(4 + 7n) --> Simplified to O(n) --> Linear Time
