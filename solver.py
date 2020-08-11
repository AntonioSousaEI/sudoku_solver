
#function to print the board
def printt(b):
    for row in range(len(b)):
        if(row % 3 == 0 and row != 0):  #print a line every 3 number except on the top
            print('---------------------')
        for col in range(len(b[0])):    #print vertical bar every 3 numbers except in the first case
            if(col % 3 == 0 and col != 0):
                print('| ', end='')
            print(str(b[row][col])+' ', end ='')
        print()
    print('--------------------------')


def is_valid(b, r, c, value): #board, row, column, value for that position
    #check lines
    for row in range(len(b)):
        if(b[row][c] == value):
            return False

    #check columns
    for col in range(len(b)):
        if(b[r][col] == value):
            return False

    #check 3by 3 squares
    #implement

    #didn't faill any test
    return True

def solve(b):
    #seach empty space
    for row in range(len(b)):
        for col in range(len(b)):
            if b[row][col] == 0: #if empty
                for i in range(1,10):
                    if is_valid(b, row, col, i): #trys possibel filer for that space until he finds the first possibel
                        b[row][col] = i
                        if solve(b):            #and sends it to find the next empty space
                            return True
                b[row][col] = 0                 #if no numbers can be used on that space makes sure it's at 0 and back to previous round to be filed with an other number
                return False
    return True                                 #by this point there is no more empty spaces


# board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#          [6, 0, 0, 1, 9, 5, 0, 0, 0],
#          [0, 9, 8, 0, 0, 0, 0, 6, 0],
#          [8, 0, 0, 0, 6, 0, 0, 0, 3],
#          [4, 0, 0, 8, 0, 3, 0, 0, 1],
#          [7, 0, 0, 0, 2, 0, 0, 0, 6],
#          [0, 6, 0, 0, 0, 0, 2, 8, 0],
#          [0, 0, 0, 4, 1, 9, 0, 0, 5],
#          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]]

print('--------start--------')
printt(board)
print('--------result-------')
solve(board)
printt(board)