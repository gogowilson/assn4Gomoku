def gomoku_board():
    for i in range(15):
        print('%6d'%(i+1),end='')
    print()
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
    chess = {}
    for x in range(1, 16):
        for  y in range(1, 16):
            chess[(x, y)] = '+'

    for i in range(15*15) :
        if i%2 == 0:
            player = 'X'
        else:
            player = 'O'
        while True:
            print('Let %s choose the position of the chess' % player)
            position = input('Please enter the position (with CAPITAL letter)：')
            xpos = position[0]
            x = ord(xpos)-64
            y = int(position[1])
            if chess[(x, y)] in ['X', 'O']:
                print('Already have chess here! Please re-enter')
            else:
                break
 
        if chess[(x, y)]=="+":
            #重画棋盘
            chess[(x, y)] = player
            for i in range(15):
                print("%6d"%(i+1),end='')
            print()
            for i in range(29):
                if(i%2==0):
                    i = int((i+1)/2)
                    print(chr(i + ord('A')) + "  ", end='')
                    for j in range(53):
                        if (j%4 == 0):
                            x=int((i+3)/2)
                            y=int(j/4+1)
                            print(chess[(x,y)],end='')
                        
                        else:
                            print("-", end='')
                else:
                    print("%3s"%' ',end='')
                    for j in range(53):
                        if(j%4==0):
                            print(" |",end='')
                        else:
                            print("  ",end='')
                print()
        else:
            isture=True
            print("您输入的位置已经有子，请重新输入！")
        win()
    
def win():
    pass

def main():
    x = 0
    y = 0
    print('=========PLAY GOMOKU WITH YOUR FRIENDS !==========')
    print('Both sides use X and O respectively, X go first\nPlayers alternate in placing chess on an empty position\nThe WINNER is people who get 5 connected chess\n')
    gomoku_board()
    play()
    
if __name__ == '__main__':
    main()        
        
