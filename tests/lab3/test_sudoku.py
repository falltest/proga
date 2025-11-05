import unittest
import tempfile
import pathlib
import os

from src.lab3.sudoku import (
    create_grid, group, get_row, get_col, get_block,
    find_empty_positions, find_possible_values, solve,
    check_solution, generate_sudoku, read_sudoku
)


class TestCreateGrid(unittest.TestCase):
    """Тесты для функции create_grid"""

    def test_create_grid_simple(self):
        puzzle = "123456789" * 9
        grid = create_grid(puzzle)
        self.assertEqual(len(grid), 9)
        self.assertEqual(len(grid[0]), 9)

    def test_create_grid_with_dots(self):
        puzzle = "1234567.9" * 9
        grid = create_grid(puzzle)
        self.assertEqual(grid[0][7], '.')

    def test_create_grid_ignores_other_chars(self):
        puzzle = "123abc456def789" + "." * 72
        grid = create_grid(puzzle)
        self.assertEqual(grid[0][:3], ['1', '2', '3'])


class TestGroup(unittest.TestCase):
    """Тесты для функции group"""

    def test_group_basic(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_group_by_three(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_group_strings(self):
        self.assertEqual(group(['a', 'b', 'c', 'd'], 2),
                         [['a', 'b'], ['c', 'd']])


class TestGetRow(unittest.TestCase):
    """Тесты для функции get_row"""

    def test_get_row_first(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_row(grid, (0, 0)), ['1', '2', '.'])

    def test_get_row_middle(self):
        grid = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        self.assertEqual(get_row(grid, (1, 0)), ['4', '.', '6'])

    def test_get_row_last(self):
        grid = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        self.assertEqual(get_row(grid, (2, 0)), ['.', '8', '9'])


class TestGetCol(unittest.TestCase):
    """Тесты для функции get_col"""

    def test_get_col_first(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_col(grid, (0, 0)), ['1', '4', '7'])

    def test_get_col_middle(self):
        grid = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        self.assertEqual(get_col(grid, (0, 1)), ['2', '.', '8'])

    def test_get_col_last(self):
        grid = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        self.assertEqual(get_col(grid, (0, 2)), ['3', '6', '9'])


class TestGetBlock(unittest.TestCase):
    """Тесты для функции get_block"""

    def test_get_block_top_left(self):
        grid = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
                ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
                ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
                ['5', '6', '7', '8', '9', '1', '2', '3', '4'],
                ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
                ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
                ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
        self.assertEqual(get_block(grid, (0, 0)),
                         ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_get_block_middle(self):
        grid = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
                ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
                ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
                ['5', '6', '7', '8', '9', '1', '2', '3', '4'],
                ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
                ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
                ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
        self.assertEqual(get_block(grid, (4, 4)),
                         ['5', '6', '7', '8', '9', '1', '2', '3', '4'])

    def test_get_block_bottom_right(self):
        grid = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
                ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
                ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
                ['5', '6', '7', '8', '9', '1', '2', '3', '4'],
                ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
                ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
                ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
        self.assertEqual(get_block(grid, (8, 8)),
                         ['9', '1', '2', '3', '4', '5', '6', '7', '8'])


class TestFindEmptyPositions(unittest.TestCase):
    """Тесты для функции find_empty_positions"""

    def test_find_empty_positions_first(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(find_empty_positions(grid), (0, 2))

    def test_find_empty_positions_middle(self):
        grid = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        self.assertEqual(find_empty_positions(grid), (1, 1))

    def test_find_empty_positions_none(self):
        grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(find_empty_positions(grid), (-1, -1))


class TestFindPossibleValues(unittest.TestCase):
    """Тесты для функции find_possible_values"""

    def test_find_possible_values_simple(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        values = find_possible_values(grid, (0, 2))
        self.assertEqual(values, {'3'})

    def test_find_possible_values_empty_grid(self):
        grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        values = find_possible_values(grid, (0, 0))
        self.assertEqual(values, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})

    def test_find_possible_values_one_option(self):
        grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '.', '9']]
        values = find_possible_values(grid, (2, 1))
        self.assertEqual(values, {'8'})


class TestCheckSolution(unittest.TestCase):
    """Тесты для функции check_solution"""

    def test_check_solution_valid(self):
        grid = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
                ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
                ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
                ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        self.assertTrue(check_solution(grid))

    def test_check_solution_invalid_duplicate(self):
        grid = [['1', '1', '3', '4', '5', '6', '7', '8', '9'],
                ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
                ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
                ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
                ['5', '6', '7', '8', '9', '1', '2', '3', '4'],
                ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
                ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
                ['9', '2', '2', '3', '4', '5', '6', '7', '8']]
        self.assertFalse(check_solution(grid))


class TestGenerateSudoku(unittest.TestCase):
    """Тесты для функции generate_sudoku"""

    def test_generate_sudoku_40_filled(self):
        grid = generate_sudoku(40)
        count = sum(1 for row in grid for e in row if e == '.')
        self.assertEqual(count, 41)

    def test_generate_sudoku_full(self):
        grid = generate_sudoku(81)
        count = sum(1 for row in grid for e in row if e == '.')
        self.assertEqual(count, 0)
        self.assertTrue(check_solution(grid))

    def test_generate_sudoku_empty(self):
        grid = generate_sudoku(0)
        count = sum(1 for row in grid for e in row if e == '.')
        self.assertEqual(count, 81)


class TestSolve(unittest.TestCase):
    """Тесты для функции solve"""

    def test_solve_empty_grid(self):
        grid = [['.' for _ in range(9)] for _ in range(9)]
        result = solve(grid)
        self.assertIsNotNone(result)
        self.assertTrue(check_solution(result))

    def test_solve_already_solved(self):
        grid = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
                ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
                ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
                ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
                ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        result = solve(grid)
        self.assertEqual(result, grid)

    def test_solve_partial_grid(self):
        grid = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
        result = solve(grid)
        self.assertIsNotNone(result)
        self.assertTrue(check_solution(result))


class TestReadSudoku(unittest.TestCase):
    """Тесты для функции read_sudoku"""

    def test_read_sudoku_basic(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write('123456789' * 9)
            fname = f.name
        try:
            grid = read_sudoku(fname)
            self.assertEqual(len(grid), 9)
            self.assertEqual(len(grid[0]), 9)
        finally:
            os.unlink(fname)

    def test_read_sudoku_pathlib(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write('53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79')
            fname = f.name
        try:
            grid = read_sudoku(pathlib.Path(fname))
            self.assertEqual(len(grid), 9)
            self.assertEqual(grid[0][0], '5')
            self.assertEqual(grid[0][2], '.')
        finally:
            os.unlink(fname)


if __name__ == '__main__':
    unittest.main()