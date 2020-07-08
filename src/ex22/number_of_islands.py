from typing import List


def num_islands(grid: List[List[str]]) -> int:
    grid = [[int(integer) for integer in ls] for ls in grid]
    result = list()
    for i, land_row in enumerate(grid):
        for j, land_col in enumerate(land_row):

            if land_col == 1:
                grid[i][j] = 0
                is_island(grid, i, j)
                result.append(i)
    return len(result)


def is_island(grid: List[List[int]], i: int, j: int) -> List[int]:
    island = list()
    island.append(i)
    if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
        grid[i][j+1] = 0
        island.extend(is_island(grid, i, j+1))
    if i + 1 < len(grid) and grid[i+1][j] == 1:
        grid[i+1][j] = 0
        island.extend(is_island(grid, i+1, j))
    if i - 1 >= 0 and grid[i-1][j] == 1:
        grid[i-1][j] = 0
        island.extend(is_island(grid, i-1, j))
    if j - 1 >= 0 and grid[i][j-1] == 1:
        grid[i][j-1] = 0
        island.extend(is_island(grid, i, j-1))
    return island
