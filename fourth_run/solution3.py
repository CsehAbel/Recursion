import copy

def is_obstacle(matrix,i,j):
    if matrix[i][j] == 'A':
        return False
    if matrix[i][j] != '.' :
        if matrix[i][j] != 'Y':
            return True
    return False

def is_not_free(matrix,i,j):
    if matrix[i][j] != '.' :
        True
    return False

def fillObscured(B):
    convert_x(B)
    for element in B:
        print(element)


def convert_x(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            if matrix[i][j] == '>':
                scan_right(i,j+1,matrix)
            elif matrix[i][j] == '<':
                scan_left(i,j-1,matrix)
            elif matrix[i][j] == '^':
                scan_top(i-1,j,matrix)
            elif matrix[i][j] == 'v':
                scan_bottom(i+1,j,matrix)

def scan_left(i,j,matrix):
    if j < 0:
        return
    if is_obstacle(matrix, i, j):
        return
    matrix[i][j] = 'Y'
    scan_left(i,j-1,matrix)

def scan_right(i,j,matrix):
    if  j > len(matrix[i])-1:
        return
    if is_obstacle(matrix,i,j):
        return
    tmp = list(matrix[i])
    tmp[j] = 'Y'
    matrix[i] = ''.join(tmp)
    scan_right(i,j+1,matrix)

def scan_bottom(i,j,matrix):
    if  i >= len(matrix):
        return
    if is_obstacle(matrix, i, j):
        return
    current = matrix[i][j]
    tmp = list(matrix[i])
    tmp[j] = 'Y'
    matrix[i] = ''.join(tmp)
    scan_bottom(i+1,j,matrix)

def scan_top(i,j,matrix):
    if i < 0:
        return
    if is_obstacle(matrix, i, j):
        return
    tmp = list(matrix[i])
    tmp[j] = 'Y'
    matrix[i] = ''.join(tmp)
    scan_top(i-1,j,matrix)


def solve(matrix):
    #we mutated the matrix with fillObscured()
    fillObscured(matrix)
    lastRowMaxIndex=matrix.__len__()-1
    lastColumnMaxIndex= matrix[lastRowMaxIndex].__len__()-1
    print(lastRowMaxIndex)
    print(lastColumnMaxIndex)
    if(matrix[lastRowMaxIndex][lastColumnMaxIndex] != "."):
        print("No solution, exit already obscured, or no route to exit")
        return
    #try to flood the mutated matrix
    solution=findRoute(matrix)
    return solution

def findRoute(matrix):
    i,j = findAssassin(matrix,0,0)
    solution = []
    findRoute2(matrix,i,j,solution,True)
    return solution

def findRoute2(matrix,i,j,solution,firstRun):
    # Check if the current cell is out of bounds or already not valid
    if( not (0<=i and matrix.__len__()-1>=i)):
        return
    if( not (0<=j and matrix[i].__len__()-1>=j)):
        return
    if(is_not_free(matrix,i,j) or matrix[i][j]=="a"):
        if(not firstRun):
            return
    #we reached bottom right corner
    if(i==len(matrix)-1 and j==len(matrix[i])-1):
        print("found a route")
        solution=copy.deepcopy(matrix)

    if matrix[i][j]!="A":
        tmp = list(matrix[i])
        tmp[j] = 'a'
        matrix[i] = ''.join(tmp)
    findRoute2(copy.deepcopy(matrix),i+1,j,solution,False)
    findRoute2(copy.deepcopy(matrix),i-1,j,solution,False)
    findRoute2(copy.deepcopy(matrix),i,j+1,solution,False)
    findRoute2(copy.deepcopy(matrix),i,j-1,solution,False)

# def findAssassin(matrix,i,j,assassinsPosition):
#     if( not (0<=i and matrix.__len__()-1>=i)):
#         return
#     if( not (0<=j and matrix[i].__len__()-1>=j)):
#         return
#     if(matrix[i][j]=="A"):
#         assassinsPosition=[i,j]
#     findAssassin(matrix,i,j+1,assassinsPosition)
#     j=0
#     findAssassin(matrix,i+1,j,assassinsPosition)

def findAssassin(matrix,i,j):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]=="A"):
                return (i,j)



    


#print(solution(["X.....>","..v..X.",".>..X..","A......"]))
#print(solution(["...Xv", "AX..^", ".XX.."]))
#print(solution(["...",">.A"]))
#input = ["A.v","..."]
#input = ["X.....>","..v..X.",".>..X..","A......"]
input = ["...Xv", "AX..^", ".XX.."]
solution=solve(input)

