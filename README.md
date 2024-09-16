# Sudoku_Solver
This is a basic Sudoku solver with 2 main functions line_solver() and Squares()

line_solver finds all the possible numbers for each empty square with respect to the rows and columns
Squares finds all the possible numbers for each empty square with respect to the 3x3 squares

Potential() simply runs the two other functions together and fills any empty spaces if there is only one possible number

main() runs potential in a loop until the grid is finished, for the case in the code it only takes 4 times

This solver can not solve all Sudokus as it can not solve multiple potential sequences, it must find spots with only one
possible value for it to replace the value
