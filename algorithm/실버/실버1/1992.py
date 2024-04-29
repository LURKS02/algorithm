def compress_quad_tree(grid, x, y, size):
    if size == 1:
        return grid[x][y]

    half_size = size // 2
    parts = [
        compress_quad_tree(grid, x, y, half_size),
        compress_quad_tree(grid, x, y + half_size, half_size),
        compress_quad_tree(grid, x + half_size, y, half_size),
        compress_quad_tree(grid, x + half_size, y + half_size, half_size),
    ]

    if all(part in '01' and part == parts[0] for part in parts):
        return parts[0]
    else:
        return "(" + "".join(parts) + ")"

def quad_tree_compression(grid):
    N = len(grid)
    return compress_quad_tree(grid, 0, 0, N)

N = int(input())

l = []

for _ in range(N):
    l.append([num for num in input()])

compression_result = quad_tree_compression(l)
print(compression_result)