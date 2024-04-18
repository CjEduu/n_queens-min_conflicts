"""MINIMUM CONFLICTS ALGORITHM IMPLEMENTED FOR N-QUEENS"""

from row import Row
from random import randint
from board import fill_board,print_board

# CREATE INITAL RANDOM TABLE

def create_initial_table(size:int) -> list[Row]:
    table = list()
    for _ in range(size):
        queen_pos = randint(0,size-1)
        row = Row(queen_pos,size)
        table.append(row)
        
    table = evaluate_conflicts(table)    
    return table

def create_next_table(table:list[Row],size:int)->list[Row]:
    new_table:list[Row] = list()
    for old_row in table:
        new_table.append(Row(old_row.queen_in,size))
    new_table = evaluate_conflicts(new_table)    
    return new_table
   
def solution(table:list[Row])->bool:
    sol = True
    for row in table:
        if row.conflict_values[row.queen_in] != 0:
            sol = False
    return sol

def evaluate_conflicts(table:list[Row]) -> list[Row]:
    table_copy = table
    for i,row in enumerate(table_copy): # ROW TO EVALUATE CONFLICTS IN
        for j,moving_row in enumerate(table_copy): # ROWS THAT GENERATE CONFLICTS
            if (i != j):
                vertical_conflict = moving_row.queen_in  # VERTICAL CONFLICTS 
                diagonal_conflict1 = moving_row.queen_in + (j-i)  #x=y conflicts
                diagonal_conflict2 = moving_row.queen_in - (j-i)  # x=-y conflicts
                
                row.conflict_values[vertical_conflict] += 1
                if  0 <= diagonal_conflict1 <= len(row.conflict_values)-1:
                    row.conflict_values[diagonal_conflict1] += 1 
                if  0 <= diagonal_conflict2 <= len(row.conflict_values)-1:
                    row.conflict_values[diagonal_conflict2] += 1 
    return table_copy 

def min_conflicts(table: list[Row],max_steps:int,size:int )-> list[Row]:
    current = table
    for _ in range(max_steps):
        if solution(current):
            return current
        random_index = randint(0,size-1)                # choose a random variable
        min_conflict_val = min(current[random_index].conflict_values) # search the min conflict value in the domain
        while current[random_index].conflict_values[current[random_index].queen_in] < min_conflict_val:
            random_index = randint(0,size-1)                # choose a random variable
            min_conflict_val = min(current[random_index].conflict_values) # search the min conflict value in the domain
        
        new_queen_pos = current[random_index].conflict_values.index(min_conflict_val) # select the min_conflict value in de domain of the variable
        current[random_index].new_queen_value(new_queen_pos)
        current = create_next_table(current,size)    
    return None

def n_queens(size:int,max_steps:int) -> None:
    try:    
        print("Starting")
        problem = create_initial_table(size)
        solution = min_conflicts(problem,max_steps,size)
        if solution is None:
            print(f"Couldn't find solution in {max_steps} steps")
        else:
            board = fill_board(solution,size)
            print_board(board)
    except KeyboardInterrupt:
        print("Exiting...")