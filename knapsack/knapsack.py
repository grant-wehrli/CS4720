from typing import List

# simply fill arrays with values from file
def read_file(path: str):
    with open(path, "r") as file:
        lines = [line.strip() for line in file]

    # capacity and number of items
    capacity, num_items = map(int, lines[0].split())

    values: List[int] = []
    sizes: List[int] = []  

    # value and size on each following line
    for i in range(1, num_items + 1):
        v, s = map(int, lines[i].split())
        values.append(v)
        sizes.append(s)

    return capacity, values, sizes

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
    # initalize list
    # A[i][c] is equal to the best value using first i items and capacity c
    A = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # subproblems, filled according to the book example code
    for i in range(1, n + 1):
        # no need to fill with 0 sice already done when declaring

        # size and value of item i
        # to match the book exmaple create s_i and v_i (i - 1 since using 0 indexed lists instead of 1 like the book)
        s_i = sizes[i - 1]
        v_i = values[i - 1]
        
        # must test all capacity from 0 to capacity
        for c in range(capacity + 1):
            # is it too large to fit?
            if s_i > c:
                A[i][c] = A[i - 1][c]
            # if not is taking or leaving better?
            else:
                skip = A[i - 1][c]
                take = A[i - 1][c - s_i] + v_i
                A[i][c] = max(skip, take)
    # full dp table
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
    # reconstructed list S init to False
    # if S[i] = True we took it
    S = [False] * n
    c = capacity
    
    # count back from n through dp table to 1
    for i in range(n, 0, -1):
        # to format like the book
        v_i = values[i - 1]
        s_i = sizes[i - 1]
        
        # aboslute mess of an if statment 
        # does the item fit? and is taking it as least as good (or better)?
        if s_i <= c and A[i - 1][c - s_i] + v_i >= A[i - 1][c]:
            # set that we took it if true
            S[i - 1] = True
            # update capacity
            c = c - s_i

    # full reconstructed list
    return S

def print_results(capacity, values, sizes, A, selections, print_array: bool = True):
    n = len(values)

    # values
    print("Values")
    for v in values:
        print(v)
    # sizes
    print("Sizes")
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
    print("Selections")
    for i, s in enumerate(selections, start=1):
        print(f"{i}: {'true' if s else 'false'}")

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
print_results(capacity, values, sizes, A, selections, print_array = False)

