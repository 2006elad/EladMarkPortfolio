import sqlite3

conn = sqlite3.connect('cigarette_box_data.db')

c = conn.cursor()

# c.execute("""DROP TABLE current_limit_data""")
# c.execute("""CREATE TABLE current_limit_data(StartHourLimit integer,
# EndHourLimit integer,
# AmountOfCigarettesDayLimit integer,
# AmountOfCigarettesEachHour integer)""")
# c.execute("""INSERT INTO current_limit_data(StartHourLimit,EndHourLimit,AmountOfCigarettesDayLimit,
# AmountOfCigarettesEachHour) VALUES(?,?,?,?);""", (0, 6, 6, 3))

conn.commit()

conn.close()
