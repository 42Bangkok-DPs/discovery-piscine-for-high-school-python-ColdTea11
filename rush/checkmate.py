#!/usr/bin/env python3
from main import *

def Check(board):
    size = len(board)
    king_pos = None

    # Find the position of the King
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        return "Error: King not found"

    king_row, king_col = king_pos

    # Check for threats from Pawns, Rooks, Bishops, Queens
    directions = {
        'P': [(1, -1), (1, 1)],  # Pawns attack diagonally forward
        'R': [(0, 1), (1, 0), (0, -1), (-1, 0)],  # Rook moves
        'B': [(1, 1), (1, -1), (-1, -1), (-1, 1)],  # Bishop moves
        'Q': [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)],  # Queen moves
    }

    for piece, moves in directions.items():
        for move in moves:
            x, y = king_row, king_col
            while True:
                x += move[0]
                y += move[1]
                if x < 0 or x >= size or y < 0 or y >= size:
                    break  # Out of bounds
                if board[x][y] != '.':
                    if board[x][y] == piece or (piece == 'P' and board[x][y] == 'P'):
                        print("Success")
                        return
                    break  # Another piece blocks the path

    print("Fail")