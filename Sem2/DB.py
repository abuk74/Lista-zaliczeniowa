import sqlite3


conn = sqlite3.connect('myMix.db')
#conn.execute('''CREATE TABLE myMix(
 #           ID INT PRIMARY KEY NOT NULL,
  #          TITLE TEXT NOT NULL,
   #         AUTHOR TEXT NOT NULL);''')
#print("Tabela utworzona")

def Main():
    selectFunction = int(input("Co chcesz zrobić? "
                           "1 - dodaj utwór"
                           " 2- wyświetl listę utworów"))
    if selectFunction == 2:
        ShowTracks()
    elif selectFunction == 1:
        AddTrack()
    else:
        print("Nie wiem co co chcesz zrobić")


def ShowTracks():
    cursor = conn.execute("SELECT id, title, author from myMix")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def AddTrack():
    id = int(input("Podaj ID utworu: "))
    title = input("Podaj tytuł: ")
    author = input("Podaj autora: ")
    conn.execute("INSERT INTO myMix (ID,TITLE,AUTHOR) VALUES ('{}', '{}', '{}')".format(id, title, author))

Main()
conn.close()
