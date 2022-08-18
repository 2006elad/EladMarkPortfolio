import sqlite3

conn = sqlite3.connect('cigarette_box_data.db')

c = conn.cursor()

c.execute("""CREATE TABLE smoke_history_data (Year integer, Month integer, Day integer, Time text)""")

c.execute("""CREATE TABLE current_limit_data (StartHourLimit integer, EndHourLimit integer, YHoursLimit integer,
XCigarettePerHourLimit integer)""")


c.execute("INSERT INTO smoke_history_data VALUES('2021','12','23', '11:14')")
c.execute("INSERT INTO current_limit_data VALUES('23','6','2', '1')")

conn.commit()

conn.close()


# conn = sqlite3.connect('cigarette_box_data.db')
# 
# c = conn.cursor()
# 
# c.execute("""CREATE TABLE current_limit_data (StartHourLimit integer, EndHourLimit integer,
#  AmountOfCigarettesDayLimit integer AmountOfCigarettesEachHour integer)""")

# 
# c.execute("INSERT INTO current_limit_data VALUES('23','6','1')")
# 
# conn.commit()
# c.close()
