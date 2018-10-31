import sqlite3

conn = sqlite3.connect('s1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS SECTION1(id REAL, eight_am TEXT, nine_am TEXT, ten_am TEXT, eleven_am TEXT, twelve_pm TEXT, one_pm TEXT, two_pm TEXT, three_pm TEXT)')


def data_entry():
    c.execute("INSERT INTO SECTION1 VALUES(1, 'MPMC lab', 'MPMC lab', 'MPMC lab', 'OE', 'Lunch Break', 'Operating System Design', 'Data Communication', 'MPMC')")
    c.execute("INSERT INTO SECTION1 VALUES(1, 'DC lab', 'DC lab', 'DC lab', 'OE', 'Lunch Break', 'Data Communication', 'MPMC', 'Theory of Computation')")
    c.execute("INSERT INTO SECTION1 VALUES(1, 'MPMC lab', 'MPMC lab', 'MPMC lab', 'OE', 'Lunch Break', 'Operating System Design', 'Data Communication', 'MPMC')")
    c.execute("INSERT INTO SECTION1 VALUES(1, 'MPMC lab', 'MPMC lab', 'MPMC lab', 'OE', 'Lunch Break', 'Operating System Design', 'Data Communication', 'MPMC')")
    c.execute("INSERT INTO SECTION1 VALUES(1, 'MPMC lab', 'MPMC lab', 'MPMC lab', 'OE', 'Lunch Break', 'Operating System Design', 'Data Communication', 'MPMC')")
    c.execute("INSERT INTO SECTION1 VALUES(1, 'MPMC lab', 'MPMC lab', 'MPMC lab', 'OE', 'Lunch Break', 'Operating System Design', 'Data Communication', 'MPMC')")
    c.execute("INSERT INTO SECTION1 VALUES(1, 'MPMC lab', 'MPMC lab', 'MPMC lab', 'OE', 'Lunch Break', 'Operating System Design', 'Data Communication', 'MPMC')")

    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
