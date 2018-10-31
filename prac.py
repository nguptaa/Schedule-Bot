from IPython.display import display, HTML
from tabulate import tabulate
import pandas
df = pandas.read_csv('s1.csv')
print(df)
response_sent_text = tabulate(df, tablefmt="grid")
print(response_sent_text)
