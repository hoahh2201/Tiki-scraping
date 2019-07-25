import psycopg2

conn = psycopg2.connect("dbname=CoderTicket_development user=minhdh")
cur = conn.cursor()
cur.execute('SELECT * FROM regions')
notes = cur.fetchall()
print(notes)
conn.close()
