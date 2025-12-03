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
def knapsack(capacity, values, sizes):
    n = len(values)
    A = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for x in range(capacity + 1):
        A[0][x] = 0
    
    for i in range(1, n + 1):
        for x in range(capacity + 1):
            size = sizes[i - 1]
            value = values[i - 1]
            if size > x:
                A[i][x] = A[i-1][x]
            else:
                skip = A[i-1][x]
                take = A[i-1][x - size] + value
                A[i][x] = max(skip, take)

    return A[n][capacity]

capacity, values, sizes = read_file("problem16.7test.txt")
print(knapsack(capacity, values, sizes))

'''reconstruct knapsack contents pseudocode
   s[1 to n] init to false

   input: the array A computed by the Knapsack
algorithm with item values v1, v2, . . . , vn, item sizes
s1, s2, . . . , sn, and knapsack capacity C.
Output: an optimal knapsack solution.
S := False ; // items in an optimal solution
c := capacity // remaining capacity
for i := n downto 1 do
if s_i < c and A[i - 1][c - s_i] + v_i  A[i - 1][c] then
S := S union {i} // Case 2 wins, include i
c := c - s_i // reserve space for it
// else skip i, capacity stays the same
return S

'''
def reconstruct(A, values, sizes,capacity):
    n = len(values)
    # false arr S
    S = [False] * n
    c = capacity

    for i in range(n, 0, -1):
        v_i = values[i - 1]
        s_i = sizes[i - 1]
        
        if s_i <= c and A[i - 1][c - s_i] + v_i >= A[i - 1][c]:
            S[i - 1] = True
            x = x - s_i

    return S

