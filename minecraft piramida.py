x=int(input())
M=[]
k=0
for i in range(x,0,-2):
    k+=1
    M.append(i)
M.reverse()
s=0
for j in M:
    s += j*j
    print(k,' ',j,'x',j,'слой:',j*j)
    k-=1
print('всего блоков:',s,'полных стаков:',s//64,'и ещё:',s%64)
