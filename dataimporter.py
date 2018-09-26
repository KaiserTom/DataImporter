#Wyatt Humnphreys CNA 330 9/20/18
#Sources: https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
#https://www.periscopedata.com/blog/python-create-table
#https://realpython.com/python-csv/

import os, csv, sqlite3

import csv, sqlite3

con = sqlite3.connect("Public_Computer_Access_Locations.db") #Creates an object that connects to the DB 
cur = con.cursor() #Creates a cursor object that "selects" the DB to execute futher commands
cur.execute("CREATE TABLE t (Lab_name, Phone, Accessible, Hours, Tech_Support_Assisted, Organization, Location, Web_address);") #Calls the cursor object to create table "t" with given column names

with open('Public_Computer_Access_Locations.csv','r') as fin: #Open and read a given spreadsheet and turn it into variable "fin" 
    #csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) #Read a row from the csv file as an OrderedDict object and put that into "dr" 
    #For each entry "i" with a given column name in the "dr" object, create a list "to_db" with those entries in specific positions
    to_db = [(i['Lab_name'], i['Phone'], i['Accessible'], i['Hours'], i['Tech_Support_Assisted'], i['Organization'], i['Location'], i['Web_address']) for i in dr] 

#Take each value in the list "to_db" and insert it into the columns of table "t" based on it's position in the list
cur.executemany("INSERT INTO t (Lab_name, Phone, Accessible, Hours, Tech_Support_Assisted, Organization, Location, Web_address) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db) # ? are used for number of items
con.commit() #Save changes
con.close() #Close the DB connection
