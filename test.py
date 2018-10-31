# from IPython.display import display, HTML
# from tabulate import tabulate
# import pandas
# df = pandas.read_csv('timetable.csv')
# print(df)
# print(df.loc[0][1])
# print(df)
# response_sent_text = tabulate(df, tablefmt="grid")
# print(response_sent_text)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['08', '09', '10', '11', '12', '13', '14', '15']
from datetime import datetime
testdate='2018-11-01T02:57:00.000+05:30'
u = datetime.strptime(testdate, '%Y-%m-%dT%H:%M:%S.000+05:30')
v = u.strftime('%A %H:%M %Y-%m-%d').split()
s=days.index(v[0])
x=v[1][0:2]
if x in times:
    z=times.index(x)
else:
    print("incorrrect time")

# print(s)


