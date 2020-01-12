import sqlite3

db = sqlite3.connect("exemplo2.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE artist(
  artistid    INTEGER PRIMARY KEY, 
  artistname  TEXT
);
""")
cursor.execute("""
CREATE TABLE track(
  trackid     INTEGER,
  trackname   TEXT, 
  trackartist INTEGER,
  FOREIGN KEY(trackartist) REFERENCES artist(artistid)
);
""")
