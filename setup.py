#       Name: Jasmine Masopeh
#       FSUID: jdm21e
#       Due Date: 2/21/2024
#       The program in this file is the individual work of Jasmine Masopeh
import sqlite3

conn = sqlite3.connect('movieData.db')
print ('Opened database successfully')

conn.execute('DROP TABLE IF EXISTS Reviews')
conn.execute('DROP TABLE IF EXISTS Movies')


conn.execute('CREATE TABLE Reviews (Username TEXT, MovieID TEXT, ReviewTime SQL Datetime, Rating float, Review TEXT, FOREIGN KEY (MovieID) REFERENCES Movies(MovieID))')
print('Created table')


conn.execute('CREATE TABLE Movies (MovieID TEXT PRIMARY KEY, Title TEXT, Director TEXT, Genre TEXT, Year integer)')
print('Created table')

conn.close()
