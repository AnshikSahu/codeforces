from typing import Tuple, List

import time
start=time.time()
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
    """Function to take input a sudoku from stdin and return
    it as a list of lists.
    Each row of sudoku is one line.
    """
    sudoku = list()
    for _ in range(9):
        row = list(map(int, input().rstrip(" ").split(" ")))
        sudoku.append(row)
    return sudoku
def print_sudoku(sudoku: List[List[int]]) -> None:
    """Helper function to print sudoku to stdout
    Each row of sudoku in one line.
    """
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print()
# You have to implement the functions below
def get_block_num(sudoku: List[List[int]], pos: Tuple[int, int]) -> int:
    """This function takes a parameter position and returns
    the block number of the block which contains the position.
    """
    for i in range(0, 3):
        if ((3 * i) < pos[0] < (3 * i + 4)):
            p = i
        if ((3 * i) < pos[1] < (3 * i + 4)):
            q = i

    return ((3 * p) + q + 1)
# your code goes here
def get_position_inside_block(sudoku: List[List[int]], pos: Tuple[int, int]) -> int:
    """This function takes parameter position
    and returns the index of the position inside the corresponding block.
    """

    rn=(pos[0]-1)%3
    cn=(pos[1]-1)%3
    return(cn+3*rn+1)
def get_block(sudoku: List[List[int]], x: int) -> List[int]:
    """This function takes an integer argument x and then
    returns the x^th block of the Sudoku. Note that block indexing is
    from 1 to 9 and not 0-8.
    """
    list=[]
    p = int((x - 1) / 3)
    q = (x - 1) % 3
    for i in range(3 * p, 3 * p + 3):
        for j in range(3 * q, 3 * q + 3):
            list.append(sudoku[i][j])
    # your code goes here
    return list
def get_row(sudoku: List[List[int]], i: int) -> List[int]:
    """This function takes an integer argument i and then returns
    the ith row. Row indexing have been shown above.
    """
    list=[]
    for j in range(0,9):
        list.append(sudoku[i-1][j])
     # your code goes here


    # your code goes here
    return list
def get_column(sudoku: List[List[int]], x: int) -> List[int]:
    """This function takes an integer argument i and then
    returns the ith column. Column indexing have been shown above.

    """
    list=[]
    for j in range(0,9):
        list.append(sudoku[j][x-1])

    # your code goes here
    return list
def find_first_unassigned_position(sudoku: List[List[int]]) -> Tuple[int, int]:
    """This function returns the first empty position in the Sudoku.
    If there are more than 1 position which is empty then position with lesser
    row number should be returned. If two empty positions have same row number then the position
    with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
    """
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j]==0:
                return (i+1,j+1)
    # your code goes here
    return (-1, -1)
def valid_list(lst: List[int]) -> bool:
    """This function takes a lists as an input and returns true if the given list is valid.
    The list will be a single block , single row or single column only.
    A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
    """
    # your code goes here
    lst.sort()
    for i in range(0,len(lst)-1):
        if ((lst[i]!=0) and (lst[i]==lst[i+1])):
            return  False
    return True
def valid_sudoku(sudoku: List[List[int]]) -> bool:
    """This function returns True if the whole Sudoku is valid.
    """
    for i in range(0,9):
        if(valid_list(get_row(sudoku,i))==False):
            return False
        if (valid_list(get_column(sudoku, i)) == False):
            return False
        if (valid_list(get_block(sudoku, i)) == False):
            return False

    # your code goes here
    return True
def get_candidates(sudoku: List[List[int]], pos: Tuple[int, int]) -> List[int]:
    list=[]
    if (sudoku[pos[0]-1][pos[1]-1]!=0):
        list.append(sudoku[pos[0]-1][pos[1]-1])

    for i in range(1,10):
        r=True

        row1=get_row(sudoku,pos[0])
        col1=get_column(sudoku,pos[1])
        block1=get_block(sudoku,get_block_num(sudoku,pos))
        for k in range(0,9):
            if row1[k]==i:
                r=False

            if col1[k] == i:
                r = False
            if block1[k] == i:
                r = False
        if r==True:
            list.append(i)
    # your code goes here
    return list
def make_move(sudoku: List[List[int]], pos: Tuple[int, int], num: int) -> List[List[int]]:
    """This function fill `num` at position `pos` in the sudoku and then returns
    the modified sudoku.
    """
    # your code goes here
    sudoku[pos[0]-1][pos[1]-1]=num
    return sudoku
