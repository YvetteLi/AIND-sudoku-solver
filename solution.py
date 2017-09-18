
assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [letter+number for letter in A for number in B]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]


# get the diagonal units
diag_units1 = [[rows[i] + cols[i] for i in range(0,9)]]
diag_units2 = [[rows[i] + cols[8-i] for i in range(0,9)]]

#add units to unit list
unitlist = row_units + column_units + square_units + diag_units1 + diag_units2

#units include all neighbours in neighbourhood in the form of the corresponding row, column,
#square and diagonal line of one cell
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)

#peers include all distinct neighbours in neighbourhood
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    #Assign values in memory-saving fashion
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
#    Eliminate values using the naked twins strategy.
#    Args:
#        values(dict): a dictionary of the form {'box_name': '123456789', ...}
#
#    Returns:
#        the values dictionary with the naked twins eliminated from peers.
#

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    
    for unit in unitlist:
        
        #check cell with two possible values
        all_two_possibilities = [values[box] for box in unit if len(values[box]) == 2]
        twins_set = set(all_two_possibilities)
        
        #use constraint propagation to reduce the possibilities
        for value in twins_set:
            if all_two_possibilities.count(value) == 2:
                for box in unit:
                    if values[box] != value:
                        for digit in value:
                            values[box] = values[box].replace(digit, "")
    return values



def grid_values(grid):

#    Convert grid into a dict of {square: char} with '123456789' for empties.
#    Args:
#        grid(string) - A grid in string form.
#    Returns:
#        A grid in dictionary form
#            Keys: The boxes, e.g., 'A1'
#            Values: The value in each box, e.g., '8'. If the box 
#                    has no value, then the value will be '123456789'.

    chars = []
    digits = "123456789"
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    
#    Display the values as a 2-D grid.
#    Args:
#        values(dict): The sudoku in dictionary form

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
            print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                                        for c in cols))
            if r in 'CF': print(line)
    return

def eliminate(values):
    
#When there is a cell having 1 value, eliminate the value from other boxes

    solved_values = [box for box in values.keys() if len(values[box]) == 1 ]
    for solved in solved_values:
        digit = values[solved]
        for peer in peers[solved]:
            values = assign_value(values, peer, values[peer].replace(digit,''))
    return values

def only_choice(values):
    
#If a cell has 1 fitting value, assign the value to the box
    
    for unit in unitlist:
        for num in "123456789":
            dplaces = [box for box in unit if num in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], num)
    return values


def reduce_puzzle(values):
    
#Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
#If the sudoku is solved, return the sudoku.
#If after an iteration of both functions, the sudoku remains the same, return the sudoku.

    solved_values = [box for box in values.keys() if len(values[box])==1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1 ])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
# use depth-first search and propagation, create a search tree and solve sudoku
    
    values = eliminate(values)
    values = reduce_puzzle(values)
    if values is False:
        return False #failed before this function called
    if all(len(values[s]) == 1 for s in boxes):
        return values #solved
        
    #Choose one of the unfilled squares with the fewest possibilties
    n,s = min((len(values[s]),s) for s in boxes if len(values[s])> 1)
    
    #Recurse on this function to solve each one of the resulting sudoku
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)



if __name__ == '__main__':
    #one example
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    display(solve(diag_sudoku_grid))

