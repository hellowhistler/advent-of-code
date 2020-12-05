with open('input.txt') as f:
    data = f.read().strip().splitlines()


def did_i_hit_a_tree(data, x: int, y: int) -> bool:
    # x, y are positions in the real world (assuming infinite horizontal expansion)
    row = data[y]
    index = x % len(row)
    value = row[index]
    if value == '#':
        return True
    return False


assert did_i_hit_a_tree(["####", ".###"], 0, 0) == True
assert did_i_hit_a_tree(["####", ".###"], 0, 1) == False
assert did_i_hit_a_tree(["####", ".###"], 4, 1) == False

# slopes in (x, y)
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
product_of_trees_hit = 1

for w, h in slopes:
    n = 0
    x, y = 0, 0
    while True:
        try:
            if did_i_hit_a_tree(data, x, y):
                n += 1
            x += w
            y += h
        except IndexError:
            break
    print(n, 'trees hit')
    product_of_trees_hit *= n

print(product_of_trees_hit, 'is the product')