def undo_move(sudoku: List[List[int]], pos: Tuple[int, int]):
    """This function fills `0` at position `pos` in the sudoku and then returns
    the modified sudoku. In other words, it undoes any move that you
    did on position `pos` in the sudoku.
    """
    sudoku[pos[0]-1][pos[1]-1]=0
    # your code goes here
    return sudoku


"""def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
     This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns
    true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
    It return them in a tuple i.e. `(True, solved_sudoku)`.

    However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
   
 #   def changemove(sudoku: List[List[int]], pos: Tuple[int, int], num: int) -> List[List[int]]:
  #      sudoku[pos[0]-1][pos[1]-1]=num

    pos=find_first_unassigned_position(sudoku)
    cand=get_candidates(sudoku,pos)

    while(pos!=(-1,-1)):

        for i in range(len(cand)):

            make_move(sudoku,pos,cand[i])
            #print_sudoku(sudoku)
            oldpos=pos
            oldcand=cand
            pos = find_first_unassigned_position(sudoku)
            cand = get_candidates(sudoku, pos)
            if len(cand)==0:
                undo_move(sudoku,oldpos)
                pos=oldpos
                cand=oldcand



# your code goes here

    # to complete this function, you may define any number of helper functions.
    # However, we would be only calling this function to check correctness.

    return (False, sudoku)


# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you
# submit your code since it may result in undefined behaviour of the autograder.
"""
'''
def in_lab_component(sudoku: List[List[int]]):
    print("Testcases for In Lab evaluation")
    print("Get Block Number:")
    print(get_block_num(sudoku, (4, 4)))
    print(get_block_num(sudoku, (7, 2)))
    print(get_block_num(sudoku, (2, 6)))
    print("Get Block:")
    print(get_block(sudoku, 3))
    print(get_block(sudoku, 5))
    print(get_block(sudoku, 9))
    print("Get Row:")
    print(get_row(sudoku, 3))
    print(get_row(sudoku, 5))
    print(get_row(sudoku, 9))
    print("Get Column:")
    print(get_column(sudoku, 3))
    print(get_column(sudoku, 5))
    print(get_column(sudoku, 9))
    print(find_first_unassigned_position(sudoku))
    print(valid_list(sudoku[0]))
    print(valid_sudoku(sudoku))
    print('d')
    print(get_candidates(sudoku,(9,9)))
    for i in range(0,9):
        for j in range(0,9):
            print(get_position_inside_block(sudoku,(i+1,j+1)))'''


'''def sudoku_solver(sudoku):
    list=[]
    pos=find_first_unassigned_position(sudoku)
    list.append([pos,0])
    while(pos!=(-1,-1)):
        if(len(list)==0):
            return (False,[])
        possible=get_candidates(sudoku,list[-1][0])
        if(list[-1][1]>=len(possible)):
            sudoku=undo_move(sudoku,list[-1][0])
            list.pop(-1)
        else:
            sudoku=make_move(sudoku,list[-1][0],possible[list[-1][1]])
            list[-1][1]+=1
            pos=find_first_unassigned_position(sudoku)
            list.append([pos,0])
    return (True,sudoku)'''
def sudoku_solver(sudoku):
    list=[]
    list.append([find_first_unassigned_position(sudoku),0])
    while(list[-1][0!=(-1,-1)]):
        p=get_candidates(sudoku,list[-1][0])
        if(list[-1][-1]>=len9(p)):
            sudoku[list[-1][0][0]-1][list[-1][0][1]-1]=0
            list.pop(-1)
        else:
            sudoku[list[-1][0][0]-1][list[-1][0][1]-1]=p[list[-1][1]]
            list[-1][1]+=1
            list.append([find_first_unassigned_position(sudoku,0)])
        if len(list)==0:
            return False
    return(True,sudoku)
#print(sudoku_solver())
#def sudoku_solver(sudoku):


# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

    # Input the sudoku from stdin
    sudoku = input_sudoku()

    # Try to solve the sudoku
    possible, sudoku = sudoku_solver(sudoku)

    # The following line is for the in-lab component
#    in_lab_component(sudoku)
    # Show the result of the same to your TA to get your code evaulated

    # Check if it could be solved
    if possible:
        print("Found a valid solution for the given sudoku :)")
        print_sudoku(sudoku)

    else:
        print("The given sudoku cannot be solved :(")
        print_sudoku(sudoku)
