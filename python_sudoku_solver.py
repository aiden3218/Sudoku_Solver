import copy
grid = [[None,None,3,5,7,None,2,None,None],[2,9,None,1,None,3,None,None,6],[None,None,None,None,None,4,1,9,None],[None,8,2,None,3,None,None,1,7],[None,None,None,7,None,8,None,None,None,],[9,1,None,None,4,None,3,6,None],[None,2,1,4,None,None,None,None,None],[7,None,None,8,None,1,None,2,5],[None,None,5,None,9,2,6,None,None]]

"""
searches for any possible values by line horizontally and vertically
"""
def line_solver(line_segment):
    if line_segment < 9:
        possibles = set()
        for i in range(1,10):
            if i not in grid[line_segment]:
                possibles.add(i)
    else:
        possibles = set([1,2,3,4,5,6,7,8,9])
        for i in range(0,9):
            for j in range(1,10):
                if j == grid[i][line_segment-9]:
                    possibles.remove(j)
    return possibles

"""
searches for any possible values by the 3x3 squares in the grid
"""
def squares(x,y):
    possibles = set([1,2,3,4,5,6,7,8,9])
    for i in range(0,3):
        for j in range(0,3):
            if grid[i+(x*3)][j+(y*3)] in possibles:
                possibles.remove(grid[i+(x*3)][j+(y*3)])
    return possibles


"""
searches for any possible values in each square adn solves the square if there is only one potential value
"""
def potential():
    potential = []
    for i in range(9):
        potential.append([None,None,None,None,None,None,None,None,None])
    for i in range(0,9):
        for j in range(9,18):
            if grid[i][j-9] == None:

                x = line_solver(i)
                y = line_solver(j)
                final = list(squares(i//3,(j-9)//3).intersection(x.intersection(y)))

                if len(final) == 1:
                    grid[i][j-9] = final[0]
                    potential[i][j-9] = None
            else:
                potential[i][j-9] = None


def equals(duplicate):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != duplicate[i][j]:
                return False
    return True

def print_grid():
    print(grid[0])
    print(grid[1])
    print(grid[2])
    print(grid[3])
    print(grid[4])
    print(grid[5])
    print(grid[6])
    print(grid[7])
    print(grid[8])
    print(grid[8])
    print("\n")


def main():
    duplicate = []
    for i in range(9):
        duplicate.append([None,None,None,None,None,None,None,None,None])
    while not equals(duplicate):
        duplicate = copy.deepcopy(grid)
        potential()
        print_grid()

main()