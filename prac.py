days=['sun','mon']
time=['8am','9am']
a=list(map(str,input().split()))
# print(a)
m=[]
for x in a:
    if x in days:
        m.append(x)
    elif x in time:
        m.append(x)
        # if x in time:
print(m)
