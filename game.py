
from termcolor import colored

class board:
    b=[
    [ 4,0,0,1,1,1,1,1,0,0,4 ],
    [0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0], 
    [1,0,0,0,0,2,0,0,0,0,1],
    [1,0,0,0,2,2,2,0,0,0,1],
    [1,1,0,2,2,3,2,2,0,1,1],
    [1,0,0,0,2,2,2,0,0,0,1],
    [1,0,0,0,0,2,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0],
    [4,0,0,1,1,1,1,1,0,0,4],
    ]
    
    
    def printboard(self):
        for i in self.b:
            for j in i:
                if j == 1:
                    print(colored(' 1 ', 'blue', 'on_green'), end='')
                elif j ==0:
                    print(colored(' 0 ', 'white'), end='')
                elif j == 2:
                    print(colored(' 2 ', 'white', 'on_red'), end='')
                elif j == 3:
                    print(colored(' 3 ', 'red', 'on_yellow'), end='')
                elif j == 4:
                    print(colored(' 4 ', 'blue', 'on_white'), end='')
            print(" "+str(j)+" ", end='')
            print()        
    # def printboard(self):
    #     for i in self.b:
    #         for j in i:
    #             print(" "+str(j)+" ", end='')
    #         print()
    
    
r = board.b
            
def positionchange():
    black = 2
    white = 1
    king = 3
    player = input("Who is moving? 1 = white; 2 = black and 3 = King        ")
    posini1 = int(input("Enter the position you want to move on x axes      "))
    posini2 = int(input("Enter the position you want to move on y axes      "))
    posfi1 = int(input("Where do you want to move on x axes?        "))
    posfi2 = int(input("Where do you want to move on x axes?        "))
    if r[posfi1][posfi2] <= 0 or r[posfi1][posfi2] == 4  :
        p = posini1+posini2 
        c = player 
        t = r[posfi1][posfi2]
        p = c 
        r[posini1][posini2] = 0
        r[posfi1][posfi2] = c
        b1.printboard()
        if t == 4:
            print("KING RULES")
            exit()
    else:
        print("Invalid Move fucking asshole")


if __name__ == "__main__":
    stop = None
    while stop != "exit":
        b1 = board()
        b1.printboard()    
        print("---------------------------------------------------------------------------")
        positionchange()
        print()
        stop = input("To exit the game enter exit. if not just press enter.")
        