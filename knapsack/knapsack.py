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
inputs: capacity (C), values array, weights array

create array: A[0 to n][0 to C]

# basecase  i = 0
for x = 0 to C:
    A[0][c] = 0

    # subproblems
for i = 1 to n:
    for c = 0 to C:
        #too large to fit
        if weights[i] > c:
            A[i][c] = A[i-1][c]
        else:
            #skip or take, c is current capacity
            skip = A[i-1][c]
            take = A[i-1][c - weights[i]] + values[i]
            A[i][c] = max(skip, take)

optimal value - A[n][W]
'''
def knapsack(capacity, values, sizes):
    n = len(values)
    A = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        size_i = sizes[i - 1]
        value_i = values[i - 1]
        for c in range(capacity + 1):
            if size_i > c:
                A[i][c] = A[i - 1][c]
            else:
                skip = A[i - 1][c]
                take = A[i - 1][c - size_i] + value_i
                A[i][c] = max(skip, take)

    return A

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
            c = c - s_i

    return S

def print_results(capacity, values, sizes, A, selections, print_array: bool = True):
    n = len(values)

    # values
    print("Values")
    for v in values:
        print(v)
    # sizes
    print("Values")
    for s in sizes:
        print(s)

    # print array (if specified)
    if print_array:
        print("Array")
        # print from n to 0, each row just like the example
        for i in range(n, -1, -1):
            row = " ".join(str(A[i][c]) for c in range(capacity + 1))
            print(row)

    # selections
    for i in selections:
        print(f"{i+1}: {selections[i]}")

    # total optimal value
    print(f"Total Optimal Value: {A[n][capacity]}")
    


# testing

# book example
capacity, values, sizes = read_file("book_example.txt")
A = knapsack(capacity, values, sizes)
selections = reconstruct(A, values, sizes, capacity)
print_results(capacity, values, sizes, A, selections)

# class example
capacity, values, sizes = read_file("class_example.txt")
A = knapsack(capacity, values, sizes)
selections = reconstruct(A, values, sizes, capacity)
print_results(capacity, values, sizes, A, selections)

# large book example
capacity, values, sizes = read_file("problem16.7test.txt")
A = knapsack(capacity, values, sizes)
selections = reconstruct(A, values, sizes, capacity)
print_results(capacity, values, sizes, A, selections)

