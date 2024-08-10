"""
    959. Regions Cut By Slashes
    https://leetcode.com/problems/regions-cut-by-slashes/

    An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\',
    or blank space ' '. These characters divide the square into contiguous regions.

    Given the grid grid represented as a string array, return the number of regions.

    Note that backslash characters are escaped, so a '\' is represented as '\\'.

"""


def regionsBySlashes(grid):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    n = len(grid)
    parent = [i for i in range(4 * n * n)]
    for i in range(n):
        for j in range(n):
            base = 4 * (i * n + j)
            if grid[i][j] == "/":
                union(base, base + 3)
                union(base + 1, base + 2)
            elif grid[i][j] == "\\":
                union(base, base + 1)
                union(base + 2, base + 3)
            else:
                union(base, base + 1)
                union(base + 1, base + 2)
                union(base + 2, base + 3)
            if j + 1 < n:
                union(base + 1, 4 * (i * n + j + 1) + 3)
            if i + 1 < n:
                union(base + 2, 4 * ((i + 1) * n + j))
    return sum(parent[i] == i for i in range(4 * n * n))


#! --- Best ---
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        points_per_side = grid_size + 1
        total_points = points_per_side * points_per_side

        # Initialize disjoint set data structure
        parent_array = [-1] * total_points

        # Connect border points
        for i in range(points_per_side):
            for j in range(points_per_side):
                if (
                    i == 0
                    or j == 0
                    or i == points_per_side - 1
                    or j == points_per_side - 1
                ):
                    point = i * points_per_side + j
                    parent_array[point] = 0

        # Set the parent of the top-left corner to itself
        parent_array[0] = -1
        region_count = 1  # Start with one region (the border)

        # Process each cell in the grid
        for i in range(grid_size):
            for j in range(grid_size):
                # Treat each slash as an edge connecting two points
                if grid[i][j] == "/":
                    top_right = i * points_per_side + (j + 1)
                    bottom_left = (i + 1) * points_per_side + j
                    region_count += self._union(parent_array, top_right, bottom_left)
                elif grid[i][j] == "\\":
                    top_left = i * points_per_side + j
                    bottom_right = (i + 1) * points_per_side + (j + 1)
                    region_count += self._union(parent_array, top_left, bottom_right)

        return region_count

    def _find(self, parent_array: List[int], node: int) -> int:
        if parent_array[node] == -1:
            return node

        parent_array[node] = self._find(parent_array, parent_array[node])
        return parent_array[node]

    def _union(self, parent_array: List[int], node1: int, node2: int) -> int:
        parent1 = self._find(parent_array, node1)
        parent2 = self._find(parent_array, node2)

        if parent1 == parent2:
            return 1  # Nodes are already in the same set, new region formed

        parent_array[parent2] = parent1  # Union the sets
        return 0  # No new region formed


#! Approach 1: Expanded Grid
class Solution:

    # Directions for traversal: right, left, down, up
    DIRECTIONS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    def regionsBySlashes(self, grid):
        grid_size = len(grid)
        # Create a 3x3 matrix for each cell in the original grid
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]

        # Populate the expanded grid based on the original grid
        # 1 represents a barrier in the expanded grid
        for i in range(grid_size):
            for j in range(grid_size):
                base_row = i * 3
                base_col = j * 3
                # Check the character in the original grid
                if grid[i][j] == "\\":
                    # Mark diagonal for backslash
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    # Mark diagonal for forward slash
                    expanded_grid[base_row][base_col + 2] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1

        region_count = 0
        # Count regions using flood fill
        for i in range(grid_size * 3):
            for j in range(grid_size * 3):
                # If we find an unvisited cell (0), it's a new region
                if expanded_grid[i][j] == 0:
                    # Fill that region
                    self._flood_fill(expanded_grid, i, j)
                    region_count += 1

        return region_count

    # Flood fill algorithm to mark all cells in a region
    def _flood_fill(self, expanded_grid, row, col):
        queue = [(row, col)]
        expanded_grid[row][col] = 1

        while queue:
            current_cell = queue.pop(0)
            # Check all four directions from the current cell
            for direction in self.DIRECTIONS:
                new_row = direction[0] + current_cell[0]
                new_col = direction[1] + current_cell[1]
                # If the new cell is valid and unvisited, mark it and add to queue
                if self._is_valid_cell(expanded_grid, new_row, new_col):
                    expanded_grid[new_row][new_col] = 1
                    queue.append((new_row, new_col))

    # Check if a cell is within bounds and unvisited
    def _is_valid_cell(self, expanded_grid, row, col):
        n = len(expanded_grid)
        return (
            row >= 0
            and col >= 0
            and row < n
            and col < n
            and expanded_grid[row][col] == 0
        )


