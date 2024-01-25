# 십자 바둑알 뒤집기

board = []

for _ in range(19):
    board.append(list(map(int,input().split())))

# 19x19 맵 생성 

n = int(input())

for _ in range(n):
    y,x = map(int,input().split())
    y = y-1
    x= x-1
    for i in range(19):
        if board[y][i] == 0:
            board[y][i] =1
        else:
            board[y][i] =0
    for j in range(19):
        if board[j][x] == 0:
            board[j][x] =1
        else:
            board[j][x] =0

for bo in board:
    for b in bo:
        print(b , end=' ')
    print()
