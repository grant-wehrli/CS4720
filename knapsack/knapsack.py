import sys
from typing import List, Tuple

# simply fill arrays with values from file
def read_file(path: str):
    with open(path, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    # capacity and num items
    capacity, num_items = map(int, lines[0].split())

    values = []
    weights = []

    # valie and weight on next line
    for i in range(1, num_items + 1):
        v, w = map(int, lines[i].split())
        values.append(v)
        weights.append(w)

    return capacity, values, weights

#print(read_file("problem16.7test.txt"))


'''pseudocode for dp table contruction
inputs: capacity (W), num items (N), values array, weights array

create array: A[0 to n][0 to W]

for x = 0 to W:
    A[0][x] = 0

for i = 1 to n:
    for x = 0 to W:
        #too large to fit
        if weights[i] > x:
            A[i][x] = A[i-1][x]
        else:
            #skip or take, x is current capacity
            skip = A[i-1][x]
            take = A[i-1][x - weights[i]] + values[i]
            
            A[i][x] = max(skip, take)

optimal value - A[n][W]
'''
def knapsack(capacity, values, weights):
    n = len(values)
    A = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for x in range(capacity + 1):
        A[0][x] = 0
    
    for i in range(1, n + 1):
        for x in range(capacity + 1):
            weight = weights[i - 1]
            value = values[i - 1]
            if weight > x:
                A[i][x] = A[i-1][x]
            else:
                skip = A[i-1][x]
                take = A[i-1][x - weight] + value
                A[i][x] = max(skip, take)

    return A[n][capacity]

capacity, values, weights = read_file("problem16.7test.txt")
print(knapsack(capacity, values, weights))
