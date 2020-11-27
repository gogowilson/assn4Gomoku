import sys
def gomoku_board(): #initialize the chessboard
    print('     1     2     3     4     5     6     7     8     9    10    11    12    13    14    15')
    for i in range(29):
        if(i%2==0):
            i = int((i+1)/2)
            print(chr(i + ord('A')) + '   ',end ='')
            for j in range(53):
                if (j%4 == 0):
                    print('+', end='')
                else:
                    print('-', end='')
        else:
            print('%3s'%' ',end='')
            for j in range(53):
                if(j%4==0):
                    print(' |',end='')
                else:
                    print('  ',end='')
        print()

def play():
    global chess
    chess = {}   #This section refers to CDSN
    for x in range(16):
        for  y in range(16):
            chess[(x, y)] = '+'

    for i in range(15*15) :
        if i%2 == 0:
            player = 'X'
        else:
            player = 'O'
        print('Let %s choose the position of the chess' % player)
        
        while True:
            position = input('Please enter the position (with CAPITAL letter)：')
            xpos = position[0]
            x = ord(xpos)-64
            y = int(position[1])
            if chess[(x, y)] in ['X', 'O']:
                print('Already have chess here! Please re-enter')
            else:
                break
 
        # here we should reprint chessborad
       # most same as gomoku_board but need to change to chess so copy and edit
        if chess[(x, y)]=='+':
            chess[(x, y)] = player
            print('     1     2     3     4     5     6     7     8     9    10    11    12    13    14    15')
            for i in range(29):
                if(i%2==0):
                    i = int((i+1)/2)
                    print(chr(i + ord('A')) + '  ', end='')
                    for j in range(53):
                        if (j%4 == 0):
                            x= i +1
                            y=int(j/4+1)
                            print(chess[(x,y)],end='')
                        else:
                            print('-', end='')
                else:
                    print("%3s"%' ',end='')
                    for j in range(53):
                        if(j%4==0):
                            print(' |',end='')
                        else:
                            print("  ",end='')
                print()
        
        win(player)
    
def win(player):
    global chess
    #find a structure for 16x16 board and based on this to programming
    #if j<=11:
       #if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4]: whowin(i,j)
    
    for i in range(1, 12):
        for j in range(1, 16):
            if (chess[(i, j)] == chess[(i + 1, j)] == chess[(i + 2, j)] == chess[(i + 3, j)] == chess[(i + 4, j)] 
                and chess[(i, j)] in ["X", "O"]):
                
                result(i,j)
                
         
    for i in range(1, 12):
        for j in range(1, 12):
            if (chess[(i, j)] == chess[(i + 1, j + 1)] == chess[(i + 2, j + 2)] == chess[(i + 3, j + 3)] == chess[(i + 4, j + 4)] 
                and chess[(i, j)] in ["X", "O"]):
                
                result(i,j)
                
    for i in range(1, 12):
        for j in range(5, 16):
            if (chess[(i, j)] == chess[(i +1, j - 1)] == chess[(i + 2, j - 2)] == chess[(i + 3, j - 3)] == chess[(i + 4, j - 4)]
                and chess[(i, j)] in ["X", "O"]):
              
                result(i,j)
             
    for i in range(1, 16):
        for j in range(1, 12):
            if (chess[(i, j)] == chess[(i, j + 1)] == chess[(i, j + 2)] == chess[(i, j + 3)] == chess[(i, j + 4)] 
                and chess[(i, j)] in ["X", "O"]):
                
                result(i,j)
                

def result(i,j):
    global chess
    # from now cannot find a best way to exit game
    if chess[(i,j)] == 'X':
        print('X win!\nGAME OVER, BYE!')
        sys.exit(0)
    else:
        print('O win!\nGAME OVER, BYE!')
        sys.exit(0)
    
            
def main():
    print('=========PLAY GOMOKU WITH YOUR FRIENDS !==========')
    print('Both sides use X and O respectively, X go first\nPlayers alternate in placing chess on an empty position\nThe WINNER is people who get 5 connected chess\n')
    gomoku_board()
    play()
    
if __name__ == '__main__':
    main()        
        
