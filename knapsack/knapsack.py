import sys
from typing import List, Tuple

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

print(read_file("problem16.7test.txt"))
