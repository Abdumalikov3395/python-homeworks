import sqlite3
with sqlite3.connect('lesson-15.db') as database:
    cursor=database.cursor()
    #ex-1
    query=("""
           create table Roster ( Name TEXT, Species TEXT, Age INT);
           """)
    cursor.executescript(query)
    #ex-2
    query=("""
           insert into Roster ( Name , Species, Age) values ('Benjamin Sisko', 'Human', 40),
           ('Jadzia Dax', 'Trill', 300),('Kira Nerys', 'Bajoran', 29);
           """)
    cursor.executescript(query)
    #ex-3
    query=("""
           UPDATE Roster set Name='Ezri Dax' where Name='Jadzia Dax'
           """)
    cursor.executescript(query)
    #ex-4
    query=("""
           select Name, Age from Roster where Species='Bajoran'
           """)
    cursor.execute(query)
    rows=cursor.fetchall()
    for i in rows:
        print(i)
