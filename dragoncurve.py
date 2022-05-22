from turtle import *
color('red')
Initial=['F','X']
prev=['F','X']
final=[]
x_app = ['X','+','Y','F','+']
y_app = ['-','F','X','-','Y']

for iter in range(7):
    final = []
    for i in range(0,len(prev)):
        if(prev[i]=='X'):
            for j in range(0,len(x_app)):
                final.append(x_app[j])
        elif(prev[i]=='Y'):
            for j in range(0,len(y_app)):
                final.append(y_app[j])
        else:
            final.append(prev[i])
    prev = final

#print(ans)

for i in range(0,len(final)):
    if(final[i] == '+'):
        right(90)
    elif(final[i] == '-'):
        left(90)
    elif(final[i] == 'F'):
        forward(20)

done()