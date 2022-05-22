from turtle import *
Initial=['r','f','l','l','f','r']
prev=['r','f','l','l','f','r']
final=[]
for iter in range(2):
    final = []
    for i in range(0,len(prev)):
        if(prev[i]=='f'):
            for j in range(0,len(Initial)):
                final.append(Initial[j])
        else:
            final.append(prev[i])
    prev = final

for i in range(0,len(final)):
    if(final[i] == 'r'):
        right(45)
    elif(final[i] == 'f'):
        forward(20)
    elif(final[i] == 'l'):
        left(45)

done()