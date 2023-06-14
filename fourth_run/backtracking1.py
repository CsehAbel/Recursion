############
#          # 
########## #
##########+#

#reach +
#store the path which leads to +
#store it by replacing the whitespace characters with *
#go from whitespace to whitespace leaving * behind
#what does that mean? entering into a stackframe set i:int and j:int to i+1,j+1, so that i takes up the value i+1, j takes up the value j+1

#we are goint to have a starting value for i,j
from typing import List

    ############
               # 
    ########## #
    ##########+#
    #this is our board
def leaveCrumbles(i:int,j:int,board:List[List[int]])->None:
    #we start here, check if board[i][j], check if this indexed value is within bounds
    #we need to check if i,j is valid index
    if 0<=i<=10 and 0<=j<=10:
        if board[i][j]=="#":
            return False
        elif board[i][j]=="X":
            return True
            #if we reach + we return True, if we reach # we return False, if we reach whitespace we continue
        elif board[i][j]==" ":
            pass
        elif board[i][j]=="*":
            return False
    #we need to check if we are at the end of the board, if we are at the end of the board we return False
    else:
        return False
    #we will only return True if the board[i][j] in case of the very first call is "+" , if board[0][0] is "+", we will return True, otherwise we will only return True if
    #if we didnt return False or True at this point, we can replace the whitespace with a *
    board[i][j]="*"
    #try and go
    #this variable returns True, it will, if inside the while loop one of the functions returns True, 
    # and those will only return True if for their respective i,j values the board[i][j] is "+" 
    # or in their stackframe 
    # inside the while loop one of the functions returns True
    # and those will only return True if for their respective i,j values the board[i][j] is "+"
    # or in their stackframe
    # inside the while loop one of the functions returns True
    # and .... and so on
    result=False
    
   
    south=leaveCrumbles(i+1,j,board)
    north=leaveCrumbles(i-1,j,board)
    east=leaveCrumbles(i,j+1,board)
    west=leaveCrumbles(i,j-1,board)

    result = south or north or east or west

    #if none of the directions return True, they won't eventually find a +, we should not go that way and not leave breadcrumbs leading to a dead end, we need to replace the * with a whitespace
    if result==False:
        board[i][j]=" "

    return result
    #if our result is false, we should try the other directions, if our result is True we should also return True, which will be assigned to a variable, this return value will be assigned to a result variable
    #lets make sure that only one result variable will be filled with our True or False return value

#we need to call another function inside main() which calls leaveCrumbles(i,j) like so
def main1():
    # the function also needs the board to read values from and write values to
    # that will be a 
    #board=int[10]
    #intialize the board
    board=[None]*10
    ############
               # 
    ########## #
    ##########+#
    #initialize the labrynth above in a 2d list
    board[0]=[x for x in "############"]
    board[1]=[x for x in "           #"]
    board[2]=[x for x in "########## #"]
    board[3]=[x for x in "##########+#"]
    board[4]=[x for x in "            "]
    board[5]=[x for x in "            "]
    board[6]=[x for x in "            "]
    board[7]=[x for x in "            "]
    board[8]=[x for x in "            "]
    board[9]=[x for x in "            "]

    #pass the board to the function, the board will need to be have its whitespaces overwritten to * characters
    leaveCrumbles(1,0,board)
    #printing board will be the expected result
    #print board:
    for row in board:
        print("".join(row))

def main2():
    #intialize the board
    board=[None]*10
    ##################################


# #         #    #     #  #   X#X#


#  ##### #### ##   ##  #  # ###  #


#  ##  #    #  ## ##  #  #     # #


#    #  ###  # ## ##   #   ### # #


# #   ####     ##  ##     ###  # #


####   #     ####     #  # ####  #


######   #########   ##   # ###  #


##     #  X X####X #  #  # ###  ##


##################################
    #initialize the labrynth above in a 2d list
    board[0]=[x for x in "##################################"]
    board[1]=[x for x in "#         #      #     #  #   X#X#"]
    board[2]=[x for x in "#  ##### #### ##   ##  #  # ###  #"]
    board[3]=[x for x in "#  ##  #    #  ## ##  #  #     # #"]
    board[4]=[x for x in "#    #  ###  # ## ##   #   ### # #"]
    board[5]=[x for x in "# #   ####     ##  ##     ###  # #"]
    board[6]=[x for x in "####   #     ####     #  # ####  #"]
    board[7]=[x for x in "######   #########   ##   # ###  #"]
    board[8]=[x for x in "##     #  X X####X #  #  # ###  ##"]
    board[9]=[x for x in "##################################"]

    #pass the board to the function, the board will need to be have its whitespaces overwritten to * characters
    leaveCrumbles(1,1,board)
    #printing board will be the expected result
    #print board:
    for row in board:
        print("".join(row))

if __name__=="__main__":
    #Lets have another test case
    #main1()
    main2()
