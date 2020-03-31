#! /usr/bin/env python3

'''
	A program to solve Sudoku puzzles
'''

puzzle1 = [[0,0,0,0,0,0,0,3,7],
           [5,0,0,0,3,0,2,0,0],
           [0,0,0,0,0,9,0,0,5],
           [0,6,0,0,0,1,9,0,0],
           [0,0,0,8,0,0,0,4,6],
           [9,8,0,0,0,3,0,0,0],
           [0,0,3,0,5,2,0,0,8],
           [0,0,0,0,0,0,0,9,1],
           [0,1,0,0,0,0,0,0,0]]

puzzle2 = [[3,0,0,7,0,4,0,0,5],
           [0,1,2,0,3,5,0,0,0],
           [0,5,0,2,6,1,0,0,0],
           [2,8,6,1,7,0,4,5,3],
           [1,0,5,8,0,3,6,9,0],
           [9,3,0,6,5,2,8,0,1],
           [0,2,3,0,9,6,0,8,0],
           [7,9,1,5,0,8,3,6,0],
           [6,4,0,3,1,7,0,0,9]]


def sudoku(puzzle):
    def print_puzzle():
        for x in range(9):
            for y in range(9):
                print(f"{sudoku.puzzle[x][y]}", end= " ")
            print()

    def possible(x, y, n):
        if n in sudoku.puzzle[x]:
           return False
        for j in range(9):
            if sudoku.puzzle[j][y] == n:
                return False
        blkx = (x // 3) * 3
        blky = (y // 3) * 3
        for i in range(blkx, blkx+3):
            for j in range(blky, blky+3):
                if sudoku.puzzle[i][j] == n:
                    return False
        return True

    def solve(lvl=0):
        for i in range(9):
            for j in range(9):
                if sudoku.puzzle[i][j] == 0:
                    for t in range(1, 10):
                        if possible(i,j,t):
                            sudoku.puzzle[i][j] = t
                            solve(lvl=lvl+1)
                            sudoku.puzzle[i][j] = 0
                    return
        print("----------")
        print_puzzle()
        return

    import copy
    sudoku.puzzle = copy.deepcopy(puzzle)
    print_puzzle()
    solve()
    print("----------")
    print("Done")

sudoku(puzzle1)

sudoku(puzzle2)
