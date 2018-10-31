days=['sun','mon']
time=['8am','9am']
daystime=list(map(str,input().split()))
if len(daystime) == 2 and daystime[0] in days and daystime[1] in time:
    print("hello")

