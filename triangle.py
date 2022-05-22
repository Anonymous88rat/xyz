from turtle import *
color('green', 'blue')
begin_fill()
Initial=['f','-','g','-','g']
prev=Initial.copy()
final=[]
rule1=['f','-','g','+','f','+','g','-','f']
rule2=['g','g']
for iter in range(4):
    final = []
    for i in range(0,len(prev)):
        if(prev[i]=='f'):
            for j in range(0,len(rule1)):
                final.append(rule1[j])
        elif(prev[i]=='g'):
            for j in range(0,len(rule2)):
                final.append(rule2[j])
        else:
            final.append(prev[i])
    prev = final

print(final)

for i in range(0,len(final)):
    if(final[i] == '+'):
        right(120)
    elif(final[i] == 'f' or final[i]=='g'):
        forward(20)
    elif(final[i] == '-'):
        left(120)


end_fill()
done()