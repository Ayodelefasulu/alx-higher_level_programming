#!/usr/bin/python3
"""
Module: 101-nqueens

Description:
    Solves the N queens puzzle, which is the challenge of placing N non-attacking queens on an N×N chessboard.

Usage:
    ./101-nqueens.py N
        If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module

Author:
    [Your Name]
"""

import sys

def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at position (row, col).
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N):
    """
    Solve the N queens puzzle using backtracking.
    """
    if row == N:
        solution = [[r, board[r]] for r in range(N)]
        print(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)

def nqueens(N):
    """
    Main function to solve the N queens problem.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    nqueens(sys.argv[1])
