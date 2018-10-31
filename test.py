from IPython.display import display, HTML
from tabulate import tabulate
import pandas
df = pandas.read_csv('timetable.csv')
# print(df)
# print(df.loc[0][1])
# print(df)
response_sent_text = tabulate(df, tablefmt="grid")
print(response_sent_text)