#! Approach 2: Disjoint Set Union (Triangles)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        total_triangles = grid_size * grid_size * 4
        parent_array = [-1] * total_triangles

        # Initially, each small triangle is a separate region
        region_count = total_triangles

        for row in range(grid_size):
            for col in range(grid_size):
                # Connect with the cell above
                if row > 0:
                    region_count -= self._union_triangles(
                        parent_array,
                        self._get_triangle_index(grid_size, row - 1, col, 2),
                        self._get_triangle_index(grid_size, row, col, 0),
                    )
                # Connect with the cell to the left
                if col > 0:
                    region_count -= self._union_triangles(
                        parent_array,
                        self._get_triangle_index(grid_size, row, col - 1, 1),
                        self._get_triangle_index(grid_size, row, col, 3),
                    )

                # If not '/', connect triangles 0-1 and 2-3
                if grid[row][col] != "/":
                    region_count -= self._union_triangles(
                        parent_array,
                        self._get_triangle_index(grid_size, row, col, 0),
                        self._get_triangle_index(grid_size, row, col, 1),
                    )
                    region_count -= self._union_triangles(
                        parent_array,
                        self._get_triangle_index(grid_size, row, col, 2),
                        self._get_triangle_index(grid_size, row, col, 3),
                    )

                # If not '\', connect triangles 0-3 and 1-2
                if grid[row][col] != "\\":
                    region_count -= self._union_triangles(
                        parent_array,
                        self._get_triangle_index(grid_size, row, col, 0),
                        self._get_triangle_index(grid_size, row, col, 3),
                    )
                    region_count -= self._union_triangles(
                        parent_array,
                        self._get_triangle_index(grid_size, row, col, 2),
                        self._get_triangle_index(grid_size, row, col, 1),
                    )

        return region_count

    # Calculate the index of a triangle in the flattened array
    # Each cell is divided into 4 triangles, numbered 0 to 3 clockwise from the top
    def _get_triangle_index(self, grid_size, row, col, triangle_num):
        return (grid_size * row + col) * 4 + triangle_num

    # Union two triangles and return 1 if they were not already connected, 0 otherwise
    def _union_triangles(self, parent_array, x, y):
        parent_x = self._find_parent(parent_array, x)
        parent_y = self._find_parent(parent_array, y)
        if parent_x != parent_y:
            parent_array[parent_x] = parent_y
            return 1  # Regions were merged, so count decreases by 1
        return 0  # Regions were already connected

    # Find the parent (root) of a set
    def _find_parent(self, parent_array, x):
        if parent_array[x] == -1:
            return x
        parent_array[x] = self._find_parent(parent_array, parent_array[x])
        return parent_array[x]


#! Approach 3: Disjoint Set Union (Graph)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        points_per_side = grid_size + 1
        total_points = points_per_side * points_per_side

        # Initialize disjoint set data structure
        parent_array = [-1] * total_points

        # Connect border points
        for i in range(points_per_side):
            for j in range(points_per_side):
                if (
                    i == 0
                    or j == 0
                    or i == points_per_side - 1
                    or j == points_per_side - 1
                ):
                    point = i * points_per_side + j
                    parent_array[point] = 0

        # Set the parent of the top-left corner to itself
        parent_array[0] = -1
        region_count = 1  # Start with one region (the border)

        # Process each cell in the grid
        for i in range(grid_size):
            for j in range(grid_size):
                # Treat each slash as an edge connecting two points
                if grid[i][j] == "/":
                    top_right = i * points_per_side + (j + 1)
                    bottom_left = (i + 1) * points_per_side + j
                    region_count += self._union(parent_array, top_right, bottom_left)
                elif grid[i][j] == "\\":
                    top_left = i * points_per_side + j
                    bottom_right = (i + 1) * points_per_side + (j + 1)
                    region_count += self._union(parent_array, top_left, bottom_right)

        return region_count

    def _find(self, parent_array: List[int], node: int) -> int:
        if parent_array[node] == -1:
            return node

        parent_array[node] = self._find(parent_array, parent_array[node])
        return parent_array[node]

    def _union(self, parent_array: List[int], node1: int, node2: int) -> int:
        parent1 = self._find(parent_array, node1)
        parent2 = self._find(parent_array, node2)

        if parent1 == parent2:
            return 1  # Nodes are already in the same set, new region formed

        parent_array[parent2] = parent1  # Union the sets
        return 0  # No new region formed
