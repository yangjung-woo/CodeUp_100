# 369 게임 

n = int(input())
li = ['3','6','9']

for i in range(1,1+n):
    Flag = False
    str_i = str(i)
    answer=''
    for s in str_i:
        if s in li:
            answer +='X'
            Flag = True

    if Flag:
        print(answer,end=' ')
    else:
        answer = i 
        print(answer,end=' ')