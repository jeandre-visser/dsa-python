def compressBoxesTwice(boxes, boxes2):
    for box in boxes:
        print(box)

    for box in boxes2:
        print(box)

# boxes and boxes2 are two different inputs, so we can't add them together. Therefore we add the complexities together.
# O(n + m) --> Linear Time
# O(n + m) is linear because it grows with the size of two different inputs n and m.
# O(2n) --> Linear Time
# O(n) --> Linear Time
# - O(2n) is also linear because it grows with the size of the input n, despite the constant factor 2.
# O(n) is the simplest form of linear time complexity, growing directly with the size of the input n.

# If the above loops were nested, the complexity would be O(n * m) --> Quadratic Time.
